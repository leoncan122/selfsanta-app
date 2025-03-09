from fastapi import APIRouter

router = APIRouter()

router.get("/system/{portal_id}")
def access_portal(portal_id: str):
    return {'message': f"Accessing portal {portal_id}"}