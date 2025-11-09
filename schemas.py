from pydantic import BaseModel
from typing import Optional, List
from datetime import date, datetime

class StopIn(BaseModel):
    customer_id: str
    route_date: date
    service_type_id: str
    service_time_sec: Optional[int] = None
    time_window_start: Optional[datetime] = None
    time_window_end: Optional[datetime] = None
    is_disposal: bool = False
    disposal_site_id: Optional[str] = None

class RouteOptimizeRequest(BaseModel):
    routeDate: date
    vehicleId: str
    archetype: str
    options: dict | None = None

class LegMetrics(BaseModel):
    leg_distance_m: int
    leg_drive_sec: int

class RouteStopOut(BaseModel):
    stop_id: str
    seq: int
    eta_ts: Optional[datetime] = None
    metrics: Optional[LegMetrics] = None

class RouteOut(BaseModel):
    routeId: str
    stops: List[RouteStopOut] = []
    total_distance_m: Optional[int] = None
    total_drive_sec: Optional[int] = None
