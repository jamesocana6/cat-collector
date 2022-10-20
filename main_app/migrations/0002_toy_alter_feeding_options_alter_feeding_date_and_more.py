# Generated by Django 4.1.2 on 2022-10-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Toy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("color", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(name="feeding", options={"ordering": ["-date"]},),
        migrations.AlterField(
            model_name="feeding",
            name="date",
            field=models.DateField(verbose_name="Feeding Date"),
        ),
        migrations.AddField(
            model_name="cat",
            name="toys",
            field=models.ManyToManyField(to="main_app.toy"),
        ),
    ]
