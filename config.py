import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
DATABASE_CONNECT_OPTIONS = {}

SECRET_KEY = "9oup7z6mdbw)9(f6$9ob@m&xha*(6ulqot&x*y1n$2^^9qo#d-"
