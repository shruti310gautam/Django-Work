from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from .models import Choice, Question, Candidate
from django.template import loader
from django.http import Http404
from django.urls import reverse
from polls.forms import ContactDetails
from django.utils import timezone
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse
import json

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
    	"""
    	Return the last five published questions (not including those set to be
    	published in the future).
    	"""
    	return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


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
        selected_choice.votes += selected_choice.votes
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def contact(request):

    if request.method == 'POST':
        f = ContactDetails(request.POST)
        if f.is_valid():
            c = Candidate(name = request.POST["contact_name"])
            c.save()
            return HttpResponse("Entry Saved !!")	 
    else:   
        f = ContactDetails()  
    return render(request, 'polls/contact.html', {'form' : f})
#def get(self, request):
#	form = ContactDetails()
#	return render(request, 'polls/contact.html',{'form' : form})

      #  data = Candidate.objects.all()
      
def todo(request):
    if request.is_ajax():
        JsonObj = ["vansh", "shrey", "shru",]
        data = json.dumps(JsonObj)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404

def more(request):
    if request.is_ajax():
        a = Candidate.objects.values()
        b = list(a)
        data = json.dumps(b)
        return HttpResponse(data, content_type= 'application/json')
    else:
        raise Http404



