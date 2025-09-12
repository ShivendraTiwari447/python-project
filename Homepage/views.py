from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import User
from django.contrib.auth.hashers import check_password, make_password
from django.views.decorators.csrf import csrf_exempt
import json

# ----------------- Home -----------------
def home(request):
    return render(request, 'Homepage/home.html')


# ----------------- User Login -----------------
@csrf_exempt
def user_login(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"success": False, "error": "Invalid data"})

        username = data.get("username")
        password = data.get("password")

        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                # Save username in session
                request.session['username'] = user.username
                # Removed login_count to avoid AttributeError
                user.save()
                return JsonResponse({"success": True})
            else:
                return JsonResponse({"success": False, "error": "Invalid password"})
        except User.DoesNotExist:
            return JsonResponse({"success": False, "error": "User does not exist"})

    # GET request → render login page
    return render(request, 'Homepage/user_login.html')


# ----------------- User Signup -----------------
def user_register(request):
    message = ""
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            message = "Username already taken."
        elif User.objects.filter(email=email).exists():
            message = "Email already registered."
        else:
            hashed_password = make_password(password)
            User.objects.create(username=username, email=email, password=hashed_password)
            return redirect('user_login')

    return render(request, 'Homepage/signup.html', {"message": message})


# ----------------- Events Page -----------------
def events_page(request):
    username = request.session.get('username')
    return render(request, 'Homepage/events.html', {"username": username})


# ----------------- User Logout -----------------
def user_logout(request):
    request.session.flush()
    return redirect('home')


# ----------------- Admin Login -----------------
@csrf_exempt
def admin_login_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({"success": False, "error": "Invalid data"})

        username = data.get("username")
        password = data.get("password")

        # Single default admin
        if username == "admin" and password == "admin123":
            return JsonResponse({"success": True})

        return JsonResponse({"success": False, "error": "Invalid username or password"})

    return render(request, 'Homepage/admin_login.html')


# ----------------- Admin Dashboard -----------------
def admin_dashboard(request):
    users = User.objects.all()
    return render(request, 'Homepage/admin_dashboard.html', {'users': users})


# ----------------- Delete User -----------------
@csrf_exempt
def delete_user(request, user_id):
    if request.method == "POST":
        try:
            user = User.objects.get(id=user_id)
            user.delete()
            return JsonResponse({"success": True})
        except User.DoesNotExist:
            return JsonResponse({"success": False, "error": "User not found"})
    return JsonResponse({"success": False, "error": "Invalid request"})
