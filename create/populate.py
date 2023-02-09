class Populate():
    def __init__(self) -> None:
        pass


    def populateRequestBody(data: dict) -> dict:
        temp = dict()

        temp["content"] = {data: {"schema": {"$ref": None}}}


        if (temp["content"][data]["schema"]["$ref"] is None):
            temp["content"][data]["schema"]["$ref"] = "#/request-schema-nao-definido"

        return temp


    def populateResponseBody(data: dict) -> dict:
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
            return {}

        return temp

    
    def populateParams(param: list) -> list:
        temp = dict()

        temp["name"] = None
        temp["in"] = "path"
        temp["description"] = None
        temp["required"] = True
        temp["schema"] = {"type": "string"}

        if (temp["description"] is None):
            temp["description"] = "Descricao nao definida"

        if (len(param) == 1):
            temp["name"] = param[0]

            return [temp]
        elif (len(param) > 1): # if there's more than 1 parameter
            aux_list = list()

            for i in range(len(param)):
                temp["name"] = param[i]

                aux_list.append(temp.copy())

            return aux_list


if __name__ == "__main__":
    Populate()