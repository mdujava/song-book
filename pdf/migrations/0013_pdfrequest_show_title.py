# Generated by Django 3.2.5 on 2021-08-14 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdf', '0012_pdfrequest_margin'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfrequest',
            name='show_title',
            field=models.BooleanField(default=True, help_text='If the title should be shown ', verbose_name='Show title'),
        ),
    ]
