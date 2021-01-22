from datetime import datetime
from dateutil.relativedelta import relativedelta
from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Person
        fields = ('iin', 'age')

    def get_age(self, obj):
        time_difference = relativedelta(datetime.now(), obj.birth_date)
        return time_difference.years % 100
