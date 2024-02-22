"""
EJERCICIO DEL DÍA 2 NÚMERO 2 MARTES
"""


def validate_input_between_5_and_50_characters(input_data):
    if 5 <= len(input_data) <= 50:
        return True
    else:
        return False


def validate_input_10_characters(input_data):
    if len(input_data) == 10:
        return True
    else:
        return False


def validate_until_true(input_data):
    while True:
        if validate_input_between_5_and_50_characters(input_data):
            break
        else:
            print("El nombre debe tener entre 5 y 50 caracteres")
            input_data = input("Intenta lo de nuevo: ")
    return input_data


def validate_until_true_phone_number(input_data):
    while True:
        if validate_input_10_characters(input_data):
            break
        else:
            print("El teléfono debe tener 10 caracteres")
            input_data = input("Intenta lo de nuevo:")
    return input_data


def sign_up_times():
    names = validate_until_true(input("Escribe tú nombre(s): "))
    last_names = validate_until_true(input("Escribe tú apellido(s): "))
    email = validate_until_true(input("Escribe tú correo electrónico: "))
    phone_number = validate_until_true_phone_number(input("Escribe tú número de teléfono: "))
    return names, last_names, email, phone_number


def sign_up(sign_up_data):
    return f"\n Hola {sign_up_data[0]} {sign_up_data[1]}, en breve recibirás un correo a {sign_up_data[2]}"


if __name__ == "__main__":
    n_times = int(input("¿Cuantos usuarios necesitas registrar? "))
    for n in range(n_times):
        how_many_times = sign_up_times()
        resp = sign_up(how_many_times)
        print(resp)
