class Response:
    def __init__(self, populate: bool) -> None:
        self.populate = populate


    def populateResponseBody(self, data: dict) -> dict:
        temp = dict()

        if ("code" in data.keys()):
            temp[str(data["code"])] = dict()
            temp[str(data["code"])]["description"] = data["status"]

            try:
                temp[str(data["code"])]["content"] = dict()
                temp[str(data["code"])]["content"][data["header"][0]["value"]] = {"schema": {"$ref": None}}

                if (temp[str(data["code"])]["content"][data["header"][0]["value"]]["schema"]["$ref"] is None):
                    temp[str(data["code"])]["content"][data["header"][0]["value"]]["schema"]["$ref"] = "#/response-schema-nao-definido"
            except:
                temp[str(data["code"])] = {"content": None}
        else:
            return {"999": {"description": "Nao possui responseBody"}}

        return temp


    def createResponseBody(self, data: dict) -> dict:
        if (not self.populate):
            return self.createResponseBodyPlaceholders()
        
        temp = dict()

        if (len(data) == 1):
            return self.populateResponseBody(data[0])
        elif (len(data) > 1):
            for i in data:
                temp = temp | self.populateResponseBody(i)
        else:
            return None
        
        return temp
    

    def createResponseBodyPlaceholders(self) -> dict:
        temp = dict()
        temp[None] = {"descripton": None, "content": {"application/json": {"schema": {"$ref": None}}}}

        return temp
