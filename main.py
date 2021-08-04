import requests

def main():
    print("####################")
    print("### Consulta CEP ###")
    print("####################")
    print()

    cepInput = input("Digite o CEP para consulta: ")

    if len(cepInput) != 8:
        print("Quantidade de dígitos inválida!")
        exit()

    request = requests.get("https://viacep.com.br/ws/{}/json/".format(cepInput))

    addressData = request.json()

    if "erro" not in addressData:
        print()
        print("==> CEP ENCONTRADO <==")
        print("CEP: {}".format(addressData['cep']))
        print("Logradouro: {}".format(addressData['logradouro']))
        print("Complemento: {}".format(addressData['complemento']))
        print("Bairro: {}".format(addressData['bairro']))
        print("Cidade: {}".format(addressData['localidade']))
        print("Estado: {}".format(addressData['uf']))
    else:
        print("{}: CEP INVÁLIDO!".format(cepInput))

    print("------------------------------")

    option = int(input("Nova consulta?\n1 = Sim\n2 = Sair\n"))

    if option == 1:
        main()
    else:
        print("Adeus")

if __name__ == "__main__":
    main()
