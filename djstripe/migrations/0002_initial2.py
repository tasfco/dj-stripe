# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-06 20:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('djstripe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='subscriber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='djstripe_customers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='coupon',
            unique_together=set([('stripe_id', 'livemode')]),
        ),
        migrations.AddField(
            model_name='charge',
            name='account',
            field=models.ForeignKey(help_text='The account the charge was made on behalf of. Null here indicates that this value was never set.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='charges', to='djstripe.Account'),
        ),
        migrations.AddField(
            model_name='charge',
            name='customer',
            field=models.ForeignKey(help_text='The customer associated with this charge.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='charges', to='djstripe.Customer'),
        ),
        migrations.AddField(
            model_name='charge',
            name='invoice',
            field=models.ForeignKey(help_text='The invoice this charge is for if one exists.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='charges', to='djstripe.Invoice'),
        ),
        migrations.AddField(
            model_name='charge',
            name='source',
            field=models.ForeignKey(help_text='The source used for this charge.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='charges', to='djstripe.StripeSource'),
        ),
        migrations.AddField(
            model_name='charge',
            name='transfer',
            field=models.ForeignKey(help_text='The transfer to the destination account (only applicable if the charge was created using the destination parameter).', null=True, on_delete=django.db.models.deletion.CASCADE, to='djstripe.Transfer'),
        ),
        migrations.AlterUniqueTogether(
            name='customer',
            unique_together=set([('subscriber', 'livemode')]),
        ),
    ]
