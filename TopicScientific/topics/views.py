from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from topics.models import topic
from topics.forms import CreateTopicForm, EditTopicForUserForm, EditTopicForSuperUserForm
from accounts.models import Account
# Create your views here.


def create_topic_view(request):

    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateTopicForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=request.user.email).first()
        obj.author = author
        obj.save()
        form = CreateTopicForm()

    context['form'] = form

    return render(request, "topics/create_topic.html", context)


def detail_topic_view(request, slug):

    context = {}

    topics = get_object_or_404(topic, slug=slug)
    context['topic'] = topics

    return render(request, 'topics/detail_topic.html', context)


def edit_topic_view(request, slug):
    context = {}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    topic_post = get_object_or_404(topic, slug=slug)
    if request.POST:
        form = EditTopicForUserForm(request.POST or None, instance=topic_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Edited"
            topic_post = obj

    form = EditTopicForUserForm(
        initial={
            "topic_name": topic_post.topic_name,
            "content": topic_post.content,
            "research_direction": topic_post.research_direction,
            "type": topic_post.type,
        }
    )
    context['form'] = form

    return render(request, 'topics/edit_topic.html', context)


def edit_topic_super_user_view(request, slug):
    context = {}
    user = request.user
    if not user.is_superuser:
        return redirect('must_authenticate')

    topic_post = get_object_or_404(topic, slug=slug)
    if request.POST:
        form = EditTopicForSuperUserForm(request.POST or None, instance=topic_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Edited"
            topic_post = obj

    form = EditTopicForSuperUserForm(
        initial={
            "rate": topic_post.rate,
            "review_date": topic_post.review_date,
            "process": topic_post.process,
        }
    )
    context['form'] = form

    return render(request, 'topics/edit_topic_super_user.html', context)


def get_topic_queryset(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        topics = topic.objects.filter(
            Q(topic_name__contains=q)|
            Q(content__icontains=q)
            ).distinct()
        for topic in topics:
            queryset.append(topic)

    # create unique set and then convert to list
    return list(set(queryset))
