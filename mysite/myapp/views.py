from django.shortcuts import render, render_to_response
from django import template
register = template.Library()

# Create your views here.
def index (request):
    return render_to_response('index.html')

@register.inclusion_tag('results.html')
def movies (request):
    return render_to_response('movies.html')

def sorrytobotheryou (request):
    return render_to_response('sorrytobotheryou.html')

def navBarTemplate(request):
    return render_to_response('index.html')

def books (request):
    return render_to_response('books.html')

def richdadpoordad (request):
    return render_to_response('richdadpoordad.html')