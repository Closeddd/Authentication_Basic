# Generated by Django 4.1.3 on 2022-12-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_accounts_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
