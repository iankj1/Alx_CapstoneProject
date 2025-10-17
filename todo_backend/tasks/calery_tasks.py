from celery import shared_task
from django.utils import timezone
from .models import Task
from django.core.mail import send_mail
import os

@shared_task
def process_due_reminders():
    now = timezone.now()
    due_tasks = Task.objects.filter(reminder_time__lte=now, status=Task.STATUS_PENDING)
    results = []
    for t in due_tasks:
        # In production, replace this with actual notification (email, push, SMS)
        subject = f"Reminder: {t.title}"
        body = f"Your task '{t.title}' is due. Description: {t.description or 'No description'}"
        # Send email if user has email and email backend configured
        if t.user.email:
            try:
                send_mail(subject, body, os.getenv("DEFAULT_FROM_EMAIL", "no-reply@example.com"), [t.user.email])
            except Exception:
                # fallback: log to stdout
                print(f"Reminder (email failed) for {t.user.email}: {subject} - {body}")
        else:
            print(f"Reminder for user {t.user.username}: {subject}")

        # clear reminder_time so it doesn't run twice (optionally)
        t.reminder_time = None
        t.save()
        results.append(t.id)
    return {"processed": len(results), "task_ids": results}
