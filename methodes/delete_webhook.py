from ETXLib.Request import Request

class deleteWebhook:
    
    """
    
    Use this method to remove webhook integration if you decide to switch back to getUpdates. Returns True on success.

    Parameters :

        drop_pending_updates (Boolean) => Optional : Pass True to drop all pending updates
            
    """
    
    async def delete_webhook(
        self,
        drop_pending_updates : bool =None,
        *,
        api: str = None,
        result: bool = None
    ):
        
        return await Request(
            'post',
            url=(api or self.url) + "/deleteWebhook",
            json={
                "drop_pending_updates" : drop_pending_updates
            },
            result=result if result is not None else self.result
        )