# Generated by Django 3.1.7 on 2021-03-13 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offer', '0001_initial'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='fk_offer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='offer.offer'),
        ),
    ]
