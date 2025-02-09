# database/models.py
from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

engine = create_engine('sqlite:///hospital.db')
metadata = MetaData()

Physicians = Table(
    'Physicians', metadata,
    Column('Name', String),
    Column('Speciality', String),
    Column('Degree', String)
)

Schedules = Table(
    'Schedules', metadata,
    Column('Doctor Name', String),
    Column('Monday', String),
    Column('Tuesday', String),
    Column('Wednesday', String),
    Column('Thursday', String),
    Column('Friday', String),
    Column('Saturday', String),
    Column('Sunday', String)
)

Specialities = Table(
    'Specialities', metadata,
    Column('Speciality Name', String),
    Column('Definition', String)
)

Pricelist = Table(
    'Pricelist', metadata,
    Column('Service Name', String),
    Column('Price (USD)', String)
)

Policy = Table(
    'Policy', metadata,
    Column('Name', String),
    Column('Policy Description', String),
    Column('Address', String),
    Column('Landline', String),
    Column('Open Date', String)
)

metadata.create_all(engine)