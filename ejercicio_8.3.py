import tkinter as tk
from tkinter import messagebox
import math

class Cilindro:
    def __init__(self, radio, altura):
        self.radio = radio
        self.altura = altura
    
    def get_volumen(self):
        return math.pi * self.radio ** 2 * self.altura
    
    def get_superficie(self):
        return 2 * math.pi * self.radio * (self.radio + self.altura)

class Esfera:
    def __init__(self, radio):
        self.radio = radio
    
    def get_volumen(self):
        return (4/3) * math.pi * self.radio ** 3
    
    def get_superficie(self):
        return 4 * math.pi * self.radio ** 2

class Piramide:
    def __init__(self, base, altura, apotema):
        self.base = base
        self.altura = altura
        self.apotema = apotema
    
    def get_volumen(self):
        return (1/3) * self.base ** 2 * self.altura
    
    def get_superficie(self):
        return self.base ** 2 + 2 * self.base * self.apotema

class VentanaCilindro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cilindro")
        self.root.geometry("280x210")
        self.root.resizable(False, False)
        
        self.radio_label = tk.Label(root, text="Radio (cms):")
        self.radio_label.pack()
        
        self.radio_entry = tk.Entry(root)
        self.radio_entry.pack()
        
        self.altura_label = tk.Label(root, text="Altura (cms):")
        self.altura_label.pack()
        
        self.altura_entry = tk.Entry(root)
        self.altura_entry.pack()
        
        self.calcular_btn = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular_btn.pack()
        
        self.volumen_label = tk.Label(root, text="Volumen (cm3):")
        self.volumen_label.pack()
        
        self.superficie_label = tk.Label(root, text="Superficie (cm2):")
        self.superficie_label.pack()
    
    def calcular(self):
        try:
            radio = float(self.radio_entry.get())
            altura = float(self.altura_entry.get())
            cilindro = Cilindro(radio, altura)
            
            self.volumen_label.config(text=f"Volumen (cm3): {cilindro.get_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {cilindro.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

class VentanaEsfera:
    def __init__(self, root):
        self.root = root
        self.root.title("Esfera")
        self.root.geometry("280x150")
        self.root.resizable(False, False)
        
        self.radio_label = tk.Label(root, text="Radio (cms):")
        self.radio_label.pack()
        
        self.radio_entry = tk.Entry(root)
        self.radio_entry.pack()
        
        self.calcular_btn = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular_btn.pack()
        
        self.volumen_label = tk.Label(root, text="Volumen (cm3):")
        self.volumen_label.pack()
        
        self.superficie_label = tk.Label(root, text="Superficie (cm2):")
        self.superficie_label.pack()
    
    def calcular(self):
        try:
            radio = float(self.radio_entry.get())
            esfera = Esfera(radio)
            self.volumen_label.config(text=f"Volumen (cm3): {esfera.get_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {esfera.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

class VentanaPiramide:
    def __init__(self, root):
        self.root = root
        self.root.title("Pirámide")
        self.root.geometry("280x180")
        self.root.resizable(False, False)
        
        self.base_label = tk.Label(root, text="Base (cms):")
        self.base_label.pack()
        
        self.base_entry = tk.Entry(root)
        self.base_entry.pack()
        
        self.altura_label = tk.Label(root, text="Altura (cms):")
        self.altura_label.pack()
        
        self.altura_entry = tk.Entry(root)
        self.altura_entry.pack()
        
        self.apotema_label = tk.Label(root, text="Apotema (cms):")
        self.apotema_label.pack()
        
        self.apotema_entry = tk.Entry(root)
        self.apotema_entry.pack()
        
        self.calcular_btn = tk.Button(root, text="Calcular", command=self.calcular)
        self.calcular_btn.pack()
        
        self.volumen_label = tk.Label(root, text="Volumen (cm3):")
        self.volumen_label.pack()
        
        self.superficie_label = tk.Label(root, text="Superficie (cm2):")
        self.superficie_label.pack()
    
    def calcular(self):
        try:
            base = float(self.base_entry.get())
            altura = float(self.altura_entry.get())
            apotema = float(self.apotema_entry.get())
            piramide = Piramide(base, altura, apotema)
            
            self.volumen_label.config(text=f"Volumen (cm3): {piramide.get_volumen():.2f}")
            self.superficie_label.config(text=f"Superficie (cm2): {piramide.get_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Campo nulo o error en formato de número")

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Figuras Geométricas")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        
        self.btn_cilindro = tk.Button(root, text="Cilindro", command=self.abrir_cilindro)
        self.btn_cilindro.pack(pady=10)
        
        self.btn_esfera = tk.Button(root, text="Esfera", command=self.abrir_esfera)
        self.btn_esfera.pack(pady=10)
        
        self.btn_piramide = tk.Button(root, text="Pirámide", command=self.abrir_piramide)
        self.btn_piramide.pack(pady=10)
        
    def abrir_cilindro(self):
        ventana = tk.Toplevel(self.root)
        VentanaCilindro(ventana)
    
    def abrir_esfera(self):
        ventana = tk.Toplevel(self.root)
        VentanaEsfera(ventana)
    
    def abrir_piramide(self):
        ventana = tk.Toplevel(self.root)
        VentanaPiramide(ventana)

if __name__ == "__main__":
    root = tk.Tk()
    app = VentanaPrincipal(root)
    root.mainloop()
