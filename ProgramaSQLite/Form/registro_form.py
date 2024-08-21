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
        compra = self.campo_compra.get()
        venta = self.campo_venta.get()
        gerencia = self.campo_gerencia.get()
        if not nombre or not salario or not cargo or not compra or not venta or not gerencia:
            messagebox.showerror('Error', 'Todos los campos son requeridos')
            return
            
        try:
            salario = float(salario)
            venta = float(venta)
        except ValueError:
            messagebox.showerror(
                'Error', 'El salario debe ser un número')
            return
        
        try:
            self.servicio_producto.register(nombre, salario, cargo, compra, venta, gerencia)
            messagebox.showinfo('Exito', ' Registrado correctamente')
            self.actualizar_lista()
            self.limpiar_campos()

        except Exception as e:
            messagebox.showerror('Error', f"No se pudo registrar el producto: {e}")

    def actualizar_lista(self):
        try:
        # Eliminar todos los registros actuales en el treeview
            registros = self.tree.get_children()
            for registro in registros:
                self.tree.delete(registro)
        
        # Obtener productos desde el servicio
            productos = self.servicio_producto.obtener_productos()
        
        # Verificar que productos no esté vacío
            if not productos:
                print("No se encontraron productos.")
                return
        
        # Insertar productos en el treeview
            for ref, producto in enumerate(productos):
                color = ('evenrow',) if ref % 2 else ('oddrow',)
                self.tree.insert(parent='', index=ref, iid=ref, text='', tags=color,
                             values=(producto['id'], producto['nombre'], producto['salario'], producto['cargo'], producto['compra'], producto['venta'], producto['gerencia']))
            print("Lista actualizada correctamente.")
        except Exception as e:
            print(f"Error al actualizar la lista: {e}")
            messagebox.showerror('Error', f'No se pudo actualizar la lista: {e}')

    def al_seleccionar_treeview(self, event):
        seleccion = event.widget.selection()
        if seleccion:
            item = event.widget.item(seleccion[0], 'values')
            if item:
                self.limpiar_campos()
                self.campo_nombre.insert(0, item[1])
                self.campo_cargo.insert(0, item[2])
                self.campo_salario.insert(0, item[3])
                self.campo_compra.insert(0, item[4])
                self.campo_venta.insert(0, item[5])
                self.campo_gerencia.insert(0, item[6])

                self.btn_eliminar.pack(**self.obtener_conf_btn_pack())
                self.btn_modificar.pack(**self.obtener_conf_btn_pack())
                self.btn_registro.pack_forget()

    def modificar_producto(self):
        try:
        # Obtener el ID del producto seleccionado
            id = self.tree.item(self.tree.selection())['values'][0]
        
        # Obtener los valores de los campos de entrada
            nombre = self.campo_nombre.get()
            salario = self.campo_salario.get()
            compra = self.campo_compra.get()
            venta = self.campo_venta.get()
            gerencia = self.campo_gerencia.get()
        
        # Convertir los valores a tipos adecuados
            try:
                venta = float(venta)
                salario = float(salario)
            except ValueError:
                messagebox.showerror('Error', 'El salario y la venta deben ser números')
                return
        
            cargo = self.campo_cargo.get()
        
        # Llamar a la función modify del servicio para actualizar las tablas relacionadas
            self.servicio_producto.modify(id, nombre, salario, cargo, compra, venta, gerencia)
        
        # Limpiar los campos de entrada
            self.limpiar_campos()
        
        # Actualizar la lista de productos
            self.actualizar_lista()
        
        except IndexError as e:
            messagebox.showerror('Error', f'Por favor seleccione un registro: {e}')
    def eliminar_producto(self):
        try:
            id = self.tree.item(self.tree.selection())['values'][0]
            self.servicio_producto.eliminar(id)
            self.limpiar_campos()
            self.actualizar_lista()
        except IndexError as e:
            messagebox.showerror('Error', 'Por favor seleccione un registro.')
        except Exception as e:
            messagebox.showerror('Error', f'Error al eliminar el producto: {e}')

    