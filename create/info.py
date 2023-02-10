class Info:
    def __init__(self) -> None:
        pass

    
    def createInfo(self, data: dict) -> dict:
        if (not self.populate):
            return self.createInfoPlaceholders()

        temp = dict()

        temp["title"] = data["name"]
        temp["description"] = data["description"]
        temp["termsOfService"] = "http://link-to-your-tos.com/fell-free-to-delete"
        temp["contact"] = {"email": "youremail@feelsafetodelete.com"}
        temp["license"] = {
            "name": "License name, you can delete the 'license' parent",
            "url": "http://license-url.com/"
        }
        temp["version"] = "1.0.0"

        return temp


    def createInfoPlaceholders(self):
        temp = dict()
        
        temp["title"] = None
        temp["description"] = None
        temp["termsOfService"] = None
        temp["contact"] = {"email": None}
        temp["license"] = {
            "name": None,
            "url": None
        }
        temp["version"] = None

        return temp
