# Generated by Django 3.2.8 on 2021-10-24 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(help_text='This field is required', max_length=100)),
                ('done', models.BooleanField(default=False)),
            ],
        ),
    ]
