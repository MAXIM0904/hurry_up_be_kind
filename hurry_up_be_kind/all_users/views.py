from django.views.generic import ListView
from .models import Philantropist, Ward

class AllPhilantropistListView(ListView):
    model = Ward
    template_name = 'forms_html/users_list.html'

