from tkinter import messagebox
from app.servicio_producto import ServicioProducto
from Form.registro_form_desing import FormularioRegistroDesing

class FormularioRegistro(FormularioRegistroDesing):
    def __init__(self):
        self.servicio_producto = ServicioProducto()
        super().__init__()
    
    def registrar_producto(self):
        nombre = self.campo_nombre.get()
        salario = self.campo_salario.get()
        cargo = self.campo_cargo.get()
        if not nombre or not salario or not cargo:
            messagebox.showerror('Error', 'Todos los campos son requeridos')
            return
            
        try:
            salario = float(salario)
        except ValueError:
            messagebox.showerror(
                'Error', 'El salario debe ser un número')
            return
        
        try:
            self.servicio_producto.register(nombre, salario, cargo)
            messagebox.showinfo('Exito', ' Registrado correctamente')
            self.actualizar_lista()
            self.limpiar_campos()

        except Exception as e:
            messagebox.showerror('Error', f"No se pudo registrar el producto: {e}")

    def actualizar_lista(self):
        registros = self.tree.get_children()
        for registro in registros:
            self.tree.delete(registro)
        productos = self.servicio_producto.obtener_productos()
        for ref, producto in enumerate(productos):
            color = ('evenrow',) if ref % 2 else ('oddrow',)
            self.tree.insert(parent='', index=ref, iid=ref, text='', tags=color,
                             values=(producto.id ,producto.nombre, producto.salario, producto.cargo))
    
    def al_seleccionar_treeview(self, event):
        seleccion = event.widget.selection()
        if seleccion:
            item = event.widget.item(seleccion[0], 'values')
            if item:
                self.limpiar_campos()
                self.campo_nombre.insert(0, item[1])
                self.campo_cargo.insert(0, item[2])
                self.campo_salario.insert(0, item[3])
                self.btn_eliminar.pack(**self.obtener_conf_btn_pack())
                self.btn_modificar.pack(**self.obtener_conf_btn_pack())
                self.btn_registro.pack_forget()

    def modificar_producto(self):
        try:
            id = self.tree.item(self.tree.selection())['values'][0]
            nombre = self.campo_nombre.get()
            salario = self.campo_salario.get()
            try:
                salario = float(salario)
            except ValueError:
                messagebox.showerror(
                    'Error', 'El salario debe ser un número')
                return
            cargo = self.campo_cargo.get()
            self.servicio_producto.modify(nombre, salario, cargo, id)
            self.limpiar_campos()
            self.actualizar_lista()

        except IndexError as e:
            messagebox.showerror('Error', f'Por favor Seleccione un registro: {e}')

    def eliminar_producto(self):
        try:
            id = self.tree.item(self.tree.selection())['values'][0]
            self.servicio_producto.eliminar(id)
            self.limpiar_campos()
            self.actualizar_lista()
        except IndexError as e:
            messagebox.showerror('Error', f'Por favor Seleccione un registro: {e}')

        

    