from abc import abstractmethod
from abc import ABC, ABCMeta
from app.domain.models import WorkShop

class WorkShopRepositoryPort(metaclass=ABCMeta):
    
    @abstractmethod
    def find_by_email(self, email:str) -> WorkShop:
        pass