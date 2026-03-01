from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Student
from .forms import StudentForm

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    ordering = ['roll_number']

class StudentCreateView(SuccessMessageMixin, CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')
    success_message = "Student record created successfully!"

class StudentUpdateView(SuccessMessageMixin, UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('student_list')
    success_message = "Student record updated successfully!"

class StudentDeleteView(SuccessMessageMixin, DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
    success_message = "Student record deleted successfully!"