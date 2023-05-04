class Email:
    def __init__(self, cuen="", dominio="", dom="", contrasena=""):
        self.__cuenta = cuen
        self.__dom = dominio
        self.__tipodom = dom
        self.__contra = contrasena

    def retornaemail(self):
        return print(self.__cuenta+"@"+self.__dom+"."+self.__tipodom)

    def retornadominio(self):
        return self.__dom

    def crearcuenta(self, correo, contra):
        lista1 = correo.split("@")
        self.__cuenta = lista1[0]
        lista2 = lista1[1].split(".")
        self.__dom = lista2[0]
        self.__tipodom = lista2[1]
        self.__contra = contra


    def modificar_contra(self):
        contra_actual = input("Ingrese su contraseña actual: ")
        if contra_actual == self.__contra:
            nueva_contra = input("Ingrese su nueva contraseña: ")
            self.__contra = nueva_contra
            print("Contraseña modificada con éxito")

        else:
            print("Contraseña actual incorrecta")
