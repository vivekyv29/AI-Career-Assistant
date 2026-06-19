from fastapi import APIRouter

router = APIRouter()

@router.get("/progress")
def get_progress():
    return {
        "progress": [
            {
                "skill": "Python",
                "status": "Completed"
            }
        ]
    }