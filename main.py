class Produto:
    def __init__(self, id, nome, categoria, quantidade, preco, localizacao):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao = localizacao

class Estoque:
    def __init__(self):
        self.produtos = {}

    def cadastrar_produto(self, id, nome, categoria, quantidade, preco, localizacao):
        if id in self.produtos:
            print("Produto já cadastrado!")
        else:
            self.produtos[id] = Produto(id, nome, categoria, quantidade, preco, localizacao)
            print(f"Produto {nome} cadastrado com sucesso!")

    def atualizar_estoque(self, id, quantidade):
        if id in self.produtos:
            self.produtos[id].quantidade += quantidade
            print(f"Estoque atualizado: {self.produtos[id].quantidade} unidades de {self.produtos[id].nome}.")
        else:
            print("Produto não encontrado!")

    def localizar_produto(self, id):
        if id in self.produtos:
            return f"Produto {self.produtos[id].nome} está na localização {self.produtos[id].localizacao}."
        return "Produto não encontrado!"

    def gerar_relatorio(self):
        print("\nRelatório de Estoque:")
        for produto in self.produtos.values():
            status = "Estoque Baixo" if produto.quantidade < 5 else "OK"
            print(f"{produto.nome} - {produto.quantidade} unidades - {status}")


estoque = Estoque()
estoque.cadastrar_produto(1, "Mouse Gamer", "Periféricos", 10, 150.00, "A1-B3")
estoque.atualizar_estoque(1, -2)
print(estoque.localizar_produto(1))
estoque.gerar_relatorio()