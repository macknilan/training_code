"""
EJERCICIO DEL DÍA 3 NÚMERO 3 MIÉRCOLES
"""


def validate_until_input_between_5_and_50_characters(input_data):
    while True:
        if 5 <= len(input_data) <= 50:
            break
        else:
            print("Escribe entre 5 y 50 caracteres")
            input_data = input("Intenta lo de nuevo: ")
    return input_data


def validate_until_true_phone_number(input_data):
    while True:
        if len(input_data) == 10:
            break
        else:
            print("El teléfono debe tener 10 caracteres")
            input_data = input("Intenta lo de nuevo: ")
    return input_data


def sign_up_times():
    names = validate_until_input_between_5_and_50_characters(input("Escribe tú nombre(s): "))
    last_names = validate_until_input_between_5_and_50_characters(input("Escribe tú apellido(s): "))
    email = validate_until_input_between_5_and_50_characters(input("Escribe tú correo electrónico: "))
    phone_number = validate_until_true_phone_number(input("Escribe tú número de teléfono: "))
    return names, last_names, email, phone_number


def sign_up(sign_up_data):
    return f"\n Hola {sign_up_data[0]} {sign_up_data[1]}, en breve recibirás un correo a {sign_up_data[2]}"


if __name__ == "__main__":
    n_times = int(input("¿Cuantos usuarios necesitas registrar?: "))

    list_of_users = []

    for n in range(n_times):
        how_many_times = sign_up_times()
        list_of_users.append(
            {
                "id": n + 1,
                "names": how_many_times[0],
                "last_names": how_many_times[1],
                "email": how_many_times[2],
                "phone_number": how_many_times[3]
            }
        )
        resp = sign_up(how_many_times)
        print(f"\n Usuario {n + 1} registrado con éxito")

    print(list_of_users)
