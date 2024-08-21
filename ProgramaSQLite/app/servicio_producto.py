import sqlalchemy as db
from sqlalchemy.orm import Session
from dominio.modelos import ProductoModel, DepartamentoModel
from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound
from typing import List, Tuple


class ServicioProducto():
    def __init__(self):
        self.engine = db.create_engine('sqlite:///db/tienda.sqlite', echo=True, future=True) 

    def register(self, nombre, cargo, salario, compra, venta, gerencia):
        producto = ProductoModel()
        producto.nombre = nombre
        producto.cargo = cargo
        producto.salario = salario
        
        departamento = DepartamentoModel()
        departamento.compra = compra
        departamento.venta = venta
        departamento.gerencia = gerencia
        
        with Session(self.engine) as session:
            session.add(producto)
            session.add(departamento)
            try:
                session.commit()
            except IntegrityError as e:
                session.rollback()
                raise e
    
    def modify(self, id, nombre, cargo, salario, compra, venta, gerencia):
        with Session(self.engine) as session:
            try:
            # Actualizar la tabla ProductoModel
                producto = session.query(ProductoModel).filter_by(id=id).first()
                if producto:
                    producto.nombre = nombre
                    producto.cargo = cargo
                    producto.salario = salario
            
            # Actualizar la tabla DepartamentoModel
                departamentos = session.query(DepartamentoModel).filter(DepartamentoModel.productos.contains(producto)).first()
                if departamentos:
                    departamentos.compra = compra
                    departamentos.venta = venta
                    departamentos.gerencia = gerencia
            
            # Confirmar los cambios
                session.commit()
                print("Producto modificado correctamente.")
            except Exception as e:
                session.rollback()
                print(f"Error al modificar el producto: {e}")
                raise
 
    def obtener_productos(self) -> List[dict]:
        with Session(self.engine) as session:
            resultados = session.query(
                ProductoModel.id,
                ProductoModel.nombre,
                ProductoModel.cargo,
                ProductoModel.salario,
                DepartamentoModel.compra,
                DepartamentoModel.venta,
                DepartamentoModel.gerencia
            ).join(DepartamentoModel, ProductoModel.id == DepartamentoModel.id).all()
            
            productos_combinados = [
                {
                    'id': resultado.id,
                    'nombre': resultado.nombre,
                    'cargo': resultado.cargo,
                    'salario': resultado.salario,
                    'compra': resultado.compra,
                    'venta': resultado.venta,
                    'gerencia': resultado.gerencia
                }
                for resultado in resultados
            ]
            
        return productos_combinados

    def eliminar(self, id):
        with Session(self.engine) as session:
            try:
                # Eliminar el departamento asociado
                departamento = session.query(DepartamentoModel).filter_by(producto_id=id).one_or_none()
                if departamento:
                    session.delete(departamento)
                
                # Eliminar el producto
                producto = session.query(ProductoModel).filter_by(id=id).one()
                session.delete(producto)
                
                # Confirmar los cambios
                session.commit()
                print("Producto eliminado correctamente.")
            except Exception as e:
                session.rollback()
                print(f"Error al eliminar el producto: {e}")
                raise