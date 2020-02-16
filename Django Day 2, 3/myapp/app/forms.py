from django import forms
from django.db import models
from .models import Question

class QuestionForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ('question', 'answer')