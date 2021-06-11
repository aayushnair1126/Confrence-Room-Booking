from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .models import Slot 
import pytz
from django.utils import timezone
utc=pytz.UTC

def job():
    slots = Slot.objects.all()
    now = timezone.now()
    for slot in slots:
        if slot.end_time <= now:
            slot.is_available = True
            slot.booked_by = None
            slot.save()


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', seconds=10)
    scheduler.start()