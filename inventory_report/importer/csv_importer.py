import csv
from .importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if not path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            data = csv.DictReader(file)
            return [row for row in data]
