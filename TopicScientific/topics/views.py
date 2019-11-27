from django.shortcuts import render
from topics.models import topic
# Create your views here.


def home(request):

    context = {}
    topics = topic.objects.all()
    context['topics'] = topics

    return render(request, 'topics/home.html', context)



