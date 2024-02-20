from typing    import Literal
from threading import Thread
from .utils     import ObjType

import httpx
import orjson


def remove_none_value(input_date: list|dict):
    
    if isinstance(input_date, dict):
        
        for key, value in dict(input_date).items():
            
            if value is None:
                del input_date[key]
            
            elif isinstance(value, (dict, list)):
                remove_none_value(value)
    
    elif isinstance(input_date, list):
        
        for value in input_date:
            
            if value is None:
                input_date.remove(value)
            
            elif isinstance(value, (dict, list)):
                remove_none_value(value)
    
    return input_date

def req(method: Literal["post", "get"], *args, **kwargs):
    
    with httpx.Client() as client:
        try:
            getattr(client, method)(
                *args, **kwargs
            )
        
        except Exception as error:
            print(error)
        
async def post_req(url, json : dict = {}, data : dict = {}, result : bool = True):

    json = remove_none_value(json)
    data = remove_none_value(data)

    async with httpx.AsyncClient() as client:
        
        if result:
            
            try:
                return (await client.post(url, json=json, data=data)).read()

            except Exception as error:
                return {"ok": False,"system": True,"description": error}
        
        else:
            Thread(
                target=req,
                kwargs={
                    "method" : "post",
                    "url" : url,
                    "data" : data,
                    "json" : json
                }
            ).start()
            
            return {}
            
async def get_req(url, result : bool = True):
    
    async with httpx.AsyncClient() as client:
        
        if result:
            
            try:
                return await client.get(url)

            except Exception as error:
                return {"ok": False,"system": True,"description": error}
        
        else:
            Thread(
                target=req,
                kwargs={
                    "method" : "get",
                    "url" : url
                }
            ).start()
        
            return {}
    
async def Request(method: Literal["post", "get"] = "post", *args, **kwargs):
    
    match method:
        
        case "post":
            return ObjType(orjson.loads(c) if not isinstance((c := await post_req(*args, **kwargs)), dict) else c)
            
        case "get":
            return ObjType(orjson.loads(c) if not isinstance((c := await get_req(*args, **kwargs)), dict) else c)
            
    raise ValueError("The method is not valid.")
