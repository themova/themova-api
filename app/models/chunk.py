from app.extensions import db


class Chunk(db.Model):
    """
    Chunk is a minimal item to translate.  Translation
    consists of multiple chunks.
    """

    chunk_id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    translation_id = db.Column(db.Integer,
                               db.ForeignKey('translation.translation_id'))
