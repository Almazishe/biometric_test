from datetime import datetime
from django.db import models

from .validators import validate_int, validate_iin

class Person(models.Model):
    iin = models.CharField(max_length=12, unique=True, validators=[validate_int, validate_iin])

    @property
    def birth_date(self):
        b_year = int(self.iin[:2])
        b_month = int(self.iin[2:4])
        b_day = int(self.iin[4:6])
        return datetime(b_year, b_month, b_day)
