import django_filters as df
from .models import *
from django import forms

b = Student.objects.values_list("urn", flat = True).distinct()
choice_b = [('','All')] + [(id,id) for id in b]

class studentfilter(df.FilterSet):
	URN = df.CharFilter(widget = forms.Select(choices = choice_b)) 
