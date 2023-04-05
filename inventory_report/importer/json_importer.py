import json
from .importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if not path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            data = file.read()
            return json.loads(data)
