"""
EJERCICIO DEL DÍA 5 NÚMERO 5 VIERNES
"""


def validate_until_input_between_5_and_50_characters(input_data):
    """
    TODO
    """
    while True:
        if 5 <= len(input_data) <= 50:
            break
        else:
            print("Escribe entre 5 y 50 caracteres")
            input_data = input("Intenta lo de nuevo: ")
    return input_data


def validate_until_true_phone_number(input_data):
    """
    TODO
    """
    while True:
        if len(input_data) == 10:
            break
        else:
            print("El teléfono debe tener 10 caracteres")
            input_data = input("Intenta lo de nuevo: ")
    return input_data


def sign_up_times():
    """
    TODO
    """
    names = validate_until_input_between_5_and_50_characters(input("Escribe tú nombre(s): "))
    last_names = validate_until_input_between_5_and_50_characters(input("Escribe tú apellido(s): "))
    email = validate_until_input_between_5_and_50_characters(input("Escribe tú correo electrónico: "))
    phone_number = validate_until_true_phone_number(input("Escribe tú número de teléfono: "))
    return names, last_names, email, phone_number


def new_user(sign_up_data):
    """
    TODO
    """
    return f"\n Hola {sign_up_data[0]} {sign_up_data[1]}, en breve recibirás un correo a {sign_up_data[2]}"


def list_users():
    """
    TODO
    """
    resp_list_users_id = [x["id"] for x in list_of_users]
    if len(resp_list_users_id) == 0:
        return "No hay usuarios registrados"

    return resp_list_users_id


def edit_user(user_id):
    """
    TODO
    """
    for user in list_of_users:
        if user["id"] == user_id:
            print(f"Usuario encontrado: {user}")
            new_names = input("Escribe tú nombre(s): ")
            new_last_names = input("Escribe tú apellido(s): ")
            new_email = input("Escribe tú correo electrónico: ")
            new_phone_number = input("Escribe tú número de teléfono: ")
            user["names"] = new_names
            user["last_names"] = new_last_names
            user["email"] = new_email
            user["phone_number"] = new_phone_number
            print(f"Usuario editado con éxito: {user}")
            break
    else:
        print("Usuario no encontrado")


def show_user(user_id):
    """
    TODO
    """
    for user in list_of_users:
        if user["id"] == user_id:
            print(user)
            break
    else:
        print("Usuario no encontrado")


def delete_user(user_id):
    """
    TODO
    """
    for user in list_of_users:
        if user["id"] == user_id:
            list_of_users.remove(user)
            print(f"Usuario eliminado con éxito: {user}")
            break
    else:
        print("Usuario no encontrado")


if __name__ == "__main__":
    """
    TODO:
    """
    list_of_users = []
    while True:
        print("+----------------------------------------------+")
        print("SELECCIONA UNA OPCIÓN")
        print("1. Registrar usuario(s): ")
        print("2. Listar usuarios(ID) registrados: ")
        print("3. Mostrar la información del usuario por medio del -ID-: ")
        print("4. Editar usuario por el -ID- del usuario: ")
        print("5. Eliminar usuario por el -ID- del usuario: ")
        print("6. Salir: ")
        print("+----------------------------------------------+")
        option = int(input("Opción: "))

        if option == 1:
            # CREATE USER(S)
            n_times = int(input("¿Cuantos usuarios necesitas registrar?: "))
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
                resp = new_user(how_many_times)
                print(f"\n Usuario {n + 1} registrado con éxito")
        if option == 2:
            # LIST USERS
            print(list_users())
        if option == 3:
            # SHOW DE DETAILS OF THE USER BY ID
            user_id = int(input("Escribe el -ID- del usuario para mostrar: "))
            show_user(user_id)
        if option == 4:
            # EDIT USER BY ID
            user_id = int(input("Escribe el -ID- del usuario a editar: "))
            edit_user(user_id)
        if option == 5:
            # DELETE BY ID
            user_id = int(input("Escribe el -ID- del usuario a eliminar: "))
            delete_user(user_id)
        if option == 6:
            # EXIT
            print("BYE!")
            break
        elif option not in [1, 2, 3, 4, 5, 6]:
            print("Opción no válida")








