# Generated by Django 4.2.6 on 2023-12-14 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('nickname', models.CharField(max_length=50)),
                ('age', models.PositiveBigIntegerField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
