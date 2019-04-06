# Generated by Django 2.1.7 on 2019-04-03 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chamado', '0002_auto_20190402_1421'),
        ('orgao', '0001_initial')
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chamados',
            options={'verbose_name': 'Chamado', 'verbose_name_plural': 'Chamados'},
        ),
        migrations.AlterField(
            model_name='chamados',
            name='idEvento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgao.Eventos', verbose_name='SERVIÇO'),
        ),
        migrations.AlterField(
            model_name='chamados',
            name='idStatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgao.Status', verbose_name='STATUS'),
        ),
    ]