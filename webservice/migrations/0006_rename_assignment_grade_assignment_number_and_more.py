# Generated by Django 4.1.6 on 2023-03-14 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0005_rename_assignment_number_grade_assignment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='assignment',
            new_name='assignment_number',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='student',
            new_name='stud_id',
        ),
    ]