# Generated by Django 2.0.3 on 2018-10-25 20:52

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20181026_0047'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('contact_no', models.CharField(max_length=10)),
                ('dept', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, max_length=50, null=True, upload_to='image/%Y/%m/%d/')),
                ('address', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=50)),
                ('mother_name', models.CharField(max_length=50)),
                ('mobile_no', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(9999999999), django.core.validators.MinValueValidator(1)])),
                ('parent_occu', models.CharField(max_length=50)),
                ('parent_income', models.CharField(max_length=50)),
                ('parent_qual', models.CharField(max_length=50)),
                ('current_cgpa', models.DecimalField(decimal_places=7, max_digits=10)),
                ('avg_cgpa', models.DecimalField(decimal_places=7, max_digits=10)),
                ('ssc_marks', models.DecimalField(decimal_places=7, max_digits=10)),
                ('hsc_marks', models.DecimalField(decimal_places=7, max_digits=10)),
                ('stu_ach', models.CharField(max_length=50)),
                ('created', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='uploaded_at',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 26, 2, 22, 44, 273622)),
        ),
    ]
