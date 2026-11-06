nome_academia = "Senac Maromba"
print("Bem vindo ao Senai Maromba! \n")
print("Valor: 150 reais mensal")
print("Comece seu cadastro abaixo. \n")

idade = int(input("Informe sua idade: "))

if idade < 0:
    print("Não é possivel que você tenha esta idade!")
elif idade < 16:
    print("Não foi possivel realizar sua matricula")

elif idade == 16 or idade == 17:
    autorização = input("Possui autorização? (s/n) ")
    if autorização == "s" :
        cpf = int(input("Informe seu CPF: "))
        input("Informe seu email: ")
        input("Crie uma senha: ")
        pagamento = float(input("Faça o pagamento de 3 meses adiantado: "))
        if pagamento != 450:
            print(f"O valor {pagamento} do pagamento está errado! Consulte nossos funcionarios para solucionar o problema!")
        
        else: 
            print(f"Pagamento realizado com sucesso. Bem-vindo(a) a academia {nome_academia}")
            
    elif autorização == "n":
        print("Sua matrícula foi negada!")

else:
    cpf = int(input("Informe seu CPF: "))
    input("Informe seu email: ")
    input("Crie uma senha: ")
    pagamento = float(input("Faça o pagamento de 3 meses adiantado: "))
    if pagamento != 450:
        print(f"O valor {pagamento} do pagamento está errado! Consulte nossos funcionarios para solucionar o problema!")

    else: 
        print(f"Pagamento realizado com sucesso. Bem-vindo(a) a academia {nome_academia}")
    
