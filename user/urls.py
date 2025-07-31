from django.urls import path

from . import views


urlpatterns=[
    path('',views.index),
    path('home/',views.index),
    path('about/',views.about),
    path('alumony/',views.alumony),
    path('contact/',views.contact),
    path('course/',views.courses),
    path('faculty/',views.faculty),
    path('feedback/',views.feedback),
    path('gallery/',views.gallery),
    path('infra/',views.infra),
    path('recruiters/',views.recruiters),
    path('principal/',views. principal),
    path('portfolio/',views. portfolio),
    path('faqs/',views.faqs),
    path('help/',views.help),
    path('chat/',views.chat),

]