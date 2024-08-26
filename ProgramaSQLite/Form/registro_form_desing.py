## Diseño de la ventana de registro de productos
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import util.util_ventana as util_ventana
## Configuración de colores
color_fondo = "#fff"
color_fondo_busqueda = "#f7f8fa"
## Clase que contiene el diseño de la ventana de registro de productos
class FormularioRegistroDesing(tk.Tk):
    def __init__(self):
        super().__init__()
        self.config_Window()
        self.crear_paneles()
        self.crear_controles()
## Configuración de la ventana        
    def config_Window(self):
        self.title("Python CRUD")
        w, h = 800, 500
        util_ventana.centrar_ventana(self, w, h)
        self .config(bg=color_fondo_busqueda)
## Creación de los paneles
    def crear_paneles(self):
        self.marco_titulo = tk.Frame(self, bg=color_fondo_busqueda, height=40)
        self.marco_titulo.pack(side=tk.TOP,fill='both')

        self.marco_registro = tk.Frame(self, bg=color_fondo, height=50)
        self.marco_registro.pack(side=tk.TOP,fill='both', pady=10)

        self.marco_acciones = tk.Frame(self, bg=color_fondo, height=50)
        self.marco_acciones.pack(side=tk.TOP,fill='both')

        self.marco_productos = tk.Frame(self, bg=color_fondo)
        self.marco_productos.pack(side=tk.TOP,fill='both', padx=30, pady=15, expand=True)
## Creación de los controles
    def crear_controles(self):
        ## Creación de los controles de la ventana
        title = tk.Label(self.marco_titulo, text="Registro de Productos",font=
                         ("Times", 24), fg="#485159", bg=color_fondo, pady=20)
        title.pack(expand=True, fill= tk.BOTH)
        ## Creación de los controles del formulario
        etiqueta_nombre = tk.Label(self.marco_registro, text="Nombre", font=
                               ("Times", 14),fg="#666a88", bg=color_fondo)
        etiqueta_nombre.pack(side=tk.LEFT, padx=5, pady=10)

        self.campo_nombre = ttk.Entry(self.marco_registro, font=
                                  ("Times", 14))
        self.campo_nombre.pack(side=tk.LEFT, padx=5, pady=10)

        etiqueta_salario = tk.Label(self.marco_registro, text="Salario", font=
                                   ("Times", 14),fg="#666a88", bg=color_fondo)
        etiqueta_salario.pack(side=tk.LEFT, padx=5, pady=10)

        self.campo_salario = ttk.Entry(self.marco_registro, font=
                                      ("Times", 14))
        self.campo_salario.pack(side=tk.LEFT, padx=5, pady=10)

        etiqueta_cargo = tk.Label(self.marco_registro, text="Cargo", font=
                                   ("Times", 14),fg="#666a88", bg=color_fondo)
        etiqueta_cargo.pack(side=tk.LEFT, padx=5, pady=10)

        self.campo_cargo = ttk.Entry(self.marco_registro, font=
                                      ("Times", 14))
        self.campo_cargo.pack(side=tk.LEFT, padx=5, pady=10)

        etiqueta_compra = tk.Label(self.marco_registro, text="Compra", font=
                                   ("Times", 14),fg="#666a88", bg=color_fondo)
        etiqueta_compra.pack(side=tk.LEFT, padx=5, pady=10)

        self.campo_compra = ttk.Entry(self.marco_registro, font=
                                        ("Times", 14))
        self.campo_compra.pack(side=tk.LEFT, padx=5, pady=10)

        etiqueta_venta = tk.Label(self.marco_registro, text="Venta", font=
                                      ("Times", 14),fg="#666a88", bg=color_fondo)
        etiqueta_venta.pack(side=tk.LEFT, padx=5, pady=10)

        self.campo_venta = ttk.Entry(self.marco_registro, font=
                                        ("Times", 14))
        self.campo_venta.pack(side=tk.LEFT, padx=5, pady=10)

        etiqueta_gerencia = tk.Label(self.marco_registro, text="Gerencia", font=
                                      ("Times", 14),fg="#666a88", bg=color_fondo)
        etiqueta_gerencia.pack(side=tk.LEFT, padx=5, pady=10)

        self.campo_gerencia = ttk.Entry(self.marco_registro, font=
                                        ("Times", 14))
        self.campo_gerencia.pack(side=tk.LEFT, padx=5, pady=10)
        
        ## Creación de los botones de la ventana
        self.btn_registro = tk.Button(self.marco_acciones, text="Registrar",
                                     font=("Times", 14), fg="#fff", bg="#51aded", bd=0,padx=15, command=self.registrar_producto) 
        self.btn_registro.pack(**self.obtener_conf_btn_pack())
        self.btn_registro.bind(
            "<Return>", (lambda event: self.registrar_producto()))
        
        self.btn_eliminar = tk.Button(self.marco_acciones, text="Eliminar",
                                     font=("Times", 14), fg="#fff", bg="#ed5153", bd=0,padx=15, command=self.eliminar_producto)
        self.btn_eliminar.pack(**self.obtener_conf_btn_pack())  
        self.btn_eliminar.bind(
            "<Return>", (lambda event: self.eliminar_producto()))
        self.btn_eliminar.pack_forget()

        self.btn_modificar = tk.Button(self.marco_acciones, text="Modificar",
                                     font=("Times", 14), fg="#fff", bg="#f0b429", bd=0,padx=15, command=self.modificar_producto)
        self.btn_modificar.pack(**self.obtener_conf_btn_pack())
        self.btn_modificar.bind(
            "<Return>", (lambda event: self.modificar_producto()))
        self.btn_modificar.pack_forget()

        self.btn_limpiar = tk.Button(self.marco_acciones, text="Limpiar Campos", 
                                    font=("Times", 14), fg="#fff", bg="#e39531", bd=0,padx=15, command=self.limpiar_campos)
        self.btn_limpiar.pack(**self.obtener_conf_btn_pack())
        self.btn_limpiar.bind(
            "<Return>", (lambda event: self.limpiar_campos()))
        
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Treeview',
                        background = '#eafbea',
                        foreground='#000')
        style.configure('Treeview.Heading', background='#6f9a8d', foreground='#fff')

        tree_scroll = ttk.Scrollbar(self.marco_productos, orient=tk.VERTICAL)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        tree_scroll_x = ttk.Scrollbar(self.marco_productos, orient=tk.HORIZONTAL)
        tree_scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        self.tree = ttk.Treeview(self.marco_productos, show='headings',
                                 yscrollcommand=tree_scroll.set)
        self.tree['columns'] = ("Id", "Nombre", "Cargo", "Salario", "compra", "venta", "gerencia")
        self.tree.column('#0')
        self.tree.column('Id', width=10)
        self.tree.column('Nombre')
        self.tree.column('Cargo')
        self.tree.column('Salario')
        self.tree.column('compra')
        self.tree.column('venta')
        self.tree.column('gerencia')
        

        self.tree.heading('#0', text='')
        self.tree.heading('Id', text='Id')
        self.tree.heading('Nombre', text='Nombre')
        self.tree.heading('Cargo', text='Cargo')
        self.tree.heading('Salario', text='Salario')
        self.tree.heading('compra', text='Compra')
        self.tree.heading('venta', text='Venta')
        self.tree.heading('gerencia', text='Gerencia')
        

        self.tree.pack(expand=True, fill='both')
        self.tree.bind("<<TreeviewSelect>>", self.al_seleccionar_treeview)

        self.tree.tag_configure('oddrow', background='#ffffe0')
        self.tree.tag_configure('evenrow', background='#eafbea')

        self.actualizar_lista()
        
    ## Métodos de la clase

    def actualizar_lista(self):
        pass

    def registrar_producto(self):
        pass
        
    def eliminar_producto(self):
        pass
    
    def modificar_producto(self):
        pass

    def al_seleccionar_treeview(self, event):
        pass

    def limpiar_campos(self):
        
        try:
            self.campo_nombre.delete(0, 'end')
            self.campo_salario.delete(0, 'end')
            self.campo_cargo.delete(0, 'end')
            self.campo_compra.delete(0, 'end')
            self.campo_venta.delete(0, 'end')
            self.campo_gerencia.delete(0, 'end')
            self.btn_registro.pack(**self.obtener_conf_btn_pack())
            self.btn_eliminar.pack_forget()
            self.btn_modificar.pack_forget()
        except Exception as e:
            messagebox.showerror("Error", f"Error al limpiar campos: {e}")


    def obtener_conf_btn_pack(self):
        return {"side": tk.RIGHT, "padx": 10, "pady": 10}