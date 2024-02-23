from aiohttp      import web
from urllib.parse import urljoin
from hashlib      import md5

import asyncio
import json

from .types import Update
from .handlers import Decorators
from .methodes import Methodes
from .handlers.utils import BaseHandler
from .utils import CustomObject


class Bot(Methodes):
    
    def __init__(self, api, url, result):
        
        Methodes.__init__(self)

        self.api = api
        self.url = url
        self.result = result
        

class Client(web.Application, Decorators):
    
    def __init__(
            self, 
            host: str = "127.0.0.1", 
            port: int = 7080,
        ):
            
        super().__init__()
        Decorators.__init__(self)
        
        self.connections = {}
        
        self.host = host
        self.port = port
        
        self.handlers = {update_type: set() for update_type in Update.__init__.__code__.co_varnames[2:]}
        
    def register(self, bot_token: str, api: str = "https://api.telegram.org", result: bool = False):
        
        webhook_path = "/" + md5(bot_token.encode()).hexdigest()
        
        self.connections[webhook_path[1:]] = Bot(api.removesuffix("/"), api.removesuffix("/") + "/bot" + bot_token, result)
        
        asyncio.run(
            self.connections[webhook_path[1:]].set_webhook(
                urljoin("http://" + self.host.strip() + ":" + str(self.port), webhook_path),
                allowed_updates=list(self.handlers),
                result=True
            )
        )
        
        self.router.add_post(webhook_path, self.request_handler)
        
    async def request_handler(self, request):
        
        async def proccess(self, request):
            
            result = json.loads(await request.read())
            del result["update_id"]

            for key, value in result.items():
                
                if (c := self.handlers.get(key)):
                    
                    tasks = []
                    
                    for obj in c:
                        
                        tasks.append(
                            obj.func(
                                self.connections[request.url.path.removeprefix("/")], 
                                CustomObject(value)
                            )
                        )
                    
                    asyncio.gather(*tasks)
            
        asyncio.create_task(proccess(self, request))
        return web.Response(text="Successfully!")
 
    def add_handler(self, handler: BaseHandler):
        self.handlers[handler.name].add(handler)
        return handler
    
    def run(self):
        web.run_app(self, host=self.host, port=self.port)