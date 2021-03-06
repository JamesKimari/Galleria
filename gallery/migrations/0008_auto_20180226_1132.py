# Generated by Django 2.0.2 on 2018-02-26 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20180226_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Illustrations', 'Illustrations'), ('Interior', 'Interior'), ('Random', 'Random'), ('Siberian', 'Siberian'), ('Wakanda', 'Wakanda')], max_length=15),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(choices=[('Poka Universe', 'Poka Universe'), ('Singapore', 'Singapore'), ('Nairobi, Kenya', 'Nairobi, Kenya'), ('Siberia', 'Siberia'), ('Wakanda', 'Wakanda')], max_length=20),
        ),
    ]
