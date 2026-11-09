from estudiantes import estudiantes
from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de estudiantes")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0)
        self.main()

    def borrarPantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    # ...VISTAS

    def main(self):
        self.borrarPantalla()
        Label(self.ventana,text="\n\t M E N U  P R I N C I P A L ").pack(pady=10)
        Button(self.ventana,text="1.-Estudiantes",command=self.menu_acciones).pack(pady=5)
        Button(self.ventana,text="2.-Salir",command=self.ventana.quit).pack(pady=5)

    def menu_acciones(self):
        self.borrarPantalla()
        tipo="Estudiantes"
        Label(self.ventana,text=f"\n\t\t\t...::: Menu de {tipo} :::... \n").pack(pady=10)
        Button(self.ventana,text="1.-Agregar",command=self.insertar_view).pack(pady=5)
        Button(self.ventana,text="2.-Borrar",command=self.eliminar_view).pack(pady=5)
        Button(self.ventana,text="3.-Modificar",command=self.modificar_view).pack(pady=5)
        Button(self.ventana,text="4.-Mostrar",command=self.consultar_view).pack(pady=5)
        Button(self.ventana,text="5.-Regresar",command=self.main).pack(pady=5)

    def insertar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="... Ingresar datos del Estudiante ...").pack(pady=10)

        Label(self.ventana,text="Nombre").pack(pady=5)
        self.nombre=Entry(self.ventana)
        self.nombre.focus()
        self.nombre.pack(pady=5)

        Label(self.ventana,text="Calificacion").pack(pady=5)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)

        Button(self.ventana,text="Guardar",command=self.insertar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)

    def eliminar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="... Ingresar el ID del Estudiante a Eliminar ...").pack(pady=10)

        Label(self.ventana,text="ID").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Button(self.ventana,text="Eliminar",command=self.eliminar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)

    def modificar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="... Ingresar el ID del Estudiante a Modificar ...").pack(pady=10)

        Label(self.ventana,text="ID").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus()
        self.id.pack(pady=5)

        Label(self.ventana,text="Nuevo Nombre").pack(pady=5)
        self.nombre=Entry(self.ventana)
        self.nombre.pack(pady=5)

        Label(self.ventana,text="Nueva Calificacion").pack(pady=5)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)

        Button(self.ventana,text="Guardar",command=self.modificar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=10)

    def consultar_view(self):
        self.borrarPantalla()
        Label(self.ventana,text="::: Consultar los Estudiantes :::").pack(pady=10)

        filas=self.consultar_controller()

        # Text con scroll para que quepan todos los registros en la ventana
        marco=Frame(self.ventana)
        marco.pack(pady=5,fill=BOTH,expand=True)
        scroll=Scrollbar(marco)
        scroll.pack(side=RIGHT,fill=Y)
        texto=Text(marco,height=20,width=60,yscrollcommand=scroll.set)
        texto.pack(side=LEFT,fill=BOTH,expand=True)
        scroll.config(command=texto.yview)
        texto.insert(END,filas)
        texto.config(state=DISABLED)

        Button(self.ventana,text="Regresar",command=self.menu_acciones).pack(pady=5)

    # ...CONTROLLERS

    def insertar_controller(self):
        estudiante1=estudiantes.Estudiantes(self.nombre.get().upper().strip(),self.nota.get().upper().strip())
        respuesta=estudiante1.insertar()
        self.respuesta_sql(respuesta)
        del estudiante1

    def eliminar_controller(self):
        id=self.id.get().strip()
        respuesta=estudiantes.Estudiantes.eliminar(id)
        self.respuesta_sql(respuesta)

    def modificar_controller(self):
        id=self.id.get().strip()
        estudiante1=estudiantes.Estudiantes(self.nombre.get(),self.nota.get())
        respuesta=estudiante1.actualizar(id)
        self.respuesta_sql(respuesta)
        del estudiante1

    def consultar_controller(self):
        filas=""
        registros=estudiantes.Estudiantes.consultar()
        if len(registros) > 0:
            num_estudiantes=1
            for fila in registros:
                filas=filas+(
                    f"Estudiante # {num_estudiantes}\n"
                    f"\tID: {fila[0]}\n"
                    f"\tNombre: {fila[1]}\n"
                    f"\tNota: {fila[2]}\n\n"
                )
                num_estudiantes+=1
        else:
            filas="\n\t No existen datos que mostrar por el momento..."
        return filas

    def respuesta_sql(self,respuesta):
        if respuesta:
            messagebox.showinfo(title="Exitoso",message="Accion realizada con exito")
        else:
            messagebox.showerror(title="Verifica por favor",message="Accion no exitosa")


if __name__=="__main__":
    ventana=Tk()
    app=App(ventana)
    ventana.mainloop()