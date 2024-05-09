agencias = ['1234']
clientes = [['1234','1234'],['1234','2345'],['1234','3456']]
logon = [['1234','1234','1234',0],['1234','2345','1234',-100000],['1234','3456','1234',100000]]

def Main():
    
    ag_temp = input('\nDigite sua agencia: ')
    
    if ag_temp == 'ad':
        password = 's'
        codigo = input('Digite senha de acesso adm: ')
        if codigo == password:
            return menu_adm()
        
        else:
            print ('********** Acesso negado! **********')
            return Main()
        
    elif ag_temp in agencias:
        cc_temp = input('\nDigite sua conta:')
        senha_temp = input('\nDigite sunha senha:')
        clientes_temp = [ag_temp,cc_temp] #variavel criada para possibilitar a identificaçao pos logon. 
        
        if clientes_temp in clientes:
            indice = clientes.index(clientes_temp)
            saldo = logon[indice][3]
            logon_temp = [ag_temp,cc_temp,senha_temp,saldo]
            
            if logon_temp in logon:
                return menu_clientes(clientes_temp)
            
            else:
                print('\n********** Senha invalida! **********')
                return Main()
        
        else:
            print('\n********** Conta invalida! **********')
            return Main()
        
    
    elif ag_temp == 'teste':
        print(agencias, clientes, logon, sep='\n\n')
        return Main()

    else:
        print('\n********** Agencia invalida! ********** ')
        return Main()

   

def menu_adm():
    print('\n Menu adm:',' 1-Criar agencias',' 2-Criar contas',' 3-Editar contas',' 4-Apagar contas',' 5-Sair', sep='\n')
    op = input('\nDigite a opção para acesso: ')
    if op == '1':
        return criar_ag()
    
    elif op =='2':
        return criar_conta()
    
    elif op == '3':
        return editar_conta()

    elif op =='4':
        return apagar_conta()

    elif op =='5' or op == 'sair':
        return Main()
    
    else:
        print('********** Comando invalido! **********')
        return menu_adm()


def criar_ag():
    ag_temp = input(' \nDigite uma nova agencia contendo 4 digitos: ')

    if len(ag_temp) == 4 and ag_temp.isnumeric():
        if ag_temp in agencias:
            print ('\n********** Agencia ja existente. **********')
            return criar_ag()
        
        elif ag_temp not in agencias:
            agencias.append(ag_temp)
            print('\n********** Agencia criada. **********')
            return menu_adm()

        else:
            print('\nErro!')
    
    elif ag_temp == 'sair':
        return menu_adm()

    else:
        print ('\n********** Agencia invalida. **********')
        return criar_ag() 

def criar_conta():
    ag_temp = input(' \nDigite a agencia a qual pertence a nova conta: ')
    
    if ag_temp in agencias:
        cc_temp = '0b'
        senha_temp = '0b'

        while not cc_temp.isnumeric() or len(cc_temp) != 4 or len(senha_temp) != 4 or not senha_temp.isnumeric():
            cc_temp = input('\nDigite numero de conta com 4 digitos: ')
            senha_temp = input('\nDigite senha do cliente com 4 digitos: ')
            if not cc_temp.isnumeric() or not senha_temp.isnumeric():
                print('\n********** Tanto conta quanto senha devem ser numericos! **********')
                    
        saldo_temp = 0 
        list_temp = [ag_temp, cc_temp]
        logon_temp = [ag_temp, cc_temp, senha_temp, saldo_temp]
        
        if list_temp not in clientes:
            clientes.append(list_temp)
            logon.append(logon_temp)
            print('\n********** Conta criada com sucesso! **********')
            return menu_adm()

        else:
            print('\n********** Conta ja existe! **********')
            return criar_conta()
            
    elif ag_temp == 'sair':
        return menu_adm()

    else:
        print ('\n********** Agencia invalida. **********')
        return criar_conta() 

def editar_conta():
    senha_temp = 'blabla'
    ag_temp = input('\nModo de edição de conta ativado. \n\nDigite Agencia: ')
    cc_temp = input('\nDigite conta corrente: ')
    clientes_temp = [ag_temp, cc_temp]
    cc_temp2 = 'blablabla'
    clientes_temp2 = []
    logon_temp = []

    if clientes_temp in clientes:
        indice = clientes.index(clientes_temp)
        saldo = logon[indice][3]
        clientes.pop(indice)
        logon.pop(indice)
        
        while not cc_temp2.isnumeric() or len(cc_temp2) != 4 or len(senha_temp) != 4 or not senha_temp.isnumeric() or clientes_temp2 in clientes:
            cc_temp2 = input('\nDigite nova conta corrente: ')
            senha_temp = input('\nDigite nova senha: ')
            clientes_temp2 = [ag_temp, cc_temp2]
            logon_temp = [ag_temp, cc_temp2, senha_temp, saldo]
            if not cc_temp2.isnumeric() or not senha_temp.isnumeric():
                print('\n********** Tanto conta quanto senha devem ser numericos! **********')
            elif clientes_temp2 in clientes:
                print('\n********** Edição criará duplicidade de contas. Defina outros valores! **********')

        clientes.append(clientes_temp2)
        logon.append(logon_temp)
        print('\n********** Alteração efetuada com sucesso! **********')
        return menu_adm()

    elif ag_temp == 'sair':
        return menu_adm()
    else:
        print('\nDados invalidos.')
        return editar_conta()

