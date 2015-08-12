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
        translation = Translation(title)
        db.session.add(translation)
        for line in text.splitlines():
            chunk = Chunk(line, translation.translation_id)
            db.session.add(chunk)
        db.session.commit()
        return translation
