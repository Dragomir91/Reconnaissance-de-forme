from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpRequest
from django.template import loader
from django.urls import reverse
from .models import Choice, Question, Login
from django.views import generic
from django.utils import timezone
from .form import Login_id
from django.views.decorators.csrf import csrf_exempt
import numpy as np
import cv2
'''def index(request):
    return HttpResponse("Hello, world. You're at the polls index. I understand better")
# Create your views here.'''
'''
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]
    
class DetailView(generic.DetailView):
    ...
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())
'''   

def req(request):
    tab = np.arange(10)
    formulaire = Login_id
    if request.method == "POST":
        formulaire = Login_id(request.POST, request.POST)
        login_database = Login.objects.get(pk = 1)
        if formulaire.is_valid():
            if request.POST['username'] == login_database.name and request.POST["pwd"] == login_database.pwd:
                return HttpResponse(tab)
            else:
                return HttpResponse("incorrecte login")
    return render(request, 'polls/recognition.html', {'formulaire':formulaire})
       
          
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
       
    except Question.DoesNotExist:   
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question })
    return HttpResponse("You're looking at question %s." % question_id)
    
def index(request):
    tab = np.arange(10)
    formulaire = Login_id
    latest_question_list = Question.objects.order_by('pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {'latest_question_list': latest_question_list,'formulaire':formulaire}
    if request.method == "POST":
        formulaire = Login_id(request.POST, request.POST)
        login_database = Login.objects.get(pk = 1)
        if formulaire.is_valid():
            if request.POST['username'] == login_database.name and request.POST["pwd"] == login_database.pwd:
                return render(request,"polls/recognition.html",{"formulaire" : formulaire})
            else:
                return HttpResponse("incorrecte login")

    #return HttpResponse(template.render(context)) #change la forme du HTML
    return render(request,'polls/index.html',context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})            

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
