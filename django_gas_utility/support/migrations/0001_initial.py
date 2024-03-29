# Generated by Django 3.2.20 on 2023-08-13 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consumer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inquiry_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('open', 'Open'), ('resolved', 'Resolved')], max_length=20)),
                ('subject', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SupportAgent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interaction_date', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('inquiry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.inquiry')),
            ],
        ),
        migrations.AddField(
            model_name='inquiry',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='support.supportagent'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumer.customer'),
        ),
    ]
