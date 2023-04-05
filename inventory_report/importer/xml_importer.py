import xml.etree.ElementTree as Et
from .importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path: str):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        data = []
        with open(path) as file:
            xml_root = Et.parse(file).getroot()
            for record in xml_root.findall(".//record"):
                produto_dict = {}
                for tag in record:
                    produto_dict[tag.tag] = tag.text
                data.append(produto_dict)
        return data
