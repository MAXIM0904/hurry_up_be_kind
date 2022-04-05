from django.views.generic import ListView
from .models import Philantropist

class AllPhilantropistListView(ListView):
    model = Philantropist
    template_name = 'forms_html/users_list.html'

