# Generated by Django 2.1 on 2018-09-10 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coreV_0_1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='stores',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='category',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='store',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='category',
        ),
        migrations.RemoveField(
            model_name='offer',
            name='store',
        ),
        migrations.RemoveField(
            model_name='payout',
            name='store',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Deal',
        ),
        migrations.DeleteModel(
            name='Offer',
        ),
        migrations.DeleteModel(
            name='Payout',
        ),
        migrations.DeleteModel(
            name='Store',
        ),
    ]
