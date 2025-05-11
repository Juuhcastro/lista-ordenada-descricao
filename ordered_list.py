class Produto:
    def __init__(self, descricao, preco):
        self.descricao = descricao
        self.preco = preco

class No:
    def __init__(self, produto):
        self.produto = produto
        self.proximo = None

class OrderedList:
    def __init__(self):
        self.inicio = None

    def insert(self, produto):
        novo = No(produto)

        if self.inicio is None or produto.descricao < self.inicio.produto.descricao:
            novo.proximo = self.inicio
            self.inicio = novo
        else:
            anterior = None
            atual = self.inicio
            while atual is not None and produto.descricao > atual.produto.descricao:
                anterior = atual
                atual = atual.proximo
            novo.proximo = atual
            anterior.proximo = novo

    def search(self, descricao):
        atual = self.inicio
        while atual is not None and atual.produto.descricao <= descricao:
            if atual.produto.descricao == descricao:
                return atual.produto
            atual = atual.proximo
        return None

    def remove(self, descricao):
        atual = self.inicio
        anterior = None

        while atual is not None and atual.produto.descricao != descricao:
            anterior = atual
            atual = atual.proximo

        if atual is None:
            return False  # não encontrou

        if anterior is None:
            self.inicio = atual.proximo
        else:
            anterior.proximo = atual.proximo

        return True  # removido com sucesso

    def exibir(self):
        atual = self.inicio
        while atual is not None:
            print(f"{atual.produto.descricao} - R$ {atual.produto.preco:.2f}")
            atual = atual.proximo

# Testes
if __name__ == "__main__":
    lista = OrderedList()

    lista.insert(Produto("Feijão", 6.50))
    lista.insert(Produto("Arroz", 5.20))
    lista.insert(Produto("Macarrão", 3.80))
    lista.insert(Produto("Abacate", 4.10))

    print("Lista ordenada por descrição:")
    lista.exibir()

    print("\nBuscando 'Feijão':")
    p = lista.search("Feijão")
    print(f"Encontrado: {p.descricao} - R$ {p.preco:.2f}" if p else "Não encontrado")

    print("\nRemovendo 'Arroz'")
    lista.remove("Arroz")
