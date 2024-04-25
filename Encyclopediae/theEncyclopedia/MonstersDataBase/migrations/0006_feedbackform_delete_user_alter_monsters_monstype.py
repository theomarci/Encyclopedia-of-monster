# Generated by Django 5.0.2 on 2024-04-12 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MonstersDataBase', '0005_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('place', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='monsters',
            name='monsType',
            field=models.CharField(choices=[('1', 'Mammal'), ('2', 'Bird')], max_length=20),
        ),
    ]
