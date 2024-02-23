from aiohttp      import web
from urllib.parse import urljoin
from hashlib      import md5

import asyncio
import orjson

from .classes import Features
from .classes.types import Update
from .classes.handlers import Decorators
from .classes.handlers.utils import BaseHandler

from .utils import ObjType

class Client(web.Application, Features, Decorators):
    
    def __init__(
            self, 
            bot_token: str, 
            api: str = "https://api.telegram.org",
            host: str = "127.0.0.1", 
            port: int = 7080,
            result: bool = False
        ):
        super().__init__()
        Decorators.__init__(self)
        
        
        self.result = result
        self.host = host
        self.port = port
        self.api = api
        
        self.url = self.create_path(self.api, bot_token)
        self.webhook_url = urljoin("http://" + host.strip() + ":" + str(port), self.create_webhook_path(bot_token))
        
        self.handlers = {update_type: set() for update_type in Update.__init__.__code__.co_varnames[2:]}
        
        self.on_startup.append(self.startup_handler)
        self.router.add_post(self.webhook_path, self.request_handler)
    
    async def request_handler(self, request):
        
        async def proccess(self, request):
            
            result = orjson.loads(await request.read())
            del result["update_id"]

            for key, value in result.items():
                
                if (c := self.handlers.get(key)):
                    
                    tasks = []
                    
                    for obj in c:
                        
                        tasks.append(
                            obj.func(self, ObjType(value))
                        )
                    
                    asyncio.gather(*tasks)
            
        asyncio.create_task(proccess(self, request))
        return web.Response(text="Successfully!")
    
    async def startup_handler(self, request):
        await self.set_webhook(
            self.webhook_url,
            allowed_updates=list(self.handlers)
        )
    
    def add_handler(self, handler: BaseHandler):
        self.handlers[handler.name].add(handler)
        return handler
            
    def create_path(self, api: str, bot_token: str):
        return urljoin(api.removesuffix("/"), "/bot" + bot_token)
    
    def create_webhook_path(self, bot_token: str):
        return "/" + md5(bot_token.encode()).hexdigest()
    
    def run(self):
        web.run_app(self, host=self.host, port=self.port)