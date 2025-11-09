from ..worker import app

@app.task
def solve_route(route_id: str) -> dict:
    # TODO: OR-Tools VRP/VRPTW using cached matrices
    return {"route_id": route_id, "status": "optimized"}
