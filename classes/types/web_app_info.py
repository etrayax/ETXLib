from .utils import TeleObj


class WebAppInfo(TeleObj):
    
    """
    
    Describes a https://core.telegram.org/bots/webapps
    
    url :
        
        - String
        - An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps
    
    """
    
    def __init__(
        self,
        url : str = None
    ) -> dict:
        self.update(locals())