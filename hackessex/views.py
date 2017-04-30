from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.shortcuts import get_object_or_404


from .models import Room, Question, Answer

class Home(ListView):
    model = Room
    template_name="home.html"

def Home2(request):
    model = Room
    return render_to_response("home.html")

class QuestionList(ListView):
    model = Question

    def get_queryset(self):
        q = super(QuestionList, self).get_queryset()
        try:
            room_id = int(self.kwargs.get('room'))
            if room_id < 0:
                return q.filter(room=abs(room_id), hidden=True)
            else:
                return q.filter(room=room_id, hidden=False)
        except ValueError:
            return HttpResponse("that is not a valid room number")

    def get_context_data(self, **kwargs):
        context = super(QuestionList, self).get_context_data(**kwargs)
        context['room'] = get_object_or_404(Room, pk=abs(int(self.kwargs.get('room'))))
        return context

class QuestionCreate(LoginRequiredMixin, CreateView):
    model = Question
    fields = ["text", "category", "hide_id"]

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        form.instance.room_id = self.kwargs.get('room')
        return super(QuestionCreate, self).form_valid(form)

class AnswerCreate(LoginRequiredMixin, CreateView):
    model = Answer
    fields = ["text"]

    def get_context_data(self, **kwargs):
        context = super(AnswerCreate, self).get_context_data(**kwargs)
        context['question'] = get_object_or_404(Question, pk=self.kwargs.get('question'))
        return context

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        form.instance.question_id = self.kwargs.get('question')
        return super(AnswerCreate, self).form_valid(form)

# vote/5/up vote/5/down
@login_required
def question_vote(request, question_id=None, t=None):
    if t not in ["up", "down"]:
        return HttpResponse("that's not right...")

    question = get_object_or_404(Question,pk=question_id)
    question.votes += 1 if t == "up" else -1
    question.save()
    return redirect(question.get_absolute_url())

@login_required
def answer_vote(request, answer_id=None, t=None):
    if t not in ["up", "down"]:
        return HttpResponse("that's not right...")

    answer = get_object_or_404(Answer,pk=answer_id)
    answer.votes += 1 if t == "up" else -1
    answer.save()
    return redirect(answer.get_absolute_url())
