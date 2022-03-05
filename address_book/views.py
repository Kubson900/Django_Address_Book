from django.shortcuts import render, get_object_or_404
from .models import Contact
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
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
    paginate_by = 5

    def get_queryset(self):
        if self.request.method == 'GET':
            user = get_object_or_404(User, username=self.kwargs.get('username'))
            user_contacts = Contact.objects.filter(owner=user)
            sorting_method = self.request.GET.get('sort_by', None)
            if sorting_method is not None:
                user_contacts = user_contacts.order_by(sorting_method)
            return user_contacts


class ContactDetailView(DetailView):
    model = Contact


class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    fields = ['name', 'surname', 'email', 'zip_code', 'city', 'street', 'number1', 'number2']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    fields = ['name', 'surname', 'email', 'zip_code', 'city', 'street', 'number1', 'number2']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.owner:
            return True
        return False


class ContactDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Contact
    success_url = '/'

    def test_func(self):
        contact = self.get_object()
        if self.request.user == contact.owner:
            return True
        return False
