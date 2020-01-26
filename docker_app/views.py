from django.views.generic import ListView

from .models import Book, Author


class IndexView(ListView):
    template_name = 'docker_app/index.html'
    model = Book
    context_object_name = 'books'
