"""faqs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from .views import QuestionList, QuestionCreate, AnswerCreate, question_vote, answer_vote


urlpatterns = [
    url(r'^$', QuestionList.as_view(), name="home"),
    url(r'add/', QuestionCreate.as_view(), name="add"),
    url(r'add_ans/', AnswerCreate.as_view(), name="add_ans"),
    url(r'vote/(?P<question_id>[0-9]+)/(?P<t>up|down)', question_vote, name="vote"),
    url(r'vote_ans/(?P<answer_id>[0-9]+)/(?P<t>up|down)', answer_vote, name="vote_ans")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
