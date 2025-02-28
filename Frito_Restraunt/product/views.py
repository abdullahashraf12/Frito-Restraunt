from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
from django.http import HttpResponse

def print_posted_categ_and_textfield(request):
    # Print the data to the console (or handle it as needed)
    Category = request.GET.get('category_category', 'All Categories')
    search_text = request.GET.get('search_text', '')

    print(f"Category: {Category}")
    print(f"Search Text: {search_text}")

    # Return a simple HttpResponse for now
    return HttpResponse(f"Category: {Category}, Search Text: {search_text}")
