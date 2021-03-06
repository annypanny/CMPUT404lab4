from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse

from models import Question, Choice

# Create your views here.
from django.views import generic


from django.http import HttpResponseRedirect,HttpResponse

class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = "latest_question_list"
	def get_queryset(self):
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'detail.html'

class ResultsView(generic.DetailView):
	model = Question
	template_name = 'results.html'

#def index(request):
	#return HttpResponse("Hello, world. You're at the polls index.")
#	latest_question_list = Question.objects.order_by('-pub_date')[:5]
#	context = {'latest_question_list': latest_question_list}
	#output = ', '.join([p.queston_text forp in latest_question_list])
	#return HttpResponse(output)
	#return render(request, 'polls/index.html',context) 
#	return render(request, 'index.html',context) 
#def detail(request, question_id):
	#return HttpResponse("You're looking at question %s." % question_id)
#	question = get_object_or_404(Question, pk=question_id)
#	return render(request, 'detail.html',{'question':question})
#def results(request, question_id):
#	question = get_object_or_404(Question, pk=question_id)
#	return render(request, 'results.html',{'question':question})
	#response = "You're loking at the results of question %s."
	#return HttpResponse(response % question_id)

def vote(request, question_id):
	p = get_object_or_404(Question, pk=question_id)
	try: 
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'detail.html', {
			'question': p, 
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

	#return HttpResponse("You're voting on question %s." % question_id)



	
