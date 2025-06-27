from sqlalchemy.orm import Session
from app.domain.models import WorkShop
from app.infraestructure.entities.workshop_entity import WorkShopEntity
from app.domain.ports.output.workshop_repository_port import WorkShopRepositoryPort

class WorkShopRepositoryImpl(WorkShopRepositoryPort):
    def __init__(self, db: Session):
        self.db = db

    def find_by_email(self, email: str) -> WorkShop | None:
        workshop_row = self.db.query(WorkShopEntity).filter(WorkShopEntity.email == email).first()
        if workshop_row:
            return WorkShop(
                id= workshop_row.id,
                email= workshop_row.email,
                password= workshop_row.password,
                activated=workshop_row.activated,
                created_at=workshop_row.created_at,
                updated_at=workshop_row.updated_at
            )
        return None