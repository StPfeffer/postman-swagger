from .populate import Populate


class Create():
    def __init__(self) -> None:
        pass


    def createInfo(self, data: dict) -> dict:
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


    def createServers(self, data: dict) -> list:
        temp = dict()
        l = list()

        for i in data:
            if (str(i["value"]).startswith("http")):
                temp["url"] = i["value"]

                l.append(temp)

        return l
    

    def createTags(self, data: dict) -> list:
        l = list()
        temp = dict()

        for i in data:
            temp["name"] = i["name"]
            try:
                temp["description"] = str(i["description"]).split(".")[0]
            except:
                temp["description"] = ""
            
            l.append(temp.copy())

        return l
    

    def createParameters(self, data: dict) -> list:
        param = list()

        for i in data["request"]["url"]["path"]:
            if ("{{" in i): # check if there's a parameter in the url path
                if (";" in i): # check if there's more than 1 parameter
                    for j in i.split(";"):
                        param.append(j[2:-2])
                else:
                    param.append(i[2:-2])

        if (param):
            return Populate.populateParams(param)


    def createRequestBody(self, data: dict, method: str) -> dict:
        if (method == "get"):
            return None

        try:
            return Populate.populateRequestBody(data["header"][0]["value"])
        except:
            return None
    

    def createResponseBody(self, data: dict, method: str) -> dict:
        temp = dict()

        if (len(data) == 1):
            return Populate.populateResponseBody(data[0])
        elif (len(data) > 1):
            for i in data:
                temp = temp | Populate.populateResponseBody(i)
        else:
            return None
        
        return temp
    

    def createPathDescription(self, d: dict, data: dict) -> dict:
        try:
            d["summary"] = str(data["description"]).split(".")[0]
        except:
            d["summary"] = ""

        try:
            d["description"] = data["description"]
        except:
            d["description"] = ""

        return d


    def createPaths(self, data: dict) -> dict:
        temp = dict()
        
        for i in data:
            for data in i["item"]:
                path = f"/{data['request']['url']['path']}"

                if (len(path) == 1):
                    path = path[0]
                elif (len(path) > 1):
                    path = path.replace("', '", "/").replace("['", "").replace("']", "")

                try:
                    path = path.replace("{{", "{")
                    path = path.replace("}}", "}")
                except:
                    pass

                methods = f"{data['request']['method'].lower()}"

                temp[path] = dict()
                temp[path][methods] = dict()

                temp[path][methods]["tags"] = [i["name"]]

                temp[path][methods] = self.createPathDescription(temp[path][methods], data["request"])

                temp[path][methods]["parameters"] = self.createParameters(data)

                # delete the parameters key if it's value is None
                if (temp[path][methods]["parameters"]):
                    pass
                else:
                    del temp[path][methods]["parameters"]

                temp[path][methods]["requestBody"] = self.createRequestBody(data["request"], methods)

                if (temp[path][methods]["requestBody"] is None):
                    del temp[path][methods]["requestBody"]

                temp[path][methods]["responses"] = self.createResponseBody(data["response"], methods)
        
        return temp


    def createComponents(self, data: dict) -> dict:
        return 
    

    def create(self, data: dict) -> dict:
        new_data = dict()

        new_data["openapi"] = "3.0.3"

        if ("info" in data.keys()):
            new_data["info"] = self.createInfo(data["info"])

        if ("variable" in data.keys()):
            new_data["servers"] = self.createServers(data["variable"])

            if (new_data["servers"] == []):
                del new_data["servers"]
        
        if ("item" in data.keys()):
            new_data["tags"] = self.createTags(data["item"])
            new_data["paths"] = self.createPaths(data["item"])
            new_data["components"] = self.createComponents(data["item"])

        return new_data


if __name__ == "__main__":
    Create()
