import requests
import os

def main():
    os.system('clear')
    print("####################")
    print("### Consulta CEP ###")
    print("####################")
    print()

    def newQuery():
        option = int(input("Nova consulta?\n1 = Sim\n2 = Sair\n"))

        if option == 1:
            main()
        else:
            print("Adeus")
            exit()

    cepInput = input("Digite o CEP para consulta: ")

    if len(cepInput) != 8:
        print()
        print("-------------------------------")
        print("Quantidade de dígitos inválida!")
        print("-------------------------------")
        print()
        newQuery()

    request = requests.get("https://viacep.com.br/ws/{}/json/".format(cepInput))

    addressData = request.json()

    if "erro" not in addressData:
        print()
        print("--------------------------------")
        print("===> CEP ENCONTRADO <===")
        print("CEP: {}".format(addressData['cep']))
        print("Logradouro: {}".format(addressData['logradouro']))
        print("Complemento: {}".format(addressData['complemento']))
        print("Bairro: {}".format(addressData['bairro']))
        print("Cidade: {}".format(addressData['localidade']))
        print("Estado: {}".format(addressData['uf']))
        print("--------------------------------")
        print()
    else:
        print()
        print("---------------------")
        print("{}: CEP INVÁLIDO!".format(cepInput))
        print("---------------------")
        print()

    newQuery()

if __name__ == "__main__":
    main()
