from sqlalchemy.orm import Session
from .. import models, schemas

# Criar ItensLote


def criar_ItensLote(db: Session, ItensLote: schemas.ItensLoteCreate):
    db_ItensLote = models.ItensLote(**ItensLote.dict())
    db.add(db_ItensLote)
    db.commit()
    db.refresh(db_ItensLote)
    return db_ItensLote

# Listar todos


def listar_ItensLote(db: Session):
    return db.query(models.ItensLote).all()

# Buscar por ID


def buscar_ItensLote(db: Session, ItensLote_id: int):
    return db.query(models.ItensLote).filter(models.ItensLote.id_ItensLote == ItensLote_id).first()

# Atualizar


def atualizar_ItensLote(db: Session, ItensLote_id: int, ItensLote_update: schemas.ItensLoteUpdate):
    db_ItensLote = buscar_ItensLote(db, ItensLote_id)
    if not db_ItensLote:
        return None
    for key, value in ItensLote_update.dict(exclude_unset=True).items():
        setattr(db_ItensLote, key, value)
    db.commit()
    db.refresh(db_ItensLote)
    return db_ItensLote

# Remover


def remover_ItensLote(db: Session, ItensLote_id: int):
    db_ItensLote = buscar_ItensLote(db, ItensLote_id)
    if db_ItensLote:
        db.delete(db_ItensLote)
        db.commit()
        return True
    return False
