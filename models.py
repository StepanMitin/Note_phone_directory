from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///phones.sqlite', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phones = relationship("Phone", back_populates="user")
    job_places = relationship("JobPlace", back_populates="user")

    def __str__(self):
        return self.name
    
    @classmethod
    def add(cls, name): 
        user = cls(name=name)
        session.add(user)
        session.commit()
        return user
    
    @classmethod
    def all(cls): 
        return session.query(cls).all()

class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="phones")

    def __str__(self):
        return self.phone

    @classmethod
    def add(cls, phone, user):
        phone = cls(phone=phone, user=user)
        session.add(phone)
        session.commit()
        return phone

class JobPlace(Base):
    __tablename__ = 'job_places'
    id = Column(Integer, primary_key=True)
    job_place = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="job_places")

    def __str__(self):
        return self.job_place

    @classmethod
    def add(cls, job_place, user):
        job_place = cls(job_place=job_place, user=user)
        session.add(job_place)
        session.commit()
        return job_place

Base.metadata.create_all(engine)