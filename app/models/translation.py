from datetime import datetime

from app import db
from app.models.chunk import Chunk


class Translation(db.Model):
    """
    Translation is whole text requested by user for translation.
    """

    translation_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    created_ts = db.Column(db.DateTime, default=datetime.utcnow)

    @classmethod
    def create(cls, title, text):
        translation = Translation(title=title)
        db.session.add(translation)
        for line in text.splitlines():
            chunk = Chunk(text=line, translation_id=translation.translation_id)
            db.session.add(chunk)
        db.session.commit()
        return translation

    @staticmethod
    def get(translation_id):
        return Translation.query.get(translation_id)

    @staticmethod
    def get_all():
        return Translation.query.all()

    def update(self, title):
        translation = Translation.get(self.translation_id)
        translation.title = title
        db.session.commit()

    def delete(self):
        translation = Translation.get(self.translation_id)
        db.session.delete(translation)
        db.session.commit()
