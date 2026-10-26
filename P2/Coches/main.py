from coches import coches

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

    def datos_coche(self,tipo):
        self.borrarPantalla()
        print(f"\n\t... Ingresar datos del {tipo}")
        cochesitos={}
        cochesitos['marca']=input("marca: ").upper().strip()
        cochesitos['color']=input("Color: ").upper().strip()
        cochesitos['modelo']=input("modelo: ").upper().strip()
        cochesitos['velocidad']=input("velocidad (Km/h): ").strip()
        cochesitos['potencia']=input("potencia Hp: ").strip()
        cochesitos['asientos']=input("# de asientos: ").strip()
        # return marca,color,modelo,velocidad,potencia,asientos
        return cochesitos
    
    def menu_coche(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = self.menu_acciones("Coches")
            match opcion:
                case '1':
                    cochesitos = self.datos_coche("coche")
                    coche1 = coches.Coches(
                        cochesitos['marca'],
                        cochesitos['color'],
                        cochesitos['modelo'],
                        cochesitos['velocidad'],
                        cochesitos['potencia'],
                        cochesitos['asientos']
                    )
                    respuesta = coche1.insertar()
                    self.respuesta_sql(respuesta)
                    del coche1

                case '2':
                    self.borrarPantalla()
                    id = input("Ingrese el ID del coche a eliminar ").strip()
                    respuesta = coches.Coches.eliminar(id)
                    self.respuesta_sql(respuesta)

                case '3':
                    id = input("Ingrese el ID del coche a modificar ").strip()
                    cochesitos = self.datos_coche("coche")
                    coche1 = coches.Coches(
                        cochesitos['marca'],
                        cochesitos['color'],
                        cochesitos['modelo'],
                        cochesitos['velocidad'],
                        cochesitos['potencia'],
                        cochesitos['asientos']
                    )
                    respuesta = coche1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del coche1

                case '4':
                    self.borrarPantalla()
                    registros = coches.Coches.consultar()
                    if len(registros) > 0:
                        num_coches = 1
                        for fila in registros:
                            print(
                                f"Coche # {num_coches}\n"
                                f"\tID: {fila[0]}\n"
                                f"\tMarca: {fila[1]}\n"
                                f"\tColor: {fila[2]}\n"
                                f"\tModelo: {fila[3]}\n"
                                f"\tVelocidad: {fila[4]}\n"
                                f"\tPotencia: {fila[5]}\n"
                                f"\tAsientos: {fila[6]}"
                            )
                            num_coches += 1
                            self.esperarTecla()
                    else:
                        print("\n\t No existen datos que mostrar por el momento... ")

                case '5':
                    opcion = False

                case _:
                    input("opcion invalida, vuelva a intentarlo")

    
    def main(self):
        opcion=True
        while opcion:
            self.borrarPantalla()
            print("menu principal")
            opcion=input("\n\t 1.-Coches \n\t 2.-Salir \n \t\tElige una Opcion: ").strip().lower()
            match opcion:
                case '1':
                    self.borrarPantalla()
                    self.menu_coche()
                    self.esperarTecla()
                case '2':
                    self.borrarPantalla()   
                    print("\n\t...Salir del sistema...")
                    opcion=False
                case _:
                    input("opcion invalida, vuelva a intentarlo")

    
if __name__=="__main__":
    app=App()

