from django.views.generic.base import TemplateResponseMixin, \
    TemplateView

from response import MakoTemplateResponse


class MakoTemplateResponseMixin(TemplateResponseMixin):
    response_class = MakoTemplateResponse


class MakoTemplateView(MakoTemplateResponseMixin, TemplateView):
    pass
