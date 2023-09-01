import uuid
from sqlalchemy import create_engine, Column, String, Date, Boolean, Float
from datetime import date
from app.infra.database import Base


class Usuarios(Base):
    __tablename__ = "usuarios"

    id = Column(String, primary_key=True, index=True, default=str(uuid.uuid4()), unique=True)
    nome = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    password = Column(String)
    data_cadastro = Column(Date, default=date.today())
    data_nascimento = Column(Date)
    ativo = Column(Boolean, default=True)
    comissao = Column(Float)
    tipo = Column(String)