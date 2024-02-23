from .utils import DictType


class WebAppInfo(DictType):
    
    """
    
    Describes a https://core.telegram.org/bots/webapps
    
    Parameters :
    
        url (String) => Required : An HTTPS URL of a Web App to be opened with additional data as specified in Initializing Web Apps
    
    """
    
    def __init__(
        self,
        url : str = None
    ) -> dict:
        
        self.url : str = url
        
        self.update(locals())