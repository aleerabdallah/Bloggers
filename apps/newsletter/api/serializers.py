from newsletter.models import Subscriber, Newletter
from rest_framework import serializers
# from utils import random_digits
from newsletter.utils import random_digits
from django.conf.global_settings import DEFAULT_FROM_EMAIL
from newsletter.utils import encode_id
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from accounts.models import UserAccount

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['first_name', 'last_name', 'email']



class CreateNewsLetterSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    class Meta:
        model = Newletter
        fields = ['subject', 'content', 'id', 'author', 'status', 'written_on', 'last_modified']
        read_only_fields = ['id', 'status', 'written_on', 'last_modified']




class SubscriberSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['email', 'conf_num', 'confirmed']
        read_only_fields = ['conf_num', 'confirmed']
    
    def validate(self, attrs):
        email = attrs.get('email')
        try:
            subscriber = Subscriber.objects.get(email=email)

            if subscriber is not None:
                if subscriber.confirmed:
                    raise serializers.ValidationError("You are alread subscribed!")
                else:
                    raise serializers.ValidationError("Please confirmed your email")
        except Subscriber.DoesNotExist:

            subscriber = Subscriber.objects.create(email=email)
            conf_num = random_digits()
            subscriber.conf_num = conf_num
            subscriber.save()
            # After saving the subscriber instance, send the confirmation message to their inbox
            subs_id = encode_id(subscriber.id)

            link = f"https://alsulk.vercel.app/newsletter/confirm/{subs_id}/{conf_num}/"
 
            user_info = {'link': link}
            html_message = render_to_string("newsletter/subscription-letter.html", user_info)
            plain_message = strip_tags(html_message)
            email = EmailMultiAlternatives(
                subject="ALSULK Newsletter Subscription",
                body=plain_message,
                from_email=None,
                to=[subscriber.email],
            )

            email.attach_alternative(html_message, "text/html")
            email.send()


        return super().validate(attrs)



