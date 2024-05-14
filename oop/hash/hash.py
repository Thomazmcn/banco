import hashlib
import os
import psycopg2


def hash_password(user_pass):
    password = user_pass.encode("utf-8")  # Convertendo a senha para bytes
    salt = os.urandom(16)  # Gerando um salt aleatório

    hash = hashlib.sha256()  # Usando o método sha256() para criar um objeto hash
    hash.update(password + salt)  # Adicionando a senha e o salt ao objeto hash

    return hash.hexdigest(), salt


def four_numbers_bank_agency():
    agency_n_4dig = False
    message_ag = "Enter your agency number: "
    while agency_n_4dig is False:
        input_ag_num = input(message_ag)
        valid_ag_n = len(input_ag_num) == 4 and input_ag_num.isdigit()
        if valid_ag_n:
            agency_n_4dig = True
            return input_ag_num
        else:
            message_ag = "Agency number consist of 4 numbers."


def valid_account():
    # search for agency number on db
    account_n_6dig = False
    message_acc = "Enter your account number: "
    while account_n_6dig is False:
        input_acc_num = input(message_acc)
        valid_acc_n = len(input_acc_num) == 4 and input_acc_num.isdigit()
        if valid_acc_n:
            account_n_6dig = True
            return input_acc_num
        else:
            pass


def verify_pass(password_input, hash_db, salt_db):
    # get salt and hash from db
    password_bytes = password_input.encode("utf-8")
    hash = hashlib.sha256()
    hash.update(password_bytes + salt_db)
    if hash.hexdigest() == hash_db:
        return "Autentication ok"
    else:
        return "Access Denied"


def new_secret():
    good_pass = False
    message = "Enter a new password:\n"
    while good_pass is False:
        user_pass = input(message)
        strong = (
            len(user_pass) >= 8
            and any(char.isupper() for char in user_pass)
            and any(char.islower() for char in user_pass)
            and any(char.isdigit() for char in user_pass)
            and any(not char.isalnum() for char in user_pass)
        )
        if strong:
            good_pass = True
            return user_pass
        else:
            message = (
                "To creat a strong password you should use more than 8 characters."
            )


"""
login()
senha = new_secret()
hash_test, salt_test = hash_password(senha)
senha_test = input("senha test:\n")
print(verify_pass(senha_test, hash_test, salt_test))"""
