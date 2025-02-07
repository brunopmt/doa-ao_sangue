# Generated by Django 4.2.14 on 2024-08-14 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AgendamentoDoacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
                ('tipoSanguineo', models.CharField(max_length=5)),
                ('quantidadeSangueML', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AgendamentoRecepcao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
                ('tipoSanguineo', models.CharField(max_length=5)),
                ('quantidadeSangueML', models.IntegerField()),
                ('recepcaoRealizada', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Doador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('tipoSanguineo', models.CharField(max_length=5)),
                ('cpf', models.CharField(max_length=20)),
                ('rg', models.CharField(max_length=20)),
                ('dataNascimento', models.DateField()),
                ('rua', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='Receptor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('tipoSanguineo', models.CharField(max_length=5)),
                ('cpf', models.CharField(max_length=20)),
                ('rg', models.CharField(max_length=20)),
                ('dataNascimento', models.DateField()),
                ('rua', models.CharField(max_length=50)),
                ('bairro', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=75)),
            ],
        ),
        migrations.CreateModel(
            name='RecepcaoInformada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataVencimento', models.DateField()),
                ('descricao', models.CharField(max_length=150)),
                ('recepcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recepcao_agendada', to='sangue.agendamentorecepcao')),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptor_email', to='sangue.receptor')),
            ],
        ),
        migrations.CreateModel(
            name='DoacaoInformada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataVencimento', models.DateField()),
                ('descricao', models.CharField(max_length=150)),
                ('doacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doacao_agendada', to='sangue.agendamentodoacao')),
                ('doador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doador_email', to='sangue.doador')),
            ],
        ),
        migrations.AddField(
            model_name='agendamentorecepcao',
            name='receptor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptor', to='sangue.receptor'),
        ),
        migrations.AddField(
            model_name='agendamentodoacao',
            name='doador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doador', to='sangue.doador'),
        ),
    ]
