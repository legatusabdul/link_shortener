from infra.database import ORM_DATABASE as db


class UrlDBModel(db.Model):
    __tablename__ = "Url"
    
    url_id: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(150), nullable=False)    
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(50), nullable=True)

    def __init__(
        self,
        title: str,
        original_url: str,
        short_url: str,
    ) -> None:
        self.title=str(title)
        self.original_url=str(original_url)
        self.short_url=str(short_url)
