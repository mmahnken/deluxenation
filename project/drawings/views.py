from django.shortcuts import render
from django.views import generic
from .models import Notebook, Drawing
from .forms import NotebookCreateForm

# Create your views here.

class HomepageView(generic.TemplateView):
    """Deluxe Nation homepage"""

    template_name = "drawings/homepage.html"


    def get_context_data(self, **kwargs):
        """Add data."""

        max_num = 5
        context = super(HomepageView, self).get_context_data()
        context['notebooks'] = \
            (Notebook
             .objects
             # .select_related('drawing')
             .order_by('-drawn_at')
             )[:max_num]

        return context


class NotebookView(generic.DetailView):
    """Notebook plus all drawings of notebook"""

    template_name = "drawings/notebook_detail.html"
    queryset = Notebook.objects


class NotebookCreateView(generic.CreateView):
    """Add a notebook and all of its drawings in one go."""

    model = Notebook
    form_class = NotebookCreateForm
    # fields = ['id', 'title', 'description', 'front_cover', 'back_cover', 'drawn_at']
    template_name = 'drawings/notebook_create.html'
    headline = "Upload a Notebook"

    form_invalid_message = "Please correct the error(s)."
    form_valid_message = "Information saved."

    def form_valid(self, form):
        self.object = form.save()
        drawings = form.files.getlist('drawings')
        if drawings:
            for drawing in drawings:
                name = drawing.name.split('.')[0]
                first_four_letters = "".join(drawing.name.split('.'))
                first_four_letters = "".join(first_four_letters.split())[:3]
                Drawing.objects.create(notebook=self.object, title=name, image=drawing, id=first_four_letters)

        return super(NotebookCreateView, self).form_valid(form)

