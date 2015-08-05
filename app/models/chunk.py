from app import db


class Chunk(db.Model):
    """
    Chunk is a minimal item to translate.  Translation
    consists of multiple chunks.
    """
    __tablename__ = 'chunk'

    chunk_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    translation_id = db.Column(db.Integer,
                               db.ForeignKey('translation.translation_id'))

    def __init__(self, text, translation_id):
        self.text = text
        self.translation_id = translation_id
