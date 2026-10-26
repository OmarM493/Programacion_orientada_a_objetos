from estudiantes import estudiantes

class App:
    def __init__(self):
        self.main()

    def esperarTecla(self):
        input("...¡Oprima enter para continuar!...")

    def borrarPantalla(self):
        print("\033c")
    
    def menu_acciones(self,tipo):
        print(f"\n\t\t\t...::: Menu de {tipo} :::... \n")
        opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Salir \n \t\tElige una Opcion: ").strip().lower()
        return opcion
    
    def respuesta_sql(self,respuesta):
        if respuesta:
            input("accion exitosa")
        else:
            input("accion no exitosa")

    def datos_estudiante(self,tipo):
        self.borrarPantalla()
        print(f"\n\t... Ingresar datos del {tipo}")
        estudiantito={}
        estudiantito['nombre']=input("Nombre: ").upper().strip()
        estudiantito['nota']=input("Calificacion: ").upper().strip()
        return estudiantito
    
    def menu_estudiantes(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            opcion=self.menu_acciones("Estudiantes")
            match opcion:
                case '1':
                    estudiantitos=self.datos_estudiante("estudiante")
                    estudiante1=estudiantes.Estudiantes(estudiantitos['nombre'],estudiantitos['nota'])
                    respuesta=estudiante1.insertar()
                    self.respuesta_sql(respuesta)
                    del estudiante1

                case '2':
                    self.borrarPantalla()
                    id=input("Ingrese el ID del estudiante a eliminar ").strip()
                    respuesta=estudiantes.Estudiantes.eliminar(id)
                    self.respuesta_sql(respuesta)

                case '3':
                    id=input("Ingrese el ID del estudiante a modificar ").strip()
                    estudiante1=estudiantes.Estudiantes(estudiantitos['nombre'],estudiantitos['nota'])
                    respuesta=estudiante1.actualizar(id)
                    self.respuesta_sql(respuesta)


                case '4':
                    self.borrarPantalla()
                    registros=estudiantes.Estudiantes.consultar()
                    if len(registros)>0:
                        num_estudiantes=1
                        for fila in registros:
                         print(f"estudiante # {num_estudiantes}\n\tID: {fila[0]}\n\tNombre: {fila[1]}\n\tNota: {fila[2]}")
                         num_estudiantes+=1
                         self.esperarTecla()
                    else:
                        print("\n\t No existen datos que mostrar por el momento... ")

                case '5':
                    opcion=False
                case _:
                    input("opcion invalida, vuelva a intentarlo")
    

    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            print("menu principal")
            opcion=input("\n\t 1.-Estudiantes \n\t 2.-Salir \n \t\tElige una Opcion: ").strip().lower()
            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_estudiantes()
                    self.esperarTecla()
                case '2':
                    self.borrarPantalla()   
                    print("\n\t...Salir del sistema...")
                    opcion=False
                case _:
                    input("opcion invalida, vuelva a intentarlo")


if __name__=="__main__":
    app=App()
