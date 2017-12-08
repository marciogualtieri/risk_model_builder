# Generated by Django 2.0 on 2017-12-06 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('risks', '0005_auto_20171206_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='choice',
            name='field',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='risks.Field'),
        ),
        migrations.AlterField(
            model_name='field',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterUniqueTogether(
            name='risk',
            unique_together={('name',)},
        ),
        migrations.AddField(
            model_name='field',
            name='risk',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fields', to='risks.Risk'),
        ),
    ]