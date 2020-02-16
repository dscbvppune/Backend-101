from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import Attendee
from .forms import AttendeeForm
import json
# Create your views here.
def home(request):
	return HttpResponse("Hello world")

def attendee_specific(request):
	tempDetails = Attendee.objects.filter(name='Dewansh Rawat')
	tempMap = {
		"name": tempDetails[0].name,
		"email": tempDetails[0].email,
		"mobile": tempDetails[0].mobileNum
	}
	return JsonResponse(tempMap, safe=False)

def attendee_new(request):
	if request.method == 'POST':
		form = AttendeeForm(request.POST)
		form.save()
		return redirect('home')
	else:
		form = AttendeeForm()
	return render(request, 'dscbvp/new.html', {'form': form})

def attendees(request):
	tempObj = Attendee.objects.all()
	details = []
	for i in tempObj:
		tempMap = {
			"name": i.name,
			"email": i.email,
			"mobile": i.mobileNum
		}
		details.append(tempMap)
	result = {
		"results": details
	}
	return JsonResponse(result, safe=False)


def attendee_details(request):
	if request.method == 'POST':-
		payload = json.loads(request.body)
		tempEmail = payload["email"]
		tempObj = Attendee.objects.get(email=tempEmail)
		tempDetails = {
			"name": tempObj.name,
			"email": tempObj.email,
			"mobile": tempObj.mobileNum,
			"Last Login": tempObj.login_Date
		}
		return JsonResponse(tempDetails, safe=False)



