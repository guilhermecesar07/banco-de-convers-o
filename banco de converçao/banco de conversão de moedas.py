import json
import urllib.request
import urllib.error

MOEDAS = {
    "1": ("BRL", "Real", "R$"),
    "2": ("USD", "Dólar", "US$"),
    "3": ("EUR", "Euro", "€"),
}

URL_COTACAO = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL"


def obter_cotacoes():
    with urllib.request.urlopen(URL_COTACAO, timeout=10) as resposta:
        dados = json.loads(resposta.read().decode("utf-8"))
    return {
        "BRL": 1.0,
        "USD": float(dados["USDBRL"]["bid"]),
        "EUR": float(dados["EURBRL"]["bid"]),
    }


def escolher_moeda(mensagem):
    while True:
        print("==================================")
        print(mensagem)
        print("==================================")
        print("1 - Real (BRL)")
        print("2 - Dólar (USD)")
        print("3 - Euro (EUR)")
        print("0 - Sair")
        print("==================================")
        opcao = input("digite a opção desejada: ")
        if opcao in MOEDAS or opcao == "0":
            return opcao
        print("Opção inválida!")


def ler_valor():
    while True:
        texto = input("Digite o valor a converter: ").strip().replace(",", ".")
        try:
            valor = float(texto)
            if valor < 0:
                print("Digite um valor positivo!")
                continue
            return valor
        except ValueError:
            print("Valor inválido!")


def formatar(valor, simbolo):

    texto = f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{simbolo} {texto}"


def converter():
    origem = escolher_moeda("   Qual moeda você TEM?")
    if origem == "0":
        return False

    destino = escolher_moeda("   Para qual moeda quer CONVERTER?")
    if destino == "0":
        return False

    if origem == destino:
        print("A moeda de origem e destino são iguais!")
        return True

    valor = ler_valor()

    try:
        taxas = obter_cotacoes()
    except (urllib.error.URLError, TimeoutError, KeyError, ValueError):
        print("Não foi possível obter a cotação. Verifique sua internet e tente novamente.")
        return True

    cod_o, nome_o, simb_o = MOEDAS[origem]
    cod_d, nome_d, simb_d = MOEDAS[destino]

    
    resultado = valor * taxas[cod_o] / taxas[cod_d]
    cotacao = taxas[cod_o] / taxas[cod_d]

    print("\n----------------------------------")
    print(f"Cotação: 1 {cod_o} = {cotacao:.4f} {cod_d}")
    print(f"{formatar(valor, simb_o)} = {formatar(resultado, simb_d)}")
    print("----------------------------------\n")
    return True


def tela_inicial():
    while True:
        print("==================================")
        print("        CONVERSOR DE MOEDAS")
        print("==================================")
        print("1 - Converter moeda")
        print("0 - Sair")
        print("==================================")

        opcao = input("digite a opção desejada: ")
        if opcao == "1":
            print(" --> Conversão de moeda ")
            if not converter():
                print("Encerrando o sistema...")
                break
        elif opcao == "0":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida!")
            continue


if __name__ == "__main__":
    tela_inicial()
