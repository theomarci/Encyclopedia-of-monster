# Generated by Django 5.0.2 on 2024-04-12 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonstersDataBase', '0007_alter_monsters_monstype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monsters',
            name='monsType',
            field=models.CharField(choices=[('Mammal', 'Mammal'), ('Bird', 'Bird'), ('Reptilia', 'Reptilia'), ('Fish', 'Fish')], max_length=20),
        ),
    ]
