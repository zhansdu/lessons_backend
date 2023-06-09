# Generated by Django 4.1.6 on 2023-02-28 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('assignment_number', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('stud_id', models.IntegerField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField()),
                ('comment', models.TextField(null=True)),
                ('assignment_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webservice.assignment')),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webservice.student')),
            ],
        ),
    ]
