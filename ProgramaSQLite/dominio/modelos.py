from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class ProductoModel(Base):
    __tablename__ = 'productos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(150))
    cargo = Column(String(150))
    salario = Column(Integer)
    departamento_id = Column(Integer, ForeignKey('departamentos.id'))

    departamento = relationship("DepartamentoModel", back_populates="productos")

    def __repr__(self):
        return f'Producto(id={self.id}, nombre={self.nombre}, cargo={self.cargo}, salario={self.salario}, departamento={self.departamento})'
    
    def __str__(self):
        return f'Producto(id={self.id}, nombre={self.nombre}, cargo={self.cargo}, salario={self.salario}, departamento={self.departamento})'

class DepartamentoModel(Base):
    __tablename__ = 'departamentos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    compra = Column(String(150))
    venta = Column(String(150))
    gerencia = Column(String(150))

    productos = relationship("ProductoModel", back_populates="departamento")

    def __repr__(self):
        return f'Departamento(id={self.id}, compra={self.compra}, venta={self.venta}, gerencia={self.gerencia})'
    
    def __str__(self):
        return f'Departamento(id={self.id}, compra={self.compra}, venta={self.venta}, gerencia={self.gerencia})'