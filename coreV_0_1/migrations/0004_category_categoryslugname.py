# Generated by Django 2.1 on 2018-09-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreV_0_1', '0003_auto_20180910_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='categorySlugName',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
