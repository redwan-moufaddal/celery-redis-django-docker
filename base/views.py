# views.py
from django.http import JsonResponse
from django.shortcuts import render
from .tasks import process_user_input

def home_page(req):
    if req.method == "POST":
        text = req.POST.get('user_input', 'hi')
        task = process_user_input.delay(text)
        
        # Return response immediately or manage task status
        response = JsonResponse({'status': 'Processing', 'task_id': task.id})
        return response

    return render(req, 'index.html')
