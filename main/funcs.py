from random import sample
import string
from django.shortcuts import render, redirect

def generate_code():
    return ''.join(sample(string.ascii_letters + string.digits, 15))



def staff_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_staff:
            result = func(request, *args, **kwargs)
        else:
            return redirect('front:index')
        return result
    return wrapper
