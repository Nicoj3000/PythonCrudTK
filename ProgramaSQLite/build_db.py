import sqlalchemy as db
import dominio.modelos as modelos
import util.generico as gen

nombre_carpetas = "db"

ruta = "./"

gen.crear_carpeta_si_no_existe(ruta, nombre_carpetas)

engine = db.create_engine('sqlite:///db/tienda.sqlite', echo=True, future=True)

modelos.Base.metadata.create_all(engine) 
