# Generated by Django 2.1.5 on 2022-07-19 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reaction_id', models.IntegerField()),
                ('reaction_desc', models.CharField(max_length=1024)),
            ],
        ),
    ]