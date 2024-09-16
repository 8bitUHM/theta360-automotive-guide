# Generated by Django 4.2.15 on 2024-09-16 09:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_company_connect_alter_company_take_picture_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='extra_detail',
            new_name='additional_details',
        ),
        migrations.AlterField(
            model_name='company',
            name='connect',
            field=models.PositiveSmallIntegerField(default=0, help_text='Connection rating (max 100).', validators=[django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='company',
            name='image',
            field=models.ImageField(help_text='Upload an image of the company.', null=True, upload_to='website.File/bytes/filename/mimetype'),
        ),
        migrations.AlterField(
            model_name='company',
            name='opinion',
            field=models.TextField(help_text='Opinion on the company.'),
        ),
    ]
