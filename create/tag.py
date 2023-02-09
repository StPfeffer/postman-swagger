class Tag:
    def __init__(self, populate: bool) -> None:
        self.populate = populate

    
    def createTag(self, data: dict) -> list:
        if (not self.populate):
            return self.createTagPlaceholders()

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
    

    def createTagPlaceholders(self) -> list:
        temp = dict()
        temp["name"] = None
        temp["description"] = None

        return [temp]
