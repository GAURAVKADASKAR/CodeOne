# Generated by Django 5.1 on 2025-05-27 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_codingquestion_sampletestcase'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sampletestcase',
            old_name='question_id',
            new_name='coding_question',
        ),
    ]
