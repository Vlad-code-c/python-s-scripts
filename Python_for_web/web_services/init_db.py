from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db import Base, TodoItem

engine = create_engine("sqlite:///tasks.db", echo=True) 
Base.metadata.create_all(engine)

Sesion = sessionmaker(bind=engine)
s = Sesion()

for desc in ("read book", "learn python", "wash footwear", "eat"):
    t = TodoItem(desc)
    s.add(t)

s.commit()