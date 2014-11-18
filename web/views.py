from django.shortcuts import render
from django.core.urlresolvers import reverse

def index(request):
    context = {}
    context['api_url'] = request.build_absolute_uri(reverse('api-root'))
    return render(request, 'home.html', context)