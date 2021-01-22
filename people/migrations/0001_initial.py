# Generated by Django 3.1.5 on 2021-01-22 13:00

from django.db import migrations, models
import people.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iin', models.CharField(max_length=12, validators=[people.validators.validate_int, people.validators.validate_iin])),
            ],
        ),
    ]