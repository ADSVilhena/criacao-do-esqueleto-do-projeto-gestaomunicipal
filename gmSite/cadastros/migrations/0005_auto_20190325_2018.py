# Generated by Django 2.1.7 on 2019-03-26 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_auto_20190325_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chamado',
            name='dataAbertura',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='dataFechamento',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='chamado',
            name='observacao',
            field=models.CharField(max_length=200),
        ),
    ]