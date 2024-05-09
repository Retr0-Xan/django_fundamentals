from django.shortcuts import render

# Create your views here.
def display_users(request):
    return render(request,'users/user_list.html')

def register_user(request):
    return render(request,'users/register.html')

