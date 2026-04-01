from fastapi import APIRouter
from src.controllers import event

router = APIRouter(prefix="/events", tags=["Events"])


router.get("/")(event.get_events)
router.get("/{event_id}")(event.get_event)
router.post("/")(event.create_event)
router.put("/{event_id}")(event.update_event)
router.delete("/{event_id}")(event.delete_event)