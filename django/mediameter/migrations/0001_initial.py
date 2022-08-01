# Generated by Django 4.0.6 on 2022-08-01 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('description', models.TextField()),
                ('pgroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mediameter.parentgroup')),
            ],
        ),
        migrations.CreateModel(
            name='Tweeter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twid', models.CharField(max_length=64, unique=True)),
                ('created_at', models.DateTimeField(max_length=128)),
                ('name', models.CharField(blank=True, max_length=128, null=True)),
                ('handle', models.CharField(blank=True, max_length=64, null=True)),
                ('favorites', models.IntegerField(blank=True, null=True)),
                ('followers', models.IntegerField(blank=True, null=True)),
                ('following', models.IntegerField(blank=True, null=True)),
                ('total_faves', models.IntegerField(blank=True, null=True)),
                ('total_rts', models.IntegerField(blank=True, null=True)),
                ('total_twts', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField()),
                ('webpage', models.URLField(blank=True, null=True)),
                ('pgroup', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mediameter.parentgroup')),
            ],
        ),
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twid', models.CharField(max_length=64)),
                ('created', models.DateTimeField(max_length=128)),
                ('datestamp', models.CharField(blank=True, max_length=16, null=True)),
                ('text', models.CharField(blank=True, max_length=1024, null=True)),
                ('likes', models.IntegerField(blank=True, null=True)),
                ('retweets', models.IntegerField(blank=True, null=True)),
                ('tweeter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mediameter.tweeter')),
            ],
            options={
                'ordering': ['-created'],
                'unique_together': {('twid', 'tweeter')},
            },
        ),
    ]
