# Generated by Django 2.2.5 on 2019-09-28 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_number', models.CharField(max_length=10)),
                ('owner_name', models.TextField()),
                ('owner_doc', models.TextField()),
                ('date_issue', models.CharField(max_length=15)),
            ],
        ),
    ]
