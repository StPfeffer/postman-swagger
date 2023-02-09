from .parameter import *
from .request import *
from .response import *


class Path:
    def __init__(self, populate: bool) -> None:
        self.populate = populate

        self.param = Parameter(self.populate)
        self.req = Request(self.populate)
        self.res = Response(self.populate)


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

    
    def createPath(self, data: dict) -> dict:
        if (not self.populate):
            return self.createPathPlaceholders()

        temp = dict()
        
        for i in data:
            for j in i["item"]:
                path = f"/{j['request']['url']['path']}"

                if (len(path) == 1):
                    path = path[0]
                elif (len(path) > 1):
                    path = path.replace("', '", "/").replace("['", "").replace("']", "")

                try:
                    path = path.replace("{{", "{")
                    path = path.replace("}}", "}")
                except:
                    pass

                methods = f"{j['request']['method'].lower()}"

                temp[path] = dict()
                temp[path][methods] = dict()

                temp[path][methods]["tags"] = [i["name"]]

                temp[path][methods] = self.createPathDescription(temp[path][methods], j["request"])

                temp[path][methods]["parameters"] = self.param.createParameters(j)

                # delete the parameters key if it's value is None
                if (temp[path][methods]["parameters"]):
                    pass
                else:
                    del temp[path][methods]["parameters"]

                temp[path][methods]["requestBody"] = self.req.createRequestBody(j["request"], methods)

                if (temp[path][methods]["requestBody"] is None):
                    del temp[path][methods]["requestBody"]

                temp[path][methods]["responses"] = self.res.createResponseBody(j["response"])
        
        return temp
    

    def createPathPlaceholders(self) -> dict:
        temp = dict()
        temp["/your-path"] = {"request-method": {"tags": [None], "summary": None, "description": None}}
        temp["/your-path"]["request-method"]["requestBody"] = {"content": {"application/json": {"schema": {"$ref": None}}}}
        temp["/your-path"]["request-method"]["responses"] = {"response-code": {"description": None, "content": {"application/json": {"schema": {"$ref": None}}}}}

        return temp
