# Generated by Django 4.1.3 on 2024-09-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_alter_course_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='description_summernote',
            field=models.CharField(default='', max_length=50000),
        ),
    ]