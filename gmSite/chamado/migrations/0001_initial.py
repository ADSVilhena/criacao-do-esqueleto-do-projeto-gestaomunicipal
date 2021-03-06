# Generated by Django 2.1.7 on 2019-04-27 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orgao', '0001_initial'),
        ('cadastros', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataAbertura', models.DateField(default=None, verbose_name='ABERTO EM')),
                ('dataFechamento', models.DateField(blank=True, default=None, null=True, verbose_name='CONCLUÍDO EM')),
                ('observacao', models.CharField(max_length=200, verbose_name='OBSERVAÇÃO')),
                ('idEndereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Endereco', verbose_name='ENDEREÇO')),
                ('idEvento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgao.Eventos', verbose_name='SERVIÇO')),
                ('idPessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='PESSOA')),
            ],
            options={
                'verbose_name': 'Chamado',
                'verbose_name_plural': 'Chamados',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50, verbose_name='STATUS')),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.AddField(
            model_name='chamados',
            name='idStatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chamado.Status', verbose_name='STATUS'),
        ),
    ]
