from collections import Counter
from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(data):
        fabr_mais_ant = min(product["data_de_fabricacao"] for product in data)
        menor_validade = min(
            (product["data_de_validade"] for product in data if product
                ["data_de_validade"] >= datetime.now().strftime("%Y-%m-%d"))
        )

        empresas = [product["nome_da_empresa"] for product in data]
        mais_produtos = Counter(empresas).most_common(1)[0][0]

        report = (
            f"Data de fabricação mais antiga: {fabr_mais_ant}\n"
            f"Data de validade mais próxima: {menor_validade}\n"
            f"Empresa com mais produtos: {mais_produtos}"
        )

        return report
