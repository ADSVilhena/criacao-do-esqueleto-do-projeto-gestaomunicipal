# Generated by Django 2.1.7 on 2019-03-25 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chamado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataAbertura', models.CharField(max_length=10)),
                ('dataFechamento', models.CharField(max_length=10)),
                ('observacao', models.CharField(max_length=200)),
                ('idEndereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Endereco')),
            ],
        ),
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
                ('idOrgao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Orgao')),
            ],
        ),
        migrations.CreateModel(
            name='Lotacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idOrgao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Orgao')),
                ('idPessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoLotacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='lotacao',
            name='idTipoLotacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.TipoLotacao'),
        ),
        migrations.AddField(
            model_name='chamado',
            name='idEvento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Eventos'),
        ),
        migrations.AddField(
            model_name='chamado',
            name='idPessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Pessoa'),
        ),
        migrations.AddField(
            model_name='chamado',
            name='idStatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastros.Status'),
        ),
    ]