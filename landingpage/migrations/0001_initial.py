# Generated by Django 2.2 on 2020-07-23 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diary_editor', models.CharField(max_length=1000)),
                ('diary_completed', models.BooleanField(default=False)),
                ('diary_time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]