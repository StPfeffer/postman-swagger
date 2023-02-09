from .populate import Populate


class Create():
    def __init__(self) -> None:
        pass


    def createInfo(self, data: dict) -> dict:
        temp = dict()
        temp["title"] = data["name"]
        temp["description"] = data["description"]
        temp["version"] = "1.0.0"

        return temp

    
    def createServers(self, data: dict) -> list:
        temp = dict()
        l = list()

        return l
    

    def createTags(self, data: dict) -> list:
        l = list()
        temp = dict()

        for i in data["item"]:
            temp["name"] = i["name"]
            try:
                temp["description"] = str(i["description"]).split(".")[0]
            except:
                temp["description"] = ""
            
            l.append(temp.copy())

        return l
    

    def createParameters(self, data: dict) -> list:
        param = list()
        temp = dict()

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

        return Populate.populateRequestBody(data["header"][0]["value"])
    

    def createResponseBody(self, data: dict, method: str) -> dict:
        temp = dict()

        if (len(data) == 1):
            return Populate.populateResponseBody(data[0])
        elif (len(data) > 1):
            for i in data:
                if ("code" in i.keys()):
                    temp[str(i["code"])] = dict()
                    temp[str(i["code"])]["description"] = data[0]["status"]

                    try:
                        temp[str(i["code"])]["content"] = dict()
                        temp[str(i["code"])]["content"][data[0]["header"][0]["value"]] = {"schema": {"$ref": None}}

                        if (temp[str(i["code"])]["content"][data[0]["header"][0]["value"]]["schema"]["$ref"] is None):
                            temp[str(i["code"])]["content"][data[0]["header"][0]["value"]]["schema"]["$ref"] = "#/referencia-de-schema-nao-definida"
                    except:
                        temp[str(i["code"])] = {"content": None}
                else:
                    temp[str(i["code"])] = None
        else:
            return None
        
        return temp


    def createPaths(self, data: dict) -> dict:
        temp = dict()

        for i in data["item"]:
            for j in i["item"]:
                path = f"/{j['request']['url']['path']}"

                if (len(path) == 1):
                    path = path[0]
                elif (len(path) > 1):
                    path = path.replace("', '", "/").replace("['", "").replace("']", "")

                methods = f"{j['request']['method'].lower()}"

                temp[path] = dict()
                temp[path][methods] = dict()

                temp[path][methods]["tags"] = [i["name"]]

                try:
                    temp[path][methods]["summary"] = str(j["request"]["description"]).split(".")[0]
                except:
                    temp[path][methods]["summary"] = ""

                try:
                    temp[path][methods]["description"] = j["request"]["description"]
                except:
                    temp[path][methods]["description"] = ""

                temp[path][methods]["parameters"] = self.createParameters(j)

                # delete the parameters key if it's value is None
                if (temp[path][methods]["parameters"]):
                    pass
                else:
                    del temp[path][methods]["parameters"]

                temp[path][methods]["requestBody"] = self.createRequestBody(j["request"], methods)

                if (temp[path][methods]["requestBody"] is None):
                    del temp[path][methods]["requestBody"]

                temp[path][methods]["responses"] = self.createResponseBody(j["response"], methods)


        return temp
    

    def createComponents(self, data: dict) -> dict:
        return 


if __name__ == "__main__":
    Create()
