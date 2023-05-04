from ClassE import Email
import csv


def punto1():
    nombre = input("Ingrese el nombre de la persona: ")
    id_cuenta = input("Ingrese el id de la cuenta: ")
    dominio = input("Ingrese el dominio: ")
    tipo_dominio = input("Ingrese el tipo de dominio: ")
    contrasena = input("Ingrese la contraseña: ")
    em = Email(id_cuenta, dominio, tipo_dominio, contrasena)
    print(f"Estimado {nombre}, te enviaremos tus mensajes a la dirección: ")
    em.retornaemail()
    return em


def punto2(em):
    em.modificar_contra()


def punto3():
    mail = Email()
    d = input("Ingrese correo: ")
    c = input("Ingrese contraseña: ")
    mail.crearcuenta(d, c)


def punto4():
    archivo = open("cuentas.csv")
    reader = csv.reader(archivo, delimiter=",")
    correos = []
    for fila in reader:
        if "@" in fila[0] and "." in fila[0]:
            mail = Email()
            mail.crearcuenta(fila[0], fila[1])
            correos.append(mail)
        else:
            print("El correo {} es invalido". format(fila[0]))

    dominioIngresado = input("Ingrese dominio: ")
    cont = 0
    for correo in correos:
        if dominioIngresado == correo.retornadominio():
            cont += 1
    print("Los objetos que tienen el dominio {} son: {}". format(dominioIngresado, cont))


if __name__ == "__main__":
    email = punto1()
    punto2(email)
    punto3()
    punto4()
