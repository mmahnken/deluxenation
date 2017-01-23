from django.views import generic

from .forms import NotebookCreateForm
from .models import Notebook, Drawing, Group
from .mixins import HybridListView


class HomepageView(generic.TemplateView):
    """Deluxe Nation homepage"""

    template_name = "drawings/homepage.html"


    def get_context_data(self, **kwargs):
        """Add data."""

        context = super(HomepageView, self).get_context_data()

        context['drawings'] = Drawing.objects.all()[:40]

        return context

class NotebookListView(generic.TemplateView):  # refactor this into a hybrid list view?
    """Deluxe Nation homepage"""

    template_name = "drawings/notebooks.html"


    def get_context_data(self, **kwargs):
        """Add data."""

        max_num = 5
        context = super(NotebookIndexView, self).get_context_data()
        context['notebooks'] = \
            (Notebook
             .objects
             # .select_related('drawing')
             .order_by('-drawn_at')
             )[:max_num]

        return context

class NotebookListJSONView(HybridListView):

    model = Notebook


class NotebookView(generic.DetailView):
    """Notebook plus all drawings of notebook"""

    template_name = "drawings/notebook_detail.html"
    queryset = Notebook.objects


class NotebookCreateView(generic.CreateView):
    """Add a notebook and all of its drawings in one go."""

    model = Notebook
    form_class = NotebookCreateForm
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
                first_ten_letters = "".join(drawing.name.split('.'))
                first_ten_letters = "".join(first_ten_letters.split())[:9]
                Drawing.objects.create(notebook=self.object, title=name, image=drawing, id=first_ten_letters)

        return super(NotebookCreateView, self).form_valid(form)


class GroupListView(HybridListView):
    """A list of groups, rendered in HTML or JSON."""

    model = Group
    template_name = "drawings/groups.html"

class BulkDrawingCreateView(generic.TemplateView):
    """Show the page with all the Javascript for bulk adding drawings."""

    template_name = "drawings/bulk-add.html"


