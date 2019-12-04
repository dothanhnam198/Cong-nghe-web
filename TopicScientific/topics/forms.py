from django import forms
from topics.models import topic


class CreateTopicForm(forms.ModelForm):

    class Meta:
        model = topic
        fields = ['topic_name', 'research_direction', 'type', 'content']


class EditTopicForUserForm(forms.ModelForm):

    class Meta:
        model = topic
        fields = ['topic_name', 'research_direction', 'type', 'content']

    def save(self, commit=True):
        topic_post = self.instance
        topic_post.topic_name = self.cleaned_data['topic_name']
        topic_post.content = self.cleaned_data['content']
        topic_post.research_direction = self.cleaned_data['research_direction']
        topic_post.type = self.cleaned_data['type']

        if commit:
            topic_post.save()
        return topic_post


class EditTopicForSuperUserForm(forms.ModelForm):

    class Meta:
        model = topic
        fields = ['rate', 'review_date', 'process']

    def save(self, commit=True):
        topic_post = self.instance
        topic_post.rate = self.cleaned_data['rate']
        topic_post.review_date = self.cleaned_data['review_date']
        topic_post.process = self.cleaned_data['process']

        if commit:
            topic_post.save()
        return topic_post