def apagar_conta():
    ag_temp = input('\nModo apagar conta ativado. \n\nDigite Agencia: ')
    cc_temp = input('\nDigite conta corrente: ')
    clientes_temp = [ag_temp, cc_temp]

    if clientes_temp in clientes:
        indice = clientes.index(clientes_temp)
        saldo = logon[indice][3]
        
        if saldo < 0:
            print('\n********** Ação bloqueada. Conta possui $',saldo,'em conta. **********')
            return menu_adm()

        elif saldo > 0:
            print('\n********** Ação bloqueada. Conta possui $',saldo,'em conta. **********')
            return menu_adm()
        
        else:
            clientes.pop(indice)
            logon.pop(indice)
            print('\n********** Conta apagada com sucesso! ************')
            return menu_adm()


    elif ag_temp == 'sair':
        return menu_adm()
    
    else:
        print('\nDados invalidos.')
        return editar_conta()

def menu_clientes(clientes_temp):
    print('\n********** Bem vindo ao Banco Blablabla.S/A **********','\n Menu inicial:',' 1-Editar senha',' 2-Transferir',' 3-Sacar',' 4-Depositar',' 5-Saldo',' 6-Fechar conta',' 7-Sair', sep='\n')
    op = input('\nDigite a opção para acesso: ')
    

    if op == '1':
        return editar_senha(clientes_temp)
    
    elif op =='2':
        return transferir(clientes_temp)
    
    elif op == '3':
        return sacar(clientes_temp)

    elif op =='4':
        return depositar(clientes_temp)

    elif op =='5':
        return saldo(clientes_temp)
    
    elif op =='6':
        return fechar_conta(clientes_temp)
    
    elif op =='7' or op == 'sair':
        return Main()
    
    else:
        print('\n********** Comando invalido! **********')
        return Main()

def editar_senha(clientes_temp):
    nova_senha = 'blablabla'
    while len(nova_senha) !=4 or not nova_senha.isnumeric():
        nova_senha = input('\nDigite sua nova senha com 4 numeros:')
        if len(nova_senha)!=4 or not nova_senha.isnumeric():
            print ('\n********** Sua senha precisa ter 4 numeros! **********')
    
    indice = clientes.index(clientes_temp)
    del logon[indice][3]
    logon[indice].insert(3, nova_senha)
    print('\n********** Senha alterada com sucesso. **********')
    return menu_clientes(clientes_temp)

def transferir(clientes_temp):
    destinatario = ['blabla','bleble']
    valor = '0'

    while destinatario not in clientes or destinatario == clientes_temp:
        ag_destino = input('\nDigite a agencia de destinatario: ')
        cc_destino = input('\nDigite a conta corrente do destinatario: ')
        destinatario = [ag_destino,cc_destino]
        if destinatario not in clientes or destinatario == clientes_temp:
            print('\n********** Dados invalidos! **********')
        
    while not valor.isnumeric() or float(valor) <=0:
        valor = input('Digite o valor a ser transferido:')
        if not valor.isnumeric():
            print('\n********** O valor deve ser um numero positivo. **********')
        elif float(valor) <= 0:
            print('\n********** Valores a serem transferidos devem ser posivitos. **********')
    valor = float(valor)
        
    indice_origem = clientes.index(clientes_temp)
    indice_destino = clientes.index(destinatario)
    saldo_remetente = logon[indice_origem][3] - valor
    saldo_destinatario = logon[indice_destino][3] + valor
    logon[indice_destino].insert(3, saldo_destinatario)
    logon[indice_origem].insert(3, saldo_remetente)
    del logon[indice_destino][-1]
    del logon[indice_origem][-1]
    print('\n********** Transferencia efetuada com sucesso. **********')    

    return menu_clientes(clientes_temp)

def sacar(clientes_temp):
    valor = '0'
    while not valor.isnumeric() or float(valor) <=0:
        valor = input('Digite o valor a ser sacado:')
        if not valor.isnumeric():
            print('\n********** O valor deve ser um numero positivo. **********')
        elif float(valor) <= 0:
            print('\n********** Valores a serem sacado devem ser posivitos. **********')
        
    valor = float(valor)

    indice_temp = clientes.index(clientes_temp)
    saldo = logon[indice_temp][3] - valor
    logon[indice_temp].insert(3, saldo)
    del logon[indice_temp][-1]
    print('\n ********** Saque efetuado com sucesso **********')

    return menu_clientes(clientes_temp)

def depositar(clientes_temp):
    valor = '0'
    while not valor.isnumeric() or float(valor) <=0:
        valor = input('Digite o valor a ser depositado:')
        if not valor.isnumeric():
            print('\n********** O valor deve ser um numero positivo. **********')
        elif float(valor) <= 0:
            print('\n********** Valores a serem sacado devem ser posivitos. **********')
    valor = float(valor)


    indice_temp = clientes.index(clientes_temp)
    saldo = logon[indice_temp][3] + valor
    logon[indice_temp].insert(3, saldo)
    del logon[indice_temp][-1]
    print('\n ********** Deposito efetuado com sucesso **********')
    return menu_clientes(clientes_temp)

def saldo(clientes_temp):
    indice_temp = clientes.index(clientes_temp)
    saldo = logon[indice_temp][3]
    print('\n$',saldo)
    return menu_clientes(clientes_temp)

def fechar_conta(clientes_temp):
    indice_temp = clientes.index(clientes_temp)
    saldo = logon[indice_temp][3]
    if saldo < 0:
        print('\n********** Ação bloqueada. Conta possui $',saldo,'em conta. **********')
        return menu_clientes()

    elif saldo > 0:
        print('\n********** Ação bloqueada. Conta possui $',saldo,'em conta. **********')
        return menu_clientes()
        
    else:
        clientes.pop(indice_temp)
        logon.pop(indice_temp)
        print('\n********** Conta apagada com sucesso! ************')
        return Main()
    
    
    #tratar inputs no menu cliente para que nao sejam inseridos caracteres alfabeticos.

Main()
