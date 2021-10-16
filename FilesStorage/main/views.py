from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
from .models import File
from django.core.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from .forms import FileFilter
from django.views.generic import ListView


class FileListView(ListView):
    filter_backends = [DjangoFilterBackend]
    filterset_class = FileFilter
    model = File
    template_name = 'upload.html'
    context_object_name = 'files'

def index(request):
    return render(request, 'main/index.html')


def upload(request):  # Загрузка файлов
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    else:
        files = File.objects.all()
    context['files'] = files
    return render(request, 'main/upload.html', context)


def notime(request):
    context = {}
    #files = File.objects.filter(type='rar') '''Фильтрация'''
    files = File.objects.all()
    context['files'] = files
    return render(request, 'main/notime.html', context)


def filter(request):  # Список файлов и их фильтрация
    form = FileForm()
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        if uploaded_file.size > 838860800:
            raise ValidationError('Размер файла больше 100мб')
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
        else:
            form = FileForm()
    return render(request, 'main/filter.html', {
        'form': form
    })


Queryset = File.objects.filter(type="123")

