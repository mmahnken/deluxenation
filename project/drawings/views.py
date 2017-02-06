from django.views import generic
from django.db.models.functions import ExtractYear

from .forms import NotebookCreateForm
from .models import Notebook, Drawing, Group, ArtistInfo
from .mixins import HybridListView


class HomepageView(generic.TemplateView):
    """Deluxe Nation homepage"""

    template_name = "drawings/homepage.html"


    def get_context_data(self, **kwargs):
        """Add data."""

        context = super(HomepageView, self).get_context_data()

        context['drawings'] = Drawing.objects.all()[:40]

        return context

# class NotebookListView(generic.TemplateView):  # refactor this into a hybrid list view?
#     """Deluxe Nation homepage"""
#
#     template_name = "drawings/notebooks.html"
#
#
#     def get_context_data(self, **kwargs):
#         """Add data."""
#
#         max_num = 5
#         context = super(NotebookIndexView, self).get_context_data()
#         context['notebooks'] = \
#             (Notebook
#              .objects
#              # .select_related('drawing')
#              .order_by('-drawn_at')
#              )[:max_num]
#
#         return context

class NotebookListView(HybridListView):
    """A list of notebooks, rendered in HTML or JSON."""

    model = Notebook
    template_name = 'drawings/notebooks.html'

class DrawingListView(HybridListView):
    model = Drawing
    template_name = 'drawings/drawings.html'

class GroupListView(HybridListView):
    """A list of groups, rendered in HTML or JSON."""

    model = Group
    template_name = "drawings/groups.html"


class NotebookDetailView(generic.DetailView):
    """Notebook plus all drawings of notebook"""

    template_name = "drawings/notebook_detail.html"
    queryset = Notebook.objects

class NotebooksByYearView(generic.TemplateView):

    template_name = "drawings/notebooks_by_year.html"

    def get_context_data(self, **kwargs):
        """Get notebooks grouped by drawn_at year."""

        distinct_years = Notebook.objects.annotate(year=ExtractYear('drawn_at')).values('year').order_by('-year').distinct()

        for y in distinct_years:
            one_nb = Notebook.objects.filter(drawn_at__year=y['year'])[:1].get()
            y['drawing_url'] = one_nb.random_favorite

        return {'data': distinct_years}


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

class ArtistStatementView(generic.ListView):
    model = ArtistInfo
    template_name = 'drawings/artist_info.html'




class BulkDrawingCreateView(generic.TemplateView):
    """Show the page with all the Javascript for bulk adding drawings."""

    template_name = "drawings/bulk-add.html"


