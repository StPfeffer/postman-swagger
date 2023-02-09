import json
from create.create import Create


class Transform():
    """
    Transforma uma coleção do Postman em um JSON pronto para ser convertido em um YAML Swagger
    """
    def __init__(self) -> None:
        pass


    def openJson(self, file_name: str) -> dict:
        try:
            with open(file_name) as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            raise FileNotFoundError(f"O arquivo {file_name} não foi encontrado")


    def transform(self, data: dict) -> dict:
        create = Create()
        new_data = dict()

        new_data["openapi"] = "3.0.3"

        if ("info" in data.keys()):
            new_data["info"] = create.createInfo(data["info"])

        if ("variable" in data.keys()):
            new_data["servers"] = create.createServers(data["variable"])
        
        if ("item" in data.keys()):
            new_data["tags"] = create.createTags(data)
            new_data["paths"] = create.createPaths(data)
            new_data["components"] = create.createComponents(data)

        return new_data


if __name__ == "__main__":
    t = Transform()

    json_file = t.openJson("postman-docs.json")

    json_file = t.transform(json_file)

    with open("out.json", "w") as out_file:
        json.dump(json_file, out_file, indent=2, ensure_ascii=False)
