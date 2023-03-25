from typing import Tuple

from infra.database import ORM_DATABASE
from models.dto import UrlDTO
from models.db import UrlDBModel


class UrlRepository:
    
    @classmethod
    def get_url_by_id(cls, url_id: int) -> UrlDTO:
        
        db_row = UrlDBModel.query.filter_by(url_id=url_id).first()
        if not db_row:
            raise ValueError(f"Not found Url {url_id}")

        return UrlDTO(
            url_id=db_row.url_id,
            title=db_row.title,
            original_url=db_row.original_url,
            short_url=db_row.short_url,
        )
  
    @classmethod
    def insert_new_url(cls, url_data: dict) -> bool:
        
        new_url = UrlDBModel(**url_data)

        try:
            ORM_DATABASE.session.add(new_url)
            ORM_DATABASE.session.commit()
            return True
        except Exception as ex:
            print(ex)
            ORM_DATABASE.session.rollback()
            return False

    @classmethod
    def delete_url_by_id(cls, url_id: int) -> Tuple[UrlDTO, bool]:
        try:
            db_row = UrlDBModel.query.filter_by(url_id=url_id).first()
            if not db_row:
                raise ValueError(f"Not found Url with Id {url_id}")

            deleted_url = UrlDTO(
                url_id=db_row.url_id,
                title=db_row.title,
                original_url=db_row.original_url,
                short_url=db_row.short_url,
            )
            ORM_DATABASE.session.query(UrlDBModel).filter(
                UrlDBModel.url_id == url_id
            ).delete()

            ORM_DATABASE.session.commit()
            return deleted_url, True
        except ValueError:
            raise
        except Exception as ex:
            print(ex)
            ORM_DATABASE.session.rollback()
            return None, False
