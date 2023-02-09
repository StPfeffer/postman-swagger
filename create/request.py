class Request:
    def __init__(self, populate: bool) -> None:
        self.populate = populate


    def populateRequestBody(self, data: dict) -> dict:
        temp = dict()

        temp["content"] = {data: {"schema": {"$ref": None}}}

        if (temp["content"][data]["schema"]["$ref"] is None):
            temp["content"][data]["schema"]["$ref"] = "#/request-schema-nao-definido"

        return temp


    def createRequestBody(self, data: dict, method: str) -> dict:
        if (not self.populate):
            return self.createRequestBodyPlaceholders()
        
        if (method == "get"):
            return None

        try:
            return self.populateRequestBody(data["header"][0]["value"])
        except:
            return None
        

    def createRequestBodyPlaceholders(self) -> dict:
        temp = dict()
        temp["content"] = {"application/json": {"schema": {"$ref": None}}}

        return temp
