# from django.shortcuts import render
# from .tasks import process_user_input
# from celery.result import AsyncResult
# import time

# def home_page(request):
#     messages = []
    
#     if request.method == "POST":
#         text = request.POST.get('user_input')
#         task = process_user_input.delay(text)
        
#         # Add user message to the context
#         messages.append({'text': text, 'class': 'user'})
        
#         # Polling for task status (blocking call, not recommended for production)
#         while True:
#             result = AsyncResult(task.id)
#             if result.ready():
#                 messages.append({'text': result.result, 'class': 'ai'})
#                 break
#             else:
#                 # This avoids a tight loop, but the page will keep refreshing
#                 messages.append({'text': 'Processing...', 'class': 'ai'})
#                 time.sleep(1)  # Wait for 1 second before checking again

#     return render(request, 'index.html', {'messages': messages})
from django.http import JsonResponse
from django.shortcuts import render
from .tasks import process_user_input
from celery.result import AsyncResult
import time

def home_page(request):
    return render(request, 'index.html')

def submit_task(request):
    if request.method == "POST":
        text = request.POST.get('user_input')
        task = process_user_input.delay(text)
        return JsonResponse({'task_id': task.id})

def check_task_status(request, task_id):
    result = AsyncResult(task_id)
    if result.ready():
        return JsonResponse({'status': 'completed', 'result': result.result})
    else:
        return JsonResponse({'status': 'pending'})
