from sqlalchemy import Column
from sqlalchemy import String, Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ProductoModel (Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150))
    cargo = Column(String(150))
    salario = Column(Integer)

    def __repr__(self):
        return f'Producto(id={self.id}, nombre={self.nombre}, cargo={self.cargo}, salario={self.salario})'
    
    def __str__(self):
        return f'Producto(id={self.id}, nombre={self.nombre}, cargo={self.cargo}, salario={self.salario})'