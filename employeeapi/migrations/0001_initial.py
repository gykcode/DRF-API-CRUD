# Generated by Django 4.1.7 on 2023-03-16 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('departmentID', models.AutoField(primary_key=True, serialize=False)),
                ('departmentName', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('employeeID', models.AutoField(primary_key=True, serialize=False)),
                ('employeeName', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('dateOfEmployment', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
