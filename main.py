import create
import json
import pyyaml


class Main():
    """
    Transforma uma coleção do Postman em um JSON pronto para ser convertido em
    um YAML no padrão Swagger
    """
    def __init__(self) -> None:
        pass


    def openJson(self, file_name: str) -> dict:
        try:
            with open(file_name) as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            raise FileNotFoundError(f" => O arquivo {file_name} não foi encontrado")


    def transform(self, data: dict) -> dict:
        return create.create(data)


if __name__ == "__main__":
    t = Main()

    json_file = t.openJson("postman-docs.json")

    json_file = t.transform(json_file)

    with open("out.json", "w") as out_file:
        json.dump(json_file, out_file, indent=2, ensure_ascii=False)

    with open("swagger.yaml", "w") as yaml_file:
        pyyaml.dump(json_file, yaml_file, sort_keys=False, indent=2, allow_unicode=True)
