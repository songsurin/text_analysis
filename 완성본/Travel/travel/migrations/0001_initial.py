# Generated by Django 4.2 on 2023-06-02 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Chat",
            fields=[
                ("idx", models.AutoField(primary_key=True, serialize=False)),
                ("query", models.CharField(max_length=500)),
                ("answer", models.CharField(max_length=1000)),
                ("intent", models.CharField(max_length=50)),
            ],
        ),
    ]
