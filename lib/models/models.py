
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

# table for many-to-many relationship between Trip and Passenger
trip_passenger = Table('trip_passenger', Base.metadata,
    Column('trip_id', Integer, ForeignKey('trips.id')),
    Column('passenger_id', Integer, ForeignKey('passengers.id'))
)

class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    make = Column(String(50), nullable=False)
    model = Column(String(50), nullable=False)
    year = Column(Integer, nullable=False)
    driver_id = Column(Integer, ForeignKey('drivers.id'))
    
    driver = relationship("Driver", back_populates="vehicle")
    trips = relationship("Trip", back_populates="vehicle")

class Driver(Base):
    __tablename__ = 'drivers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    license_number = Column(String(20), unique=True, nullable=False)
    
    vehicle = relationship("Vehicle", back_populates="driver", uselist=False)
    trips = relationship("Trip", back_populates="driver")

class Route(Base):
    __tablename__ = 'routes'
    id = Column(Integer, primary_key=True)
    start_location = Column(String(100), nullable=False)
    end_location = Column(String(100), nullable=False)
    distance_km = Column(Integer, nullable=False)
    estimated_duration_min = Column(Integer, nullable=False)
    
    trips = relationship("Trip", back_populates="route")

class Passenger(Base):
    __tablename__ = 'passengers'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    contact_info = Column(String(50))

    trips = relationship("Trip", secondary=trip_passenger, back_populates="passengers")

class Trip(Base):
    __tablename__ = 'trips'
    id = Column(Integer, primary_key=True)
    driver_id = Column(Integer, ForeignKey('drivers.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    route_id = Column(Integer, ForeignKey('routes.id'))
    scheduled_time = Column(DateTime)

    driver = relationship("Driver", back_populates="trips")
    vehicle = relationship("Vehicle", back_populates="trips")
    route = relationship("Route", back_populates="trips")
    passengers = relationship("Passenger", secondary=trip_passenger, back_populates="trips")
