from .creator import *


def create_all(data: dict, populate: bool, Creator=Creator) -> dict:
    creator = Creator(populate)

    new_data = dict()


    new_data["openapi"] = "3.0.3"

    if (not populate):
        new_data["openapi"] = None

    if ("info" in data.keys()):
        new_data["info"] = creator.createInfo(data["info"])

    if ("variable" in data.keys()):
        new_data["servers"] = creator.createServer(data["variable"])

        if (new_data["servers"] == []):
            del new_data["servers"]

    if ("item" in data.keys()):
        new_data["tags"] = creator.createTag(data["item"])
        new_data["paths"] = creator.createPath(data["item"])
        new_data["components"] = creator.createComponent(data["item"])

    return new_data


def create(data, populate=True, Creator=Creator):
    return create_all(data, populate, Creator=Creator)
