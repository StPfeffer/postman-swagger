class Server:
    def __init__(self, populate: bool) -> None:
        self.populate = populate

    
    def createServer(self, data: dict) -> list:
        if (not self.populate):
            return self.createServerPlaceholders()

        temp = dict()
        l = list()

        for i in data:
            if (str(i["value"]).startswith("http")):
                temp["url"] = i["value"]

                l.append(temp)

        return l


    def createServerPlaceholders(self) -> list:
        temp = dict()
        temp["url"] = None

        return [temp]
