from django.urls import path
from . import views




app_name = "newsletter"



newsletter_pattern = [
    path('confirm/<str:id>/<int:conf_num>/', views.ConfirmSubscribtionEmailAPIView.as_view(), name="confirm-newsletter"),
    path('subscribe/', views.NewsLatterSubscribtionAPIView.as_view(), name="newletter-subscription"),
    # path('unsubscribe/', views.NewsLatterSubscribtionAPIView.as_view(), name="newletter-subscription"),
    path("newsletter/", views.CreateNewsLetterAPIView.as_view(), name="createNewsLetter"),
    path("newsletter/<int:pk>/", views.NewsletterAPIView.as_view(), name="createNewsLetter"),
    path('newsletter/send/<int:pk>/', views.SendNewsLetterAPIView.as_view(), name="sendNewsletter")
]
