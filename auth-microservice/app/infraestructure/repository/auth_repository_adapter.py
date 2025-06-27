

from abc import ABCMeta, abstractmethod
from app.domain.ports.output.auth_repository_port import AuthRepositoryPort
from entities.workshop_entity import WorkShopEntity
from domain.models import WorkShop
from conection_db import get_db
from sqlalchemy.orm import Session


class AuthRepositoryAdapter(AuthRepositoryPort):

    def __init__(self, db: Session):
        self.db = db
    
    def login(self, email:str, password:str) -> WorkShop:
        user_row = self.db.query(WorkShopEntity).filter(WorkShopEntity.email == email, ).first()
        if user_row:
            return WorkShop(
                id=user_row.id,
                email=user_row.email,
                password=user_row.password,
                activated=user_row.activated,
                created_at=user_row.created_at,
                updated_at=user_row.updated_at
            )
        return None