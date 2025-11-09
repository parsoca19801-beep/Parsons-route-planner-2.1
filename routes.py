from fastapi import APIRouter
from ..schemas import RouteOptimizeRequest, RouteOut

router = APIRouter()

@router.post("/optimize", response_model=dict)
async def optimize(req: RouteOptimizeRequest):
    # TODO: enqueue Celery task build_matrices -> solve_route
    return {"routeId": "stub"}

@router.get("/routes/{route_id}", response_model=RouteOut)
async def get_route(route_id: str):
    # TODO: fetch from DB; include leg metrics and totals
    return {"routeId": route_id, "stops": []}

@router.get("/routes/{route_id}/preview")
async def get_route_preview(route_id: str):
    # TODO: call provider to build polyline + steps
    return {"routeId": route_id, "polyline": "ENCODED_POLYLINE_STUB", "steps": []}
