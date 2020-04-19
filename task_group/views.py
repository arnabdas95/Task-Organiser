
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,UpdateView,CreateView,DeleteView
from . import models
from .models import Catagories




class TaskListView(ListView):
    context_object_name = 'tasks'
    model = models.Task

    def get_context_data(self, **kwargs):
        context = super(TaskListView, self).get_context_data(**kwargs)
        context['cat_list'] = Catagories.objects.all()
        print(context)
        return context


class TaskCreateView(CreateView):

    fields = ( 'Catagories' ,'title')
    model = models.Task
    success_url = reverse_lazy("task_group:tlist")

    def get_context_data(self, **kwargs):
        context = super(TaskCreateView, self).get_context_data(**kwargs)
        context['cat_list'] = Catagories.objects.all()
        print(context)
        return context

class TaskDeleteView(DeleteView):
    model = models.Task
    success_url = reverse_lazy("task_group:tlist")

    def get_context_data(self, **kwargs):
        context = super(TaskDeleteView, self).get_context_data(**kwargs)
        context['cat_list'] = Catagories.objects.all()
        print(context)
        return context


class TaskUpdateView(UpdateView):
    fields = ('Catagories' , 'title', 'done')
    model = models.Task
    success_url = reverse_lazy("task_group:tlist")

    def get_context_data(self, **kwargs):
        context = super(TaskUpdateView, self).get_context_data(**kwargs)
        context['cat_list'] = Catagories.objects.all()
        print(context)
        return context




class CatagoriesDetailView(DetailView):
    context_object_name = 'catagories_detail'
    model = models.Catagories
    template_name = 'task_group/catagories_detail.html'

    def get_context_data(self, **kwargs):
        context = super(CatagoriesDetailView, self).get_context_data(**kwargs)
        context['cat_list'] = Catagories.objects.all()
        print(context)
        return context


class CatagoriesCreateView(CreateView):
    #fields is a tuple not str so add a ,
    fields = ('catagories_name',)
    model = models.Catagories
    success_url = reverse_lazy("task_group:tlist")

    def get_context_data(self, **kwargs):
        context = super(CatagoriesCreateView, self).get_context_data(**kwargs)
        context['cat_list'] = Catagories.objects.all()
        print(context)
        return context


class CatagoriesDeleteView(DeleteView):
    model = models.Catagories
    success_url = reverse_lazy("task_group:tlist")

    def get_context_data(self, **kwargs):
        context = super(CatagoriesDeleteView, self).get_context_data(**kwargs)
        context['cat_list'] = Catagories.objects.all()
        print(context)
        return context