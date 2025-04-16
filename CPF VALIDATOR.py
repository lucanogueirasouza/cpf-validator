while True:
    cpf = input(
        "Digite um cpf: "
    )

    if len(cpf) > 11: 
        print (
            "O cpf deve ter 11 digitos."
        )

    nove_digitos = cpf[:9]
    contagem_reg_num_one = 10
    resultado_digito_1 = 0

    for numeros in nove_digitos:
        resultado_digito_1 += int(numeros) * contagem_reg_num_one
        contagem_reg_num_one -= 1
    digito_1 = (resultado_digito_1 * 10) % 11
    if digito_1 < 9: 
        digito_1 = digito_1
    else: 
        digito_1 = 0 

    dez_digitos = nove_digitos + str(digito_1)
    contador_reg_num_two = 11
    resultado_digito_2 = 0

    for numeros in dez_digitos:
        resultado_digito_2 += int(numeros) * contador_reg_num_two
        contador_reg_num_two -= 1
    digito_2 = (resultado_digito_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0

    cpf_gerado = (
        f'{nove_digitos}{digito_1}{digito_2}'
    )

    if cpf == cpf_gerado:
        print(
            "CPF VALIDO"
        )
        break
    else:
        print(
            "CPF INVALIDO"
        )
        break