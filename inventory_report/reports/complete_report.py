from .simple_report import SimpleReport
from collections import Counter


class CompleteReport:
    @staticmethod
    def generate(data):
        simple_report = SimpleReport.generate(data)
        empresas = [produto["nome_da_empresa"] for produto in data]
        empresas_sem_duplicatas = []
        for empresa in empresas:
            if empresa not in empresas_sem_duplicatas:
                empresas_sem_duplicatas.append(empresa)
        produtos_por_empresa = Counter(empresas)
        report = f"{simple_report}\nProdutos estocados por empresa:\n"
        for empresa in empresas_sem_duplicatas:
            quantidade = produtos_por_empresa[empresa]
            report += f"- {empresa}: {quantidade}\n"
        return report
