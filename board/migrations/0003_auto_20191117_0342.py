# Generated by Django 2.2.7 on 2019-11-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20191117_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='author',
            field=models.CharField(max_length=50),
        ),
    ]