from django.http import JsonResponse
from django.core import serializers

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

