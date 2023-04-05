import csv
import json
import xml.etree.ElementTree as Et
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def read(path):
    if path.endswith(".csv"):
        with open(path) as file:
            data = csv.DictReader(file)
            return [row for row in data]
    elif path.endswith(".json"):
        with open(path) as file:
            data = file.read()
            return json.loads(data)
    elif path.endswith(".xml"):
        return read_xml(path)
    else:
        raise ValueError("Formato de arquivo não suportado.")


def read_xml(path):
    data = []
    with open(path) as file:
        xml_root = Et.parse(file).getroot()
        for record in xml_root.findall(".//record"):
            produto_dict = {}
            for tag in record:
                produto_dict[tag.tag] = tag.text
            data.append(produto_dict)
    return data


class Inventory:
    @staticmethod
    def import_data(path, type):
        data = read(path)
        if type == "simples":
            return SimpleReport.generate(data)
        elif type == "completo":
            return CompleteReport.generate(data)
