# Generated by Django 3.1.4 on 2020-12-17 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposal', '0002_proposal_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='status',
            field=models.TextField(choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected')], default='Pending'),
        ),
    ]
