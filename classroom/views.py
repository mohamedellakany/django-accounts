from django.shortcuts import render
from django.views.generic import (
    TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView)
from . forms import ContactForm
from . models import Teacher
from django.urls import reverse_lazy
# Create your views here.


class HomeView(TemplateView):
    template_name = 'classroom/home.html'


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'classroom/contact.html'
    success_url = reverse_lazy('classroom:thank_you')

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class TeacherCreateView(CreateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:list_teacher')
    # modelname_form.html === teacher_form.html


class TeacherListView(ListView):
    model = Teacher
    context_object_name = 'teacher_list'
    queryset = Teacher.objects.order_by("first_name")
    # modelname_list.html === teacher.list.html


class TeacherDetailView(DetailView):
    model = Teacher
    # modelname_detail.html === teacher_detail.html


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy('classroom:list_teacher')


class TeacherDeleteView(DeleteView):
    model = Teacher
    success_url = reverse_lazy('classroom:list_teacher')
    # modelname_confirm_delete.html


class ThankYouView(TemplateView):
    template_name = 'classroom/thank_you.html'
