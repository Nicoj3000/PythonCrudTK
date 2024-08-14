import sqlalchemy as db
from sqlalchemy.orm import Session
from dominio.modelos import ProductoModel
from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

class ServicioProducto():
    def __init__(self):
        self.engine = db.create_engine('sqlite:///db/tienda.sqlite', echo=True, future=True) 
    def register(self, nombre, cargo, salario):
        producto = ProductoModel()
        producto.nombre = nombre
        producto.cargo = cargo
        producto.salario = salario
        with Session(self.engine) as session:
            session.add(producto)
            try:
                session.commit()
            except IntegrityError as e:
                session.rollback()
                raise e
    
    def modify(self, nombre, cargo, salario, producto_id):
        try:
            with Session(self.engine) as session:
                producto = session.query(ProductoModel).filter_by(id=producto_id).one()
                producto.nombre = nombre
                producto.cargo = cargo
                producto.salario = salario
                session.commit()
                print(f"Producto modificado correctamente con el id: {producto_id}")
        
        except NoResultFound :
            print(f"No se encontró el producto con id: {producto_id}")
            return False
        except Exception as e:
            print(f"Error al modificar el producto: {e}")
            return False
 
    def obtener_productos(self) -> List[ProductoModel]:
        productos: ProductoModel = None
        with Session(self.engine) as session:
            productos = session.query(ProductoModel).all()
        return productos   

    def eliminar(self, id):
        with Session(self.engine) as session:
            producto = session.query(ProductoModel).filter_by(id=id).one()
            if producto:
                try:
                    session.delete(producto)
                    session.commit()
                    print("Producto eliminado")
                except IntegrityError as e:
                    session.rollback()
                    print("Error al eliminar")
            else:
                print("Producto no encontrado")
                