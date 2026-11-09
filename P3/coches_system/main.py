from coches import coches
from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0)
        self.main()

    def esperarTecla(self):
        input("...¡Oprima enter para continuar!...")

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()
    
    # def menu_acciones(self,tipo):
    #     print(f"\n\t\t\t...::: Menu de {tipo} :::... \n")
    #     opcion=input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Salir \n \t\tElige una Opcion: ").strip().lower()
    #     return opcion
    
    # ...VISTAS

    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Coches"
        Label(self.ventana,text=f"\n\t\t\t...::: Menu de {tipo} :::... \n").pack(pady=10)
        Button(self.ventana,text="1.-Agregar",command=self.insertar_view).pack(pady=5)
        Button(self.ventana,text="2.-Borrar",command=self.eliminar_view).pack(pady=5)
        Button(self.ventana,text="3.-Modificar",command=self.modificar_view).pack(pady=5)
        Button(self.ventana,text="4.-Mostrar",command=self.consultar_view).pack(pady=5)
        Button(self.ventana,text="5.- Regresar",command=self.main).pack(pady=5)
                
    def main(self):
        self.borrarPantalla()
        Label(self.ventana,text="\n\t M E N U  P R I N C I P A L ").pack(pady=10)
        Button(self.ventana,text="1.-Coches",command=self.menu_acciones).pack(pady=5)
        Button(self.ventana,text="2.-Salir",command=self.ventana.quit).pack(pady=5)

    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="... Ingresar datos del Coche...").pack(pady=10)
        
        Label(self.ventana,text="Marca").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.focus()
        self.marca.pack(pady=5)
        
        Label(self.ventana,text="Color").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)
        
        Label(self.ventana,text="Modelo").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)        
        
        Label(self.ventana,text="Velocidad").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)
        
        Label(self.ventana,text="Potencia").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana,text="Numero de asientos").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(self.ventana,text="Guardar",command=self.insertar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)


    def eliminar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="... Ingresar el ID del Coche a Eliminar...").pack(pady=10)
        
        Label(self.ventana,text="ID").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Button(self.ventana,text="Eliminar",command=self.eliminar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)

    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="... Ingresar el ID del Coche a Modificar...").pack(pady=10)
        
        Label(self.ventana,text="ID").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Label(self.ventana,text="Nueva Marca").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.pack(pady=5)
        
        Label(self.ventana,text="Nuevo Color").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)
        
        Label(self.ventana,text="Nuevo Modelo").pack(pady=5)
        self.modelo=Entry(self.ventana)
        self.modelo.pack(pady=5)        
        
        Label(self.ventana,text="Nueva Velocidad").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)
        
        Label(self.ventana,text="Nueva Potencia").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)

        Label(self.ventana,text="Nuevo Numero de asientos").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)

        Button(self.ventana,text="Guardar",command=self.modificar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)

    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="::: Consultar los Coches :::").pack(pady=10)
        filas=""
        filas=self.consultar_controller(filas)
        Label(self.ventana,text=f"{'No':<20}{'ID':<20}{'Marca':<20}{'color':<20}{'Modelo':<20}{'Velocidad':20}{'potencia':<20}{'asientos':<20}").pack(pady=5)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)


    def insertar_controller(self):
        coche1 = coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta = coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1

    def eliminar_controller(self):
        id=self.id.get()
        respuesta=coches.Coches.eliminar(id)
        self.respuesta_sql(respuesta)

    def consultar_controller(self):
        registros=coches.Coches.consultar()
        if len(registros) > 0:
            num_coches = 1
            for fila in registros:
                filas=filas+f"Coche # {num_coches}\n"f"\tID: {fila[0]}\n"f"\tMarca: {fila[1]}\n"f"\tColor: {fila[2]}\n"f"\tModelo: {fila[3]}\n"f"\tVelocidad: {fila[4]}\n"f"\tPotencia: {fila[5]}\n"f"\tAsientos: {fila[6]}"
            num_coches += 1
            self.esperarTecla()
        else:
            print("\n\t No existen datos que mostrar por el momento... ")

    def modificar_controller(self):
        id=self.id.get()
        coche1 = coches.Coches(self.marca.get(),self.color.get(),self.modelo.get(),self.velocidad.get(),self.potencia.get(),self.asientos.get())
        respuesta = coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1        

    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(title="Exitoso",message="accion realizada con exito")
        else:
            input("accion no exitosa")
            messagebox.showerror(title="Verifica por favor",message="accion no exitosa")
                
    
if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()

#balsamiq 