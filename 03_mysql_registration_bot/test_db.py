import config
from db import DB

db = DB(
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    db_name=config.DB_NAME
)

