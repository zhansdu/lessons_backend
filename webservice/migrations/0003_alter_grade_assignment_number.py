# Generated by Django 4.1.6 on 2023-03-14 00:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0002_assignment_due_date_assignment_start_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='assignment_number',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webservice.assignment'),
        ),
    ]
