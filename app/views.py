from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Repository
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect, get_object_or_404\




# Create your views here.
def Homepage(request):
    return render(request, 'index.html')

@login_required
def Afterlogin(request):
    user = request.user
    context = {
        'user_id': user.id,
        'username': user.username,
        'email': user.email,
    }
    return render(request, 'aftlogin/Afterloginpg.html', context)




from django.shortcuts import render, redirect  
from django.contrib.auth.decorators import login_required  
from django.contrib.auth.models import User  
  
  
def showprofile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    try:
        profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        profile = None

    context = {
        'user_profile': user_profile,
        'profile': profile
    }
    return render(request, 'footerpgs/showprofile.html', context)


  
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile

def updateprofile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        bio = request.POST.get('bio', '').strip()
        hobbies = request.POST.get('hobbies', '').strip()
        skill1 = request.POST.get('skill1', '').strip()
        progress1 = request.POST.get('progress1', '0').strip()
        skill2 = request.POST.get('skill2', '').strip()
        progress2 = request.POST.get('progress2', '0').strip()
        skill3 = request.POST.get('skill3', '').strip()
        progress3 = request.POST.get('progress3', '0').strip()

        if bio:
            user_profile.bio = bio
        if hobbies:
            user_profile.hobbies = hobbies
        if skill1:
            user_profile.skill1 = skill1
        if progress1.isdigit():
            user_profile.progress1 = int(progress1)
        if skill2:
            user_profile.skill2 = skill2
        if progress2.isdigit():
            user_profile.progress2 = int(progress2)
        if skill3:
            user_profile.skill3 = skill3
        if progress3.isdigit():
            user_profile.progress3 = int(progress3)
        
        user_profile.save()
        return redirect('showprofile')

    return render(request, 'footerpgs/updateprofile.html', {'user_profile': user_profile})




    
    

from django.shortcuts import render
from .models import Repository

def Repositories(request):
    query = request.GET.get('q')
    if query:
        repositories = Repository.objects.filter(user=request.user, rep_name__icontains=query)
    else:
        repositories = Repository.objects.filter(user=request.user)
    
    data = []
    for repository in repositories:
        file_url = repository.file.url if repository.file and hasattr(repository.file, 'url') else None
        data.append({
            'rep_id': repository.rep_id,
            'rep_name': repository.rep_name,
            'rep_des': repository.rep_des,
            'file_url': file_url,
            'username': repository.user.username
        })
    
    return render(request, 'aftlogin/repo.html', {'repositories': data})

from .models import Repository

from django.shortcuts import render
from .models import Repository

from django.shortcuts import render
from .models import Repository

from django.shortcuts import render
from .models import Repository





def Upload(request):
    return render(request, 'aftlogin/upload.html')

def Blog(request):
    return render(request, 'footerpgs/blog.html')

def Careers(request):
    return render(request, 'footerpgs/careers.html')

def Contact(request):
    return render(request, 'footerpgs/contact.html')

def Customers(request):
    return render(request, 'footerpgs/customers.html')

def Privacy(request):
    return render(request, 'footerpgs/privacynotice.html')

def Reviews(request):
    return render(request, 'footerpgs/reviews.html')

def Security(request):
    return render(request, 'footerpgs/security.html')

def Services(request):
    return render(request, 'footerpgs/servicestatus.html')

def Support(request):
    return render(request, 'footerpgs/supportcenter.html')

def Terms(request):
    return render(request, 'footerpgs/termsofuse.html')

def About(request):
    return render(request, 'footerpgs/about.html')

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        data = auth.authenticate(username=username, password=password)

        if data is not None:
            auth.login(request, data)
            return redirect('Afterlogin')

    return render(request, 'signin.html')

from .models import Profile

def signup(request):
    if request.method == "POST":
        name = request.POST.get('Name')
        username = request.POST.get('username')
        groupid = request.POST.get('group')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return render(request, 'signup.html', {'error': "Passwords do not match!"})

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'signup.html', {'error': "Username already exists!"})

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, 'signup.html', {'error': "Email already exists!"})

        user = User.objects.create_user(email=email, username=username, password=pass1)
        user.first_name = name
        user.save()

        profile = Profile.objects.get(user=user)
        profile.groupid = groupid
        profile.save()

        messages.success(request, "Account created successfully!")
        return redirect('signin')

    return render(request, 'signup.html')

from django.shortcuts import render
from .models import Repository, Profile

def Library(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        groupid = profile.groupid
        query = request.GET.get('q')

        if query:
            repositories = Repository.objects.filter(user__profile__groupid=groupid, rep_name__icontains=query)
        else:
            repositories = Repository.objects.filter(user__profile__groupid=groupid)
    else:
        repositories = []

    data = []
    for repository in repositories:
        file_url = repository.file.url if repository.file and hasattr(repository.file, 'url') else None
        data.append({
            'rep_id': repository.rep_id,
            'rep_name': repository.rep_name,
            'rep_des': repository.rep_des,
            'file_url': file_url,
            'username': repository.user.username
        })

    return render(request, 'aftlogin/library.html', {'data': data})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Repository

def Create(request):
    if request.method == 'POST':
        rep_id = request.POST.get('rep_id', '')
        rep_name = request.POST.get('rep_name', '')
        rep_des = request.POST.get('rep_des', '')
        file = request.FILES.get('file', None)  # Get the uploaded file
      

        # Validate and save the form data
        if rep_id and rep_name and rep_des and file:
            repository = Repository(rep_id=rep_id, rep_name=rep_name, rep_des=rep_des, file=file, user=request.user)
            repository.save()
            messages.success(request, "Repository created successfully.")
            return redirect('Repositories')
        else:
            messages.error(request, "Please fill out all fields and upload a file.")

    return render(request, 'aftlogin/create.html')


def Update(request, rep_id):
    repository = get_object_or_404(Repository, rep_id=rep_id)

    if request.method == 'POST':
        rep_name = request.POST.get('rep_name', '')
        rep_des = request.POST.get('rep_des', '')
        file = request.FILES.get('file', None)

        repository.rep_name = rep_name
        repository.rep_des = rep_des
        if file:
            repository.file = file
        repository.save()

        return redirect('Repositories')
    else:
        return render(request, 'aftlogin/update.html', {'repository': repository})
    

@login_required
def user_profile(request):
    # Retrieve the user information from the request
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'aftlogin/user_profile.html', context)

def logout_view(request):
    logout(request)
    return redirect('Homepage')







# yourapp/views.py

# yourapp/views.py

from django.shortcuts import render, redirect  
from django.contrib.auth.decorators import login_required  
from.models import Profile  
  
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Profile , UserProfile
@login_required  
def profileform(request):  
   profile, created = UserProfile.objects.get_or_create(user=request.user)  
   if request.method == 'POST':  
      profile.bio = request.POST.get('bio')  
      profile.hobbies = request.POST.get('hobbies')  
      profile.skill1 = request.POST.get('skill1')  
      profile.progress1 = int(request.POST.get('progress1'))  
      profile.skill2 = request.POST.get('skill2')  
      profile.progress2 = int(request.POST.get('progress2'))  
      profile.skill3 = request.POST.get('skill3')  
      profile.progress3 = int(request.POST.get('progress3'))  
      profile.save()  
      return redirect('showprofile')  
   return render(request, 'profileform.html', {'profile': profile}) 
   
