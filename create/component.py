class Component:
    def __init__(self) -> None:
        pass

    
    def createComponent(self, data: dict) -> dict:
        if (not self.populate):
            return self.createComponentPlaceholders()
        
        return {}

    
    def createComponentPlaceholders(self) -> dict:
        temp = dict()
        temp["schemas"] = {None: {"type": None, "properties": {None: {"type": None, "format": None, "example": None}}}}
        temp["requestBodies"] = {None: {"description": None, "content": {"application/json": {"schema": {"$ref": None}}}}}
        temp["securitySchemes"] = {None: {"type": None, "flows": {"implicit": {"authorizationUrl": None, "scopes": {None: None}}}}}

        return temp
