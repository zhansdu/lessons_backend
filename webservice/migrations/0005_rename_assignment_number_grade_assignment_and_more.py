# Generated by Django 4.1.6 on 2023-03-14 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0004_alter_grade_assignment_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='assignment_number',
            new_name='assignment',
        ),
        migrations.RenameField(
            model_name='grade',
            old_name='stud_id',
            new_name='student',
        ),
    ]
