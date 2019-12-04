from django.shortcuts import render
from topics.views import get_topic_queryset
from topics.models import topic
# Create your views here.


def home(request):

    context = {}

    query = ""
    if request.GET:
        query = request.GET['q']
        context['query'] = str(query)

    topics = get_topic_queryset(query)
    context['topics'] = topics

    return render(request, 'topics/home.html', context)