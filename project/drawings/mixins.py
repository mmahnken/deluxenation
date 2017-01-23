from django.http import JsonResponse
from django.core import serializers
from django.views import generic


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )                               # why doesn't this set content type = json? must parse on front end.

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """

        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        data = serializers.serialize("json", context.get('object_list'))

        return {'data': data}


class HybridListView(JSONResponseMixin, generic.ListView):
    """A generic list view that can render in HTML or JSON."""

    def render_to_response(self, context):
        # Look for a 'format=json' GET argument
        if self.request.GET.get('format') == 'json':
            return self.render_to_json_response(context)
        else:
            return super(HybridListView, self).render_to_response(context)

