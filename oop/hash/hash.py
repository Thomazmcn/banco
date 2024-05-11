import hashlib
import os


def hash_password(user_pass):
    password = user_pass.encode("utf-8")  # Convertendo a senha para bytes
    salt = os.urandom(16)  # Gerando um salt aleatório

    hash = hashlib.sha256()  # Usando o método sha256() para criar um objeto hash
    hash.update(password + salt)  # Adicionando a senha e o salt ao objeto hash

    return hash.hexdigest(), salt


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


senha = new_secret()
hash_test, salt_test = hash_password(senha)
senha_test = input("senha test:\n")
print(verify_pass(senha_test, hash_test, salt_test))
