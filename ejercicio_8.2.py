import tkinter as tk
from tkinter import ttk

class Notas:
    def __init__(self):
        self.lista_notas = [0.0] * 5
    
    def calcular_promedio(self):
        suma = 0
        for i in range(len(self.lista_notas)):
            suma += self.lista_notas[i]
        return suma / len(self.lista_notas)
    
    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = 0
        for nota in self.lista_notas:
            suma += (nota - prom) ** 2
        return (suma / len(self.lista_notas)) ** 0.5
    
    def calcular_menor(self):
        menor = self.lista_notas[0]
        for nota in self.lista_notas:
            if nota < menor:
                menor = nota
        return menor
    
    def calcular_mayor(self):
        mayor = self.lista_notas[0]
        for nota in self.lista_notas:
            if nota > mayor:
                mayor = nota
        return mayor

class VentanaPrincipal:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Notas")
        self.ventana.geometry("280x380")
        self.ventana.resizable(False, False)
        
        self.inicializar_componentes()
        self.ventana.mainloop()
    
    def inicializar_componentes(self):
        self.nota1 = tk.Label(self.ventana, text="Nota 1:")
        self.nota1.place(x=20, y=20)
        self.campo_nota1 = tk.Entry(self.ventana)
        self.campo_nota1.place(x=105, y=20, width=135, height=23)
        
        self.nota2 = tk.Label(self.ventana, text="Nota 2:")
        self.nota2.place(x=20, y=50)
        self.campo_nota2 = tk.Entry(self.ventana)
        self.campo_nota2.place(x=105, y=50, width=135, height=23)
        
        self.nota3 = tk.Label(self.ventana, text="Nota 3:")
        self.nota3.place(x=20, y=80)
        self.campo_nota3 = tk.Entry(self.ventana)
        self.campo_nota3.place(x=105, y=80, width=135, height=23)
        
        self.nota4 = tk.Label(self.ventana, text="Nota 4:")
        self.nota4.place(x=20, y=110)
        self.campo_nota4 = tk.Entry(self.ventana)
        self.campo_nota4.place(x=105, y=110, width=135, height=23)
        
        self.nota5 = tk.Label(self.ventana, text="Nota 5:")
        self.nota5.place(x=20, y=140)
        self.campo_nota5 = tk.Entry(self.ventana)
        self.campo_nota5.place(x=105, y=140, width=135, height=23)
        
        self.calcular = tk.Button(self.ventana, text="Calcular", command=self.calcular_notas)
        self.calcular.place(x=20, y=170, width=100, height=23)
        
        self.limpiar = tk.Button(self.ventana, text="Limpiar", command=self.limpiar_campos)
        self.limpiar.place(x=125, y=170, width=80, height=23)
        
        self.promedio = tk.Label(self.ventana, text="Promedio = ")
        self.promedio.place(x=20, y=210)
        
        self.desviacion = tk.Label(self.ventana, text="Desviación = ")
        self.desviacion.place(x=20, y=240)
        
        self.mayor = tk.Label(self.ventana, text="Nota mayor = ")
        self.mayor.place(x=20, y=270)
        
        self.menor = tk.Label(self.ventana, text="Nota menor = ")
        self.menor.place(x=20, y=300)
    
    def calcular_notas(self):
        try:
            notas = Notas()
            notas.lista_notas[0] = float(self.campo_nota1.get())
            notas.lista_notas[1] = float(self.campo_nota2.get())
            notas.lista_notas[2] = float(self.campo_nota3.get())
            notas.lista_notas[3] = float(self.campo_nota4.get())
            notas.lista_notas[4] = float(self.campo_nota5.get())
            
            promedio = notas.calcular_promedio()
            desv = notas.calcular_desviacion()
            
            self.promedio.config(text=f"Promedio = {promedio:.2f}")
            self.desviacion.config(text=f"Desviación estándar = {desv:.2f}")
            self.mayor.config(text=f"Valor mayor = {notas.calcular_mayor()}")
            self.menor.config(text=f"Valor menor = {notas.calcular_menor()}")
        except ValueError:
            pass
    
    def limpiar_campos(self):
        self.campo_nota1.delete(0, tk.END)
        self.campo_nota2.delete(0, tk.END)
        self.campo_nota3.delete(0, tk.END)
        self.campo_nota4.delete(0, tk.END)
        self.campo_nota5.delete(0, tk.END)

if __name__ == "__main__":
    app = VentanaPrincipal()
