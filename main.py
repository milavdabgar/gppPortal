from app import create_app
from app.worker import celery_init_app
from celery.schedules import crontab
from app.tasks import daily_reminder

app = create_app()
celery_app = celery_init_app(app)


@celery_app.on_after_configure.connect
def send_email(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=19, minute=55, day_of_month=20),
        daily_reminder.s("milav.dabgar@gmail.com", "Daily Test"),
    )


if __name__ == "__main__":
    app.run(debug=True)
