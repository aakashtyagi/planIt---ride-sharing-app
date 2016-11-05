from django.core.management.base import BaseCommand
from django.core.mail import EmailMultiAlternatives
from django.conf import settings

class Command(BaseCommand):
    help = "Test Email Settings"

    def handle(self, *args, **options):
        subject, from_email, to = "Plan It Test Email", getattr(settings, 'DEFAULT_FROM_EMAIL'), args[0]
        text_content = "This is a test email from plan it"
        html_content = "This is a test email from <b>plan it</b>"
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()