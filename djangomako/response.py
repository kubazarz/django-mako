from django.template.response import SimpleTemplateResponse, TemplateResponse

from mako.template import Template

import middleware


class MakoSimpleTemplateResponse(SimpleTemplateResponse):
    def resolve_template(self, template):
        if isinstance(template, Template):
            return template
        elif isinstance(template, list):
            template = template[0]
        return middleware.lookup.get_template(template)

    @property
    def rendered_content(self):
        template = self.resolve_template(self.template_name)
        context = self.resolve_context(self.context_data)
        context_dictionary = {}
        for d in context:
            context_dictionary.update(d)
        content = template.render(**context_dictionary)
        return content


class MakoTemplateResponse(MakoSimpleTemplateResponse, TemplateResponse):
    pass
