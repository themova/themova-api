from datetime import datetime

from app import db

from app.models.chunk import Chunk


class Translation(db.Model):
    """
    Translation is whole text requested by user for translation.
    """
    __tablename__ = 'translation'

    translation_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    created_ts = db.Column(db.DateTime)

    def __init__(self, title, created_ts=None):
        self.title = title
        if created_ts is None:
            self.created_ts = datetime.now()
        else:
            self.created_ts = created_ts

    @classmethod
    def create(cls, title, text):
        translation = Translation(title)
        db.session.add(translation)
        for line in text.splitlines():
            chunk = Chunk(line, translation.translation_id)
            db.session.add(chunk)
        db.session.commit()
        return translation
