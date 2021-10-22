from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    renters = relationship("Renters", back_populates="owner")


class Renters(Base):
    __tablename__ = "renters"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    phone = Column(String)
    e_mail = Column(String)
    activity_kind_id = Column(Integer, ForeignKey("activity_kinds.id"))
    activity = relationship("Activity_kinds", back_populates="who")
    demanded_addr_id = Column(Integer, ForeignKey("addresses.id"))
    demanded_addr = relationship("Addresses", back_populates="interested_addr") 
    meters_required = Column(Integer)
    comments = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="renters")


class Activity_kinds(Base):
    __tablename__ = "activity_kinds"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    who = relationship("Renters", back_populates="activity")


class Addresses(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    interested_addr = relationship("Renters", back_populates="demanded_addr")
