from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Project
import bcrypt

def home(request):
	return render(request, 'project_app/home.html')

def login(request):
    return render(request, 'project_app/user_dash.html')

def register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    if len(first_name) == 0:
        messages.error(request,"Please enter first name")
        return redirect('/')
    if len(last_name) == 0:
        messages.error(request,"Please enter last name")
        return redirect('/')
    if len(email) == 0:
        messages.error(request,"Please enter email")
        return redirect('/')
    if len(password) == 0:
        messages.error(request,"Please enter password")
        return redirect('/')
    else:
        hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = create_user(request.POST, hashed_password)
        request.session['id'] = user.id
        return redirect('/dashboard')

def log_in(request):
    users = User.objects.filter(email=request.POST['email'])
    for user in users:
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            print("Password matches!")
            request.session['id'] = user.id
            return redirect('/dashboard')
        else:
            messages.error(request, "Failed password")
            return redirect('/')

def create_user(form, hash):
    new_user = User.objects.create()
    new_user.first_name = form['first_name']
    new_user.last_name = form['last_name']
    new_user.email = form['email']
    new_user.password = hash
    new_user.save()
    return new_user

def dashboard(request):
    context = {
        "my_projects": Project.objects.filter(creator_id=request.session["id"]).filter(done=False),
        "my_past_projects": Project.objects.filter(creator_id=request.session["id"]).filter(done=True),
    }
    return render(request, 'project_app/user_dash.html', context)

def proj_board(request):
    return render(request, 'project_app/proj_board.html')

def new_project(request):
    return render(request, 'project_app/new_project.html')

def create_project(request):
    title = request.POST["name_input"]
    description = request.POST["description_input"]
    creator_id = request.session["id"]
    new_project = Project.objects.create(title=title, description=description, creator_id=creator_id)
    new_project.save()
    return redirect(f"/view_project/{new_project.id}")

def view_project(request, project_id):
    context = {
        "this_project": Project.objects.get(id=project_id),
    }
    return render(request, 'project_app/proj_board.html', context)

def logout(request):
    try:
        del request.session["id"]
    except KeyError:
        return render(request, 'project_app/dashboard.html')
    return redirect('/')