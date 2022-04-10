# Generated by Django 3.2.12 on 2022-04-10 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='학과명')),
                ('head', models.CharField(max_length=20, verbose_name='학과장')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='학번')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('friends', models.ManyToManyField(blank=True, db_table='e_friendship', related_name='_e_student_friends_+', to='e.Student', verbose_name='친구들')),
                ('major', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='e.department', verbose_name='주전공')),
            ],
        ),
    ]