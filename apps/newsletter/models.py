from django.db import models
from django.conf import settings
from django.core.mail import EmailMultiAlternatives



class Subscriber(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Subscribers"
        verbose_name = "Subscriber"
    
    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"



class Newletter(models.Model):
    DRAFT = "Draft"
    SENT = "Sent"
    
    LETTER_STATUS = [
        (DRAFT, 'Draft'),
        (SENT, 'Sent'),
    ]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="newsletters")
    subject = models.CharField(max_length=100)
    content = models.TextField(max_length=2000)
    status = models.CharField(max_length=10, default=DRAFT, choices=LETTER_STATUS)
    written_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject
    
    def send(self, request):
        subscribers = Subscriber.objects.filter(confirmed=True)
        email = EmailMultiAlternatives(
            subject=self.subject,
            body=self.content,
            from_email=None,
            to=[subscriber for subscriber in subscribers],
        )

        email.attach_alternative(self.content, "text/html")
        try:
            email.send()
            self.status = self.SENT
            self.save()
        except:
            pass


