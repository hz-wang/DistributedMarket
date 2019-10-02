from django.shortcuts import render
from django.http import HttpResponse

##### User API #####
def register(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0

    return render(request, 'register_status.json', context, 
        content_type='application/json')

def login(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'User login API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')

##### Machine API #####
def submit_machine(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'Submit machine API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')

def remove_machine(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'Remove machine API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')

def list_machines(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'List machine API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')

##### Job API #####
def submit_job(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'Submit job API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')

def cancel_job(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'Cancel job API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')

def get_result(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'Get result API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')

def get_log(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'Get log API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')

##### Credit API #####
def get_credit(request):
    context = {}
    context['status'] = True
    context['error_code'] = 0
    context['message'] = 'Get credit API'

    return render(request, 'general_status.json', context, 
        content_type='application/json')
