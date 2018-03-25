from django.shortcuts import render
from .models import Student,Branch,Info
from .forms import InfoForm
from django.http  import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index1(request):
	num_students = Student.objects.all().count()
	num_branchs = Branch.objects.all().count()

	return render(
		request,
		'index1.html',
		context = {'num_branchs' :num_branchs,'num_students':num_students},
		)






