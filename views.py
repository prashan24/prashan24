from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.http import HttpResponse
from Register.models import Register

# Create your views here.
def register_page(request):
    if request.method == "POST":
        firstname=request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        country = request.POST['country']
        mobile = request.POST['mobile']
        password = request.POST['password']
        confirm_password = request.POST['password_confirmation']

        val1 = Register.objects.filter(UserName=username).exists()
        val2 = Register.objects.filter(Email=email).exists()
        error_message = None
        message = None
        if val1:
            error_message = 'username already exist'
            return redirect('Register')
        elif val2:
            error_message = 'email already exists'
            return redirect('Register')
        else:
            user = Register(FirstName=firstname,LastName=lastname,UserName=username, Email=email, Country=country, Mobile=mobile,
                            Password=password, Confirm_Password =confirm_password)

            user.Password = make_password(user.Password)
            user.save()

            return render(request, 'register_page.html', {'error_message': error_message, 'message': message})


    return render(request, 'register_page.html')
