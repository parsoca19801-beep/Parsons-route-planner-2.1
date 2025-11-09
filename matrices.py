from ..worker import app

@app.task
def build_matrices(route_id: str) -> dict:
    # TODO: call HERE Matrix for time buckets and cache results
    return {"route_id": route_id, "status": "matrices_built"}
