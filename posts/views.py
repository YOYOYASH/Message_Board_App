from django.views import generic
from .models import Post


class HomePageView(generic.ListView):
    model = Post
    template_name = 'home.html'
