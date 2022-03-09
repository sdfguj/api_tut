
from sqlalchemy import Table, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import null, text
from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key = True, nullable = False)
    user_id = Column(Integer, ForeignKey("users.id", ondelete = "cascade"), nullable = False)
    title = Column(String, nullable = False)
    content = Column(String, nullable = False)
    published = Column(Boolean, server_default = 'TRUE')
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))
    owner = relationship("User")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True, nullable = False)
    email = Column(String, unique = True, nullable = False)
    password = Column(String, nullable = False)
    created_at = Column(TIMESTAMP(timezone=True), nullable = False, server_default = text('now()'))
    phone_number = Column(String)

class Votes(Base):
    __tablename__= "votes"
    user_id = Column(Integer, primary_key = True, nullable = False)
    post_id = Column(Integer, primary_key = True, nullable = False)


