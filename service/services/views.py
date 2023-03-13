from django.db.models import Prefetch, F
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from services.models import Subscription
from services.serializer import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.objects.select_related('plan', 'service').prefetch_related(Prefetch(
        'client', queryset=Client.objects.select_related('user').only('company_name', 'user__email')
        )
    ).annotate(price=F('service__full_price') -
                     F('service__full_price') * F('plan__discount_percent') / 100.00)
    serializer_class = SubscriptionSerializer
