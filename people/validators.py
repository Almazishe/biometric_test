from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_int(value):
    try:
        value = int(value)
    except:
        raise ValidationError(
            _('%(value)s can contain only integers'),
            params={'value': value},
        )

def validate_iin(value):
    if len(value) != 12:
        raise ValidationError(
            _('%(value)s\'s length not 12'),
            params={'value': value},
        )