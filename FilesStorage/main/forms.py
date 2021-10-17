from django import forms
from .models import File
from django_filters import rest_framework as filters


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = {'file','title','type','size','details'}


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class FileFilter(filters.FilterSet):

    size = filters.RangeFilter()
    type = CharFilterInFilter(field_name='type', lookup_expr='in')
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    time = filters.RangeFilter()


    class Meta:
        model = File
        fields = ['size', 'type','name','time']
