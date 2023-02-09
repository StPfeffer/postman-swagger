class Parameter:
    def __init__(self, populate: bool) -> None:
        self.populate = populate


    def populateParams(self, param: list) -> list:
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


    def createParameters(self, data: dict) -> list:
        if (not self.populate):
            return self.createParametersPlaceholders()

        param = list()

        for i in data["request"]["url"]["path"]:
            if ("{{" in i): # check if there's a parameter in the url path
                if (";" in i): # check if there's more than 1 parameter
                    for j in i.split(";"):
                        param.append(j[2:-2])
                else:
                    param.append(i[2:-2])

        if (param):
            return self.populateParams(param)
        

    def createParametersPlaceholders(self) -> list:
        temp = dict()
        temp["name"] = None
        temp["in"] = None
        temp["description"] = None
        temp["required"] = None
        temp["schema"] = {"type": None}

        return [temp]

