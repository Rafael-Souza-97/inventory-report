import csv
import json
import xml.etree.ElementTree as Et
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def read(path):
    with open(path) as file:
        if path.endswith(".csv"):
            data = csv.DictReader(file)
            return [row for row in data]
        elif path.endswith(".json"):
            data = file.read()
            return json.loads(data)
        elif path.endswith(".xml"):
            data = []
        with open(path) as inventory_xml:
            xml_root = Et.parse(inventory_xml).getroot()
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
