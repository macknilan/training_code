"""
EJERCICIO DEL DÍA 1 NÚMERO 1 LUNES
"""


def record(names, last_names, email):
    return f"Hola {names} {last_names}, en breve recibirás un correo a {email}"


if __name__ == "__main__":
    names = input("Escribe tú nombre(s): ")
    last_names = input("Escribe tú apellido(s): ")
    phone_number = input("Escribe tú número de teléfono: ")
    email = input("Escribe tú correo electrónico: ")
    resp = record(names, last_names, email)
    print(resp)
