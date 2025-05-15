from tkinter import *
from tkinter import messagebox

root = Tk()

root.title("Ingreso de Datos")
root.geometry("500x300")

root.config(bg="black", cursor="pirate")

myFrame = Frame(root)
myFrame.config(bg="black")
myFrame.pack(anchor="n",expand=True)

labelNombre = Label(myFrame, text="Nombre:")
labelNombre.grid(row=0, column=0, padx=10, pady=10, sticky="we")
inputNombre = Entry(myFrame, width=65)
inputNombre.grid(row=0, column=1, padx=10, pady=10)

labelApellido = Label(myFrame, text="Apellido:")
labelApellido.grid(row=1, column=0, padx=10, pady=10)
inputApellido = Entry(myFrame, width=65)
inputApellido.grid(row=1, column=1, padx=10, pady=10, sticky="we")

labelEmail = Label(myFrame, text="Email:")
labelEmail.grid(row=2, column=0, padx=10, pady=10, sticky="we")
inputEmail = Entry(myFrame, width=65)
inputEmail.grid(row=2, column=1, padx=10, pady=10)


labelDev = Label(root, text="Hecho por: Lautaro Ignacio Arias", font=("Arial", 13, "bold"))
labelDev.config(fg="white", bg="black")
labelDev.pack(fill="x")


# funciones de validacion

def validar_cadena(cadena): 
    #Validar nombre y apellido ingresado
    resultado = True 
    pos = 0
    if len(cadena) > 25: 
        resultado=False
    while pos < len(cadena) and resultado: 
        if not cadena[pos].isalpha(): 
            resultado=False
        pos += 1 

    if not resultado: 
        messagebox.showwarning("ERROR", "Formato de nombre o apellido inválido")
    return resultado 


def validar_email(email): 
    resultado = True
    if email[0] in "@" or email[-1] in "@": 
        resultado = False
    if len(email) > 20: 
        resultado = False
    
    pos = 1
    count = 0
    while pos < len(email)-1 and resultado: 
        if email[pos] == "@": 
            count += 1 
        if count > 1: 
            resultado = False 
        pos += 1
    
    if count != 1: 
        resultado = False
    
    if not resultado:
        messagebox.showwarning("ERROR", "Formato de email inválido")

    return resultado 

def validacion(nombre,apellido,email):
    if(nombre and apellido and email): 
        nombre_validado = validar_cadena(nombre)
        apellido_validado = validar_cadena(apellido)
        email_validado = validar_email(email)
        if nombre_validado and apellido_validado and email_validado: 
            messagebox.showinfo("AVISO", "Los datos fueron recibidos")
    else: 
        messagebox.showwarning("ERROR","No se han llenado todos los campos")

   

def validate():
    validacion(inputNombre.get(),inputApellido.get(),inputEmail.get())

boton = Button(
myFrame, 
text="Enviar >", 
command=validate, 
height=1, 
font=("Verdana", 8, "bold"), 
bg="#83C0DF", 
fg="white",
activebackground="#4CAF50", 
activeforeground="white",
borderwidth=1,
relief="raised",
cursor="hand2"
)
boton.grid(row=3, column=1, padx=10, pady=10, sticky="we")
    
root.mainloop()