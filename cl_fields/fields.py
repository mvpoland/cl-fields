from django import forms
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.utils import simplejson as json
from django.utils.translation import ugettext_lazy as _


class JSONWidget(forms.Textarea):
    def render(self, name, value, attrs=None):
        if not isinstance(value, basestring):
            value = json.dumps(value, indent=2)
        return super(JSONWidget, self).render(name, value, attrs)


class JSONFormField(forms.CharField):
    def __init__(self, *args, **kwargs):
        if 'widget' not in kwargs:
            kwargs['widget'] = JSONWidget
        super(JSONFormField, self).__init__(*args, **kwargs)

    def clean(self, value):
        if not value:
            return
        try:
            return json.loads(value)
        except Exception, exc:
            raise forms.ValidationError(
                u'JSON decode error: %s' % (unicode(exc),)
            )


class JSONField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = _(u'JSON data')

    def formfield(self, **kwargs):
        if 'form_class' not in kwargs:
            kwargs['form_class'] = JSONFormField
        return super(JSONField, self).formfield(**kwargs)

    def to_python(self, value):
        if isinstance(value, basestring):
            value = json.loads(value)
        return value

    def get_db_prep_save(self, value, connection=None):
        if value is None:
            return None
        return json.dumps(value, cls=DjangoJSONEncoder)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)


try:
    import south
except ImportError:
    pass
else:
    # Since we inherit from a TextField, we don't need to add new rules
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ['^cl_fields.fields.JSONField'])
