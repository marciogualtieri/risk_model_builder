# Generated by Django 2.0 on 2017-12-06 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0003_auto_20171206_1925'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='value',
            new_name='option',
        ),
        migrations.AlterField(
            model_name='choice',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='risks.Field'),
        ),
    ]