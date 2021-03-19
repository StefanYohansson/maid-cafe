# Generated by Django 3.0.6 on 2020-05-14 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0016_merge_20200513_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='client',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='requestmenu',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cafe.Menu'),
        ),
        migrations.AlterField(
            model_name='requestmenu',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cafe.Request'),
        ),
    ]