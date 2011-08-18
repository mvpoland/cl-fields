from django.contrib.admin import FieldListFilter
from django.utils.translation import ugettext_lazy as _

class IsNullFilter(FieldListFilter):
    title = _(u'is null value')

    def __init__(self, field, request, params, model, model_admin, field_path):
        super(IsNullFilter, self).__init__(field,
            request, params, model, model_admin, field_path)
        self.lookup_kwarg = '%s__isnull' % self.field_path
        self.lookup_val = request.GET.get(self.lookup_kwarg, None)

    def used_params(self):
        return [self.lookup_kwarg]

    def choices(self, cl):
        for lookup, title in (
                (None, _('All')),
                ('1', _('Yes')),
                ('0', _('No'))):
            if lookup is None:
                qs_kwarg = {}
            else:
                qs_kwarg = {self.lookup_kwarg: lookup}
            yield {
                'selected': self.lookup_val == lookup,
                'query_string': cl.get_query_string(qs_kwarg, [self.lookup_kwarg]),
                'display': title,
            }
