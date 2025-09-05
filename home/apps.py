from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from django.utils import timezone



class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        def activate_quiz():
            from home.models import Quiz
            current_time = timezone.now()
            events = Quiz.objects.filter(start_time__lte=current_time, is_active=False)
            for event in events:
                event.is_active = True
                event.save()

        scheduler = BackgroundScheduler()
        scheduler.add_job(activate_quiz, 'interval', seconds=10)
        scheduler.start()
