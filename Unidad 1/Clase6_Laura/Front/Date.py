import tkinter as tk
import requests 
from tkinter import messagebox


def ingresar_bafle():
    marca = txtMarca.get()
    tamaño = txtTamaño.get()
    color = txtColor.get()
    precio = txtPrecio.get()

    if not marca or not tamaño or not color or not precio:
        messagebox.showwarning("Error", "Por favor completa todos los campos.")
        return

    data = {
        "marca": marca,
        "tamaño": tamaño,
        "color": color,
        "precio": precio
    }

    #url
    url = 'http://127.0.0.1:8000/v1/bafle'

    try:
        response = requests.post(url, json=data)
        if response.status_code == 201:  
            messagebox.showinfo("Exito", "Información creada con exito")
        else:
            messagebox.showerror("Error", f"Error al agregar la información sobre el bafle: {response.text}")
    except Exception as e:
        messagebox.showerror("Error", f"Error al conectar con la API: {str(e)}")


principal = tk.Tk()
principal.title('Bafle')
principal.geometry("240x220")

frame = tk.Frame(principal, padx=10, pady=10)
lblTitulo = tk.Label(frame, text='Ingresar Datos')
lblTitulo.grid(row=0, column=0, columnspan=2) 

lblMarca = tk.Label(frame, text='Marca:')
lblMarca.grid(row=1, column=0, padx=5, pady=5)  
lblTamaño = tk.Label(frame, text='Tamaño:')
lblTamaño.grid(row=2, column=0, padx=5, pady=5)
lblColor = tk.Label(frame, text='Color:')
lblColor.grid(row=3, column=0, padx=5, pady=5)
lblPrecio = tk.Label(frame, text='Precio:')
lblPrecio.grid(row=4, column=0, padx=5, pady=5)

txtMarca = tk.Entry(frame, width=20)
txtMarca.grid(row=1, column=1, padx=5, pady=5)  
txtTamaño = tk.Entry(frame, width=20)
txtTamaño.grid(row=2, column=1, padx=5, pady=5)
txtColor = tk.Entry(frame, width=20)
txtColor.grid(row=3, column=1, padx=5, pady=5)  
txtPrecio = tk.Entry(frame, width=20)
txtPrecio.grid(row=4, column=1, padx=5, pady=5)  

btnIngresar = tk.Button(frame, text='Ingresar', command=ingresar_bafle)
btnIngresar.grid(row=5, column=1, columnspan=2)

frame.pack(padx=10, pady=10)

principal.mainloop()    