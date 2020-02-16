from django.shortcuts import render, redirect
from .models import Question
from .forms import QuestionForm
# Create your views here.
def home(request):
	return render(request, 'app/home.html')

def question(request):
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid():
			Question = form.save(commit=False)
			Question.save()
			return redirect('home')
	else:
		form = QuestionForm()
	return render(request, 'app/question.html', {'form': form})

def list(request):
	li = Question.objects.all()
	return render(request, 'app/list.html', {'list': li})