# Generated by Django 4.1.7 on 2023-04-05 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bibliotheque.category'),
        ),
    ]
