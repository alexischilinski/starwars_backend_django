# Generated by Django 3.0.2 on 2020-02-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('starwarsapi', '0026_auto_20200206_1823'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercharacter',
            name='category',
            field=models.CharField(default='character', max_length=200),
        ),
        migrations.AddField(
            model_name='userplanet',
            name='category',
            field=models.CharField(default='planet', max_length=200),
        ),
        migrations.AddField(
            model_name='userwildlife',
            name='category',
            field=models.CharField(default='wildlife', max_length=200),
        ),
        migrations.AlterField(
            model_name='usercharacter',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userplanet',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='userwildlife',
            name='image',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
