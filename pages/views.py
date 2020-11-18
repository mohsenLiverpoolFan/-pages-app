from django.views.generic import ListView
from .models import Posts


class HomepageView(ListView):
    model=Posts
    template_name='home.html'
    context_object_name='all_posts_list' #new