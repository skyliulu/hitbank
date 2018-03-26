# Generated by Django 2.0.3 on 2018-03-25 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
        ('transfer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessAudit',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('password', models.CharField(max_length=64)),
                ('paycode', models.CharField(max_length=6)),
                ('user_ip', models.GenericIPAddressField()),
            ],
        ),
        migrations.CreateModel(
            name='EncryptionAlgorithm',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('pk_algo', models.CharField(max_length=8)),
                ('user_pkey', models.CharField(max_length=64)),
                ('bank_pkey', models.CharField(max_length=64)),
                ('bank_skey', models.CharField(max_length=64)),
                ('sk_algo', models.CharField(max_length=8)),
                ('sym_key', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='LoginAudit',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('password', models.CharField(max_length=64)),
                ('user_ip', models.GenericIPAddressField()),
                ('Algorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='security.EncryptionAlgorithm')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Account')),
            ],
        ),
        migrations.CreateModel(
            name='PayAudit',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('password', models.CharField(max_length=64)),
                ('paycode', models.CharField(max_length=6)),
                ('order_hash', models.CharField(max_length=64)),
                ('pay_info', models.CharField(max_length=128)),
                ('double_sign', models.CharField(max_length=64)),
                ('Algorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='security.EncryptionAlgorithm')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Account')),
                ('serial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.Flow')),
            ],
        ),
        migrations.AddField(
            model_name='businessaudit',
            name='Algorithm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='security.EncryptionAlgorithm'),
        ),
        migrations.AddField(
            model_name='businessaudit',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Account'),
        ),
        migrations.AddField(
            model_name='businessaudit',
            name='serial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transfer.Flow'),
        ),
    ]