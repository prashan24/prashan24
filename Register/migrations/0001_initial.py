# Generated by Django 3.2.5 on 2022-03-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(default='', max_length=50)),
                ('LastName', models.CharField(default='', max_length=50)),
                ('UserName', models.CharField(default='', max_length=50)),
                ('Email', models.EmailField(default='', max_length=50)),
                ('Country', models.CharField(default='', max_length=50)),
                ('Mobile', models.CharField(default='', max_length=50)),
                ('Password', models.CharField(default='', max_length=50)),
                ('Confirm_Password', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
