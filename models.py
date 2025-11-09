from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, Boolean, Date, JSON
from sqlalchemy.dialects.postgresql import UUID, TSTZRANGE
from sqlalchemy.orm import relationship
import uuid
from .db import Base

class Depot(Base):
    __tablename__ = "depots"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    lat = Column(Numeric(9,6), nullable=False)
    lon = Column(Numeric(9,6), nullable=False)

class ServiceType(Base):
    __tablename__ = "service_types"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    default_service_sec = Column(Integer, nullable=False, default=60)
    constraints_json = Column(JSON)

class Customer(Base):
    __tablename__ = "customers"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    lat = Column(Numeric(9,6), nullable=False)
    lon = Column(Numeric(9,6), nullable=False)
    service_type_id = Column(UUID(as_uuid=True), ForeignKey("service_types.id"))

class Stop(Base):
    __tablename__ = "stops"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    route_date = Column(Date, nullable=False)
    customer_id = Column(UUID(as_uuid=True), ForeignKey("customers.id"))
    service_type_id = Column(UUID(as_uuid=True), ForeignKey("service_types.id"))
    time_window = Column(TSTZRANGE)
    service_time_sec = Column(Integer)  # override
    priority = Column(Integer, default=0)
    is_disposal = Column(Boolean, default=False)
    disposal_site_id = Column(UUID(as_uuid=True))

class Route(Base):
    __tablename__ = "routes"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    route_date = Column(Date, nullable=False)
    total_drive_sec = Column(Integer)
    total_distance_m = Column(Integer)
