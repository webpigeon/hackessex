from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404

from .models import Question

class QuestionList(ListView):
    model = Question

# vote/5/up vote/5/down
def question_vote(request, question_id=None, t=None):
    if t not in ["up", "down"]:
        return HttpResponse("that's not right...")

    question = get_object_or_404(Question,pk=question_id)
    question.votes += 1 if t == "up" else -1
    question.save()
    return HttpResponse("that worked")
