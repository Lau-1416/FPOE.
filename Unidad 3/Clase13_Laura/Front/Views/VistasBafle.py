import tkinter as tk
import re
from tkinter import messagebox
from Front.Controller.Validaciones import Validaciones
from Front.Controller.Comunicacion import Comunicacion
from Front.Controller.Peticiones import Peticiones
from Front.Models.Bafle import Bafle
from Front.Views.Tabla import Tabla
from functools import partial

class VistasBafle():
    def __init__(self):
        titulos = ['ID', 'Marca', 'Tamaño', 'Color', 'Precio']
        columnas = ['id', 'marca', 'tamaño', 'color', 'precio']
        data = []
        self.frame = tk.Tk()
        self.Comunicacion = Comunicacion()
        self.Validaciones = Validaciones()
        self.tabla = Tabla(self.frame, titulos, columnas, data)
    
    def ValidarEntrada(self, valor, etiquetaerror):
        mensaje_erroneo = Validaciones.validarLetras(valor)
        if mensaje_erroneo:
            etiquetaerror.config(text=mensaje_erroneo)
        else:
            etiquetaerror.config(text="")
            
    def BotonGuardar(self, entryId, entryMarca, entryTamaño, entryColor, entryPrecio):
        if id == '':
            self.Comunicacion.guardar(entryId, entryMarca, entryTamaño, entryColor, entryPrecio)
        else:
            messagebox.showwarning("Espera!", "Por favor llene los campos")

    def Bafle_update(id_bafle):
        Peticiones.actualizar(id_bafle, entryMarca.get(), txtEstudiante.get(), txtSalon.get(), txtLocal.get())
        messagebox.showinfo("Éxito", "Universidad actualizada exitosamente.")
        limpiar_campos()  # Limpiar los campos después de actualizar
        actualizar_tabla()  # Actualizar la tabla después de la actualización
        Peticiones.guardar_universidades_en_archivo()
            
    def Actualizar(self):
        Busqueda = {}  
        resultado = Peticiones.Buscar(Busqueda)
        if resultado is not None:
            data = []
            for elemento in resultado:
                data.append((
                    elemento.get('id'),
                    elemento.get('marca'),
                    elemento.get('tamaño'),
                    elemento.get('color'),
                    elemento.get('local')
                ))
            self.tabla.refrescar(data)

    def limpiar_cajas(self):
        self.txtMarca.delete(0,tk.END)
        self.txtTamaño.delete(0,tk.END)
        self.txtColor.delete(0,tk.END)
        self.txtPrecio.delete(0,tk.END)
        self.txtId.delete(0,tk.END)

    def ConsultarTodo(self, marca, tamaño, color, precio):
        resultado = self.Comunicacion.ConsultarTodo(marca, tamaño, color, precio)
        data = []
        for elemento in resultado:
            data.append((elemento.get('id'), elemento.get('marca'), elemento.get('tamaño'), elemento.get('color'), elemento.get('precio')))
        self.tabla.refrescar(data)
        print(resultado)
        print(type(resultado))
    
    def ConsultarBoton1(self, lblConsultaMarca, lblConsultaTamaño, lblConsultaColor, lblConsultaPrecio, id):
        resultado = self.Comunicacion.consultar(id)
        print(resultado)
        print(type(resultado))
        lblConsultaMarca.config(text= resultado.get('marca'))
        lblConsultaTamaño.config(text= resultado.get('tamaño'))
        lblConsultaColor.config(text= resultado.get('color'))
        lblConsultaPrecio.config(text= resultado.get('precio'))

    def Peticion_IngresarBafle(self):
        Peticiones.ingresar_bafle(self.txtMarca, self.txtTamaño, self.txtColor, self.txtPrecio)
    

    def ver_interfaz(self):
        bafle = Bafle(self.frame, id)
        
        lblId = tk.Label(self.frame, text="ID")
        lblId.grid(row=0, column=0, padx=10)
        entryId = tk.Entry(self.frame, textvariable=bafle.id)
        entryId.grid(row=1, column=0)

        lblMarca = tk.Label(self.frame, text="Marca")
        lblMarca.grid(row=2, column=0, padx=20)
        entryMarca = tk.Entry(self.frame, textvariable=bafle.marca)
        entryMarca.grid(row=3, column=0)
        
        txtMarca = tk.Label(self.frame, width=20)
        txtMarca.grid(row=1, column=1, padx=5, pady=5)
        txtMarca.lblAdvertencia1 = tk.Label(self.frame, text='Solo se permiten letras y números', fg="red")
        txtMarca.lblAdvertencia1.grid(row=2, column=1, sticky="w")
        txtMarca.lblAdvertencia1.grid_remove()

        lblTamaño = tk.Label(self.frame, text="Tamaño")
        lblTamaño.grid(row=4, column=0, padx=30)
        entryTamaño = tk.Entry(self.frame, width=20, textvariable=bafle.tamaño)
        entryTamaño.grid(row=5, column=0)

        txtTamaño = tk.Label(self.frame, width=20)
        txtTamaño.grid(row=3, column=1, padx=5, pady=5)
        txtTamaño.lblAdvertencia2 = tk.Label(self.frame, text='Solo se permiten letras y números', fg="red")
        txtTamaño.lblAdvertencia2.grid(row=4, column=1, sticky="w")
        txtTamaño.lblAdvertencia2.grid_remove()

        lblColor = tk.Label(self.frame, text="Color")
        lblColor.grid(row=6, column=0, padx=40)
        entryColor = tk.Entry(self.frame, width=20, textvariable=bafle.color)
        entryColor.grid(row=7, column=0)

        txtColor = tk.Label(self.frame, width=20)
        txtColor.grid(row=5, column=1, padx=5, pady=5)
        txtColor.lblAdvertencia3 = tk.Label(self.frame, text='Solo se permiten letras', fg="red")
        txtColor.lblAdvertencia3.grid(row=6, column=1, sticky="w")
        txtColor.lblAdvertencia3.grid_remove()

        lblPrecio = tk.Label(self.frame, text="Precio")
        lblPrecio.grid(row=8, column=0, padx=50)
        entryPrecio = tk.Entry(self.frame, width=20, textvariable=bafle.precio)
        entryPrecio.grid(row=9, column=0)

        txtPrecio = tk.Label(self.frame, width=20)
        txtPrecio.grid(row=7, column=1, padx=5, pady=5)
        txtPrecio.lblAdvertencia4 = tk.Label(self.frame, text='Solo se permiten letras y números', fg="red")
        txtPrecio.lblAdvertencia4.grid(row=8, column=1, sticky="w")
        txtPrecio.lblAdvertencia4.grid_remove()

        btnGuardar = tk.Button(self.frame, text='Guardar', command=lambda: self.BotonGuardar(entryId.get(), entryMarca.get(), entryTamaño.get(), entryColor.get(), entryPrecio.get()))
        btnGuardar.grid(row=10, column=0)

        btnConsultar1 = tk.Button(self.frame, text="Consulta 1", command=lambda: self.ConsultarBoton1(entryMarca.get(), entryTamaño.get(), entryColor.get(), entryPrecio.get(), entryId.get()))
        btnConsultar1.grid(row=12, column=0)

        btnConsultaTodo = tk.Button(self.frame, text='Consulta de todo', command=lambda: self.ConsultarTodo(entryMarca.get(), entryTamaño.get(), entryColor.get(), entryPrecio.get()))
        btnConsultaTodo.grid(row=14, column=0)

        lblConsultaMarca = tk.Label(self.frame, text='')
        lblConsultaMarca.grid()
        lblConsultaTamaño = tk.Label(self.frame, text='')
        lblConsultaTamaño.grid()
        lblConsultaColor = tk.Label(self.frame, text='')
        lblConsultaColor.grid()
        lblConsultaPrecio = tk.Label(self.frame, text='')
        lblConsultaPrecio.grid()

        marca_error = tk.Label(self.frame, text="", fg="red")
        marca_error.place(x=260, y=20)
        tamaño_error = tk.Label(self.frame, text="", fg="red")
        tamaño_error.place(x=260, y=60)
        color_error = tk.Label(self.frame, text="", fg="red")
        color_error.place(x=260, y=100)
        precio_error = tk.Label(self.frame, text="", fg="red")
        precio_error.place(x=260, y=140)
        
        self.frame.title('Bafle')
        self.frame.geometry("1000x1000")
        self.tabla.tabla.grid()
        
        def SeleccionElemento(_):
            for i in self.tabla.tabla.selection():
                valores = self.tabla.tabla.item(i)['values']
                entryId.delete(0, tk.END)
                entryId.insert(0, str(valores[0]))
                
                entryMarca.delete(0, tk.END)
                entryMarca.insert(0, str(valores[1]))
                
                entryTamaño.delete(0, tk.END)
                entryTamaño.insert(0, str(valores[2]))
                
                entryColor.delete(0, tk.END)
                entryColor.insert(0, str(valores[3]))
            
                entryPrecio.delete(0, tk.END) 
                entryPrecio.insert (0, str(valores[4]))        
                
        def BorrarElemento(_):
            for i in self.tabla.tabla.selection():
                self.Comunicacion.eliminar(self.tabla.tabla.item(i)['values'][0])
                self.tabla.tabla.delete(i)

        txtMarca.bind('<KeyRelease>', Validaciones.Advertencia1)
        txtTamaño.bind('<KeyRelease>', Validaciones.Advertencia2)
        txtColor.bind('<KeyRelease>', Validaciones.Advertencia3)
        txtPrecio.bind('<KeyRelease>', Validaciones.Advertencia4)

        entryMarca.bind("<KeyRelease>", lambda event: self.ValidarEntrada(entryMarca.get(), marca_error))
        entryTamaño.bind("<KeyRelease>", lambda event: self.ValidarEntrada(entryTamaño.get(), tamaño_error))
        entryColor.bind("<KeyRelease>", lambda event: self.ValidarEntrada(entryColor.get(), color_error))
        entryPrecio.bind("<KeyRelease>", lambda event: self.ValidarEntrada(entryPrecio.get(), precio_error))
       
        self.tabla.tabla.bind('<<TreeviewSelect>>', SeleccionElemento)
        self.tabla.tabla.bind('<Delete>', BorrarElemento)

        self.frame.mainloop()        
        