from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.

def home(request):
	records = Record.objects.all()
	context= {'records': records}
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Bienvenue, vous êtes bien connectés !")
			return redirect('home')
		else:
			messages.error(request, "Impossible de vous connecter, verifiez vos informations de connectiion")
			return redirect('home')
	else:
		return render(request, 'home.html',context)

# def login_user(request):
#     pass

def logout_user(request):
	logout(request)
	messages.info(request, "vous êtes bien déconectés, à bientôt")
	return redirect('home')

def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "You Have Successfully Registered! Welcome!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})

def customer_record(request, pk):
	if request.user.is_authenticated:
		customer_record = Record.objects.get(id=pk)
		return render(request,  'record.html', {'customer_record':customer_record})
	else:
		messages.error(request, "Vous devez être connectés pour voir cette page..." )
		return redirect('home')
	# 	customer_record=Record.objects.get(id=pk)
	# 	return render(request, 'record.html', {'customer_record':customer_record})
	# else:
	# 	messages.success(request, "Vous devez être connectés pour voir cette page...")
	# 	return redirect('home')


def delete_record(request, pk):
	if request.user.is_authenticated:
		delete_it = Record.objects.get(id=pk)
		delte_it.delete()
		messages.success(request, "Enregistrement supprimé avec succès !")
		return redirect('home')
	else :
		messages.success(request, "Désolé, vous devez être connectés pour effectuer cette opération !")
		return redirect('home')


def add_record(request):
	form = AddRecordForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_record = form.save()
				messages.success(request, "Engegistrement effectué avec succès !")
				return redirect('home')
		return render(request, 'add_record.html', {'form': form})
	else:
		messages.success(request, "Désolé, vous devez être connectés pour effectuer cette opération !")
		return redirect('home')

def update_record(request, pk):
	if request.user.is_authenticated:
		current_record = Record.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance=current_record)
		if form.is_valid():
			form.save()
			messages.success(request, "Enregistrement modifié avec succès !")
			return redirect('home')
		return render(request, 'update_record.html', {'form': form})
	else:
		messages.success(request, "Désolé, vous devez être connectés pour effectuer cette opération !")
		return redirect('home')



