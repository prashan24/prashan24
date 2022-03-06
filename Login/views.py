from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Register.models import Register


def login_view(request):
    if request.method == "POST":
        email = request.POST['username']
        password = request.POST['password']
        error_message = None
        try:
            match = Register.objects.filter(Email=email).exists()
            user = Register.objects.get(Email=email)
        except:
            error_message = 'Invalid credentials'

        print(match)

        if match:
            flag = check_password(password, user.Password)

            if flag:
                request.session['user_id'] = user.id
                request.session['email'] = user.Email
                request.session['username'] = user.UserName
                print(user.UserName)
                return redirect('dashboard')
            else:
                error_message = 'Incorrect password'
                print('first')
                return render(request, 'login_page.html', {'error_message': error_message})
        else:
            print('Invalid credentials')
            print('second')
            return render(request, 'login_page.html', {'error_message': error_message})

    return render(request, 'login_page.html')

def logout(request):
    return render(request, 'logout_page.html')


def dashboard(request):
    return  render(request,'dashboard.html')

