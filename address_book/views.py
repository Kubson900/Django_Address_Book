from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User


def home(request):
    context = {
        'contacts': Contact.objects.all()
    }
    return render(request, 'address_book/home.html', context)


class ContactListView(ListView):
    model = Contact
    template_name = 'address_book/user_contacts.html'
    context_object_name = 'contacts'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Contact.objects.filter(owner=user).order_by('name')


class ContactDetailView(DetailView):
    model = Contact


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['name', 'surname', 'email', 'address']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
