# Generated by Django 3.2.8 on 2021-11-02 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advisorapi', '0007_advisor_adname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisorbookingtrans',
            name='whichAdvisor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advisorapi.advisor'),
        ),
    ]