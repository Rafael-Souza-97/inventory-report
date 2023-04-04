from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        "TechShop",
        "Processador I9",
        "01/01/2023",
        "N/A",
        "123456789",
        "Local arejado, sem umidade",
    )

    assert product.id == 1
    assert product.nome_do_produto == "TechShop"
    assert product.nome_da_empresa == "Processador I9"
    assert product.data_de_fabricacao == "01/01/2023"
    assert product.data_de_validade == "N/A"
    assert product.numero_de_serie == "123456789"
    assert product.instrucoes_de_armazenamento == "Local arejado, sem umidade"
