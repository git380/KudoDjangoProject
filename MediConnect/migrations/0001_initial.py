# Generated by Django 5.0 on 2023-12-21 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('empid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('empfname', models.CharField(max_length=64)),
                ('emplname', models.CharField(max_length=64)),
                ('emppasswd', models.CharField(max_length=256)),
                ('emprole', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicineid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('medicinename', models.CharField(max_length=64)),
                ('unit', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('patfname', models.CharField(max_length=64)),
                ('patlname', models.CharField(max_length=64)),
                ('hokenmei', models.CharField(max_length=64)),
                ('hokenexp', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Tabyouin',
            fields=[
                ('tabyouinid', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('tabyouinmei', models.CharField(max_length=64)),
                ('tabyouinaddres', models.CharField(max_length=64)),
                ('tabyouintel', models.CharField(max_length=13)),
                ('tabyouinshihonkin', models.IntegerField()),
                ('kyukyu', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patid', models.CharField(max_length=64)),
                ('medicineid', models.CharField(max_length=64)),
                ('quantity', models.IntegerField()),
                ('impdate', models.DateField()),
            ],
        ),
    ]