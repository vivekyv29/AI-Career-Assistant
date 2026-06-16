from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class RoadmapRequest(BaseModel):
    role: str

@router.post("/roadmap")
def roadmap(request: RoadmapRequest):

    if request.role == "AI Engineer":

        return {
            "roadmap": [
                "Learn Python",
                "Learn Machine Learning",
                "Learn Deep Learning",
                "Learn TensorFlow",
                "Learn PyTorch",
                "Learn Docker",
                "Learn AWS",
                "Build Projects",
                "Prepare Interviews",
                "Apply For Jobs"
            ]
        }

    return {
        "roadmap": [
            "No roadmap available"
        ]
    }