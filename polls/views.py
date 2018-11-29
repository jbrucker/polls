from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import JsonResponse
from django.template import loader
from django.urls import reverse
from django.views import generic
from .models import Question

def get_questions_as_text(request):
    """get list of questions"""
    #questions = Question.objects.order_by('-pub_date')[:10]
    questions = Question.objects.order_by('id')[:10]
    list = ''
    for q in questions:
        list += q.question_text + '\n'
    return HttpResponse(list, content_type="text/plain")

def get_questions_as_json(request):
    """get list of questions as a Json object"""
    #questions = Question.objects.order_by('-pub_date')[:10]
    questions = Question.objects.order_by('id')[:10]
    qdict = {}
    for q in questions:
        qdict[q.id] = q.question_text
    return JsonResponse(qdict)

def index(request):
    """show index of recent poll questions"""
    #questions = Question.objects.order_by('-pub_date')[:10]
    questions = Question.objects.order_by('id')[:10]
    template = loader.get_template('polls/index.html')
    # If you use template.render() it does NOT get an automatic reference 
    # to current user. You must add to context yourself.
    #return HttpResponse(template.render({'question_list':questions,'user':request.user}), request)
    # if you use the render shortcut, it _does_ get a reference to user
    return render(request, 'polls/index.html', {'question_list':questions})

def detail(request, question_id):
    """Display details of a single question, select by question_id."""
    try:
        q = Question.objects.get(id=question_id)
    except:
        return HttpResponseNotFound("Question id %d not found." % question_id)
    context = {"question":q}
    return render(request, 'polls/detail.html', context)

@login_required(login_url='/accounts/login/') # '/accounts/login/'
def vote(request, question_id):
    """Vote for one of the answers to a question."""
    try:
        q = Question.objects.get(id=question_id)
        choice_id = request.POST['choice_id']
        print("Question ",q," Selected choice_id", choice_id)
        choice = q.choice_set.get(pk=choice_id)
        print("Choice is", choice)
    except:
        context = {'question':q, 'error_message':"Missing or invalid answer choice"}
        return render(request, 'polls/detail.html', context)
    # Add 1 to votes for this choice
    choice.votes += 1
    choice.save()
    return HttpResponseRedirect(reverse('polls:results',args=(q.id,)))

def results(request, question_id):
    """Show results of a poll. Same as ResultsView class w/o using a class view."""
    try:
        q = Question.objects.get(id=question_id)
        choices = q.choice_set.all()
    except:
        return HttpResponseNotFound("Question id %d not found." % question_id)
    # show all choices and votes
    context = {'question':q}
    return render(request, 'polls/results.html', context )

##################################################################################
# Class-based views for the same thing as above

class PollListView(generic.ListView):
    model = Question
    # context_object_name = 'myquestion_list"  # name of variable injected into template
    # queryset = Question.objects.all()[:10]
    # template_name = 'question_list.html'     # this is the default name
    queryset = Question.objects.all().order_by()

from django.contrib.auth.mixins import LoginRequiredMixin
class DetailView(LoginRequiredMixin,generic.DetailView):
    """Class based view for viewing a poll."""
    model = Question
    template_name = 'polls/detail.html'
    # values used by LoginRequiredMixin
    login_url = '/accounts/login/'
    #redirect_field_name = 


class ResultsView(generic.DetailView):
    """The urls() mapping should include a url pattern to match the primary key (pk)
       of Question.  This is used by superclass to select an object from the model.
    """
    model = Question
    template_name = 'polls/results.html'
