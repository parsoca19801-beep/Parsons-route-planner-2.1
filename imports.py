from fastapi import APIRouter, UploadFile, File
router = APIRouter()

@router.post("/imports/stops")
async def import_stops(file: UploadFile = File(...)):
    # TODO: parse CSV/Excel and enqueue job
    return {"jobId": "stub"}
