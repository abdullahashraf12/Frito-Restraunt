# core/middleware.py

from django.shortcuts import redirect
from redis.exceptions import TimeoutError  # Import TimeoutError from Redis library
from django.urls import reverse


class RedisTimeoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            response = self.get_response(request)
        except TimeoutError:
            # Redirect to core:my_orders URL when TimeoutError occurs
            return redirect('core:my_orders')
        
        return response
