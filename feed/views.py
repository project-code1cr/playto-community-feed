from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.timezone import now
from datetime import timedelta
from django.db.models import Sum

from .models import Post, KarmaEvent
from .serializers import PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


@api_view(['GET'])
def leaderboard(request):
    cutoff = now() - timedelta(hours=24)

    data = (
        KarmaEvent.objects
        .filter(created_at__gte=cutoff)
        .values('user__username')
        .annotate(total_karma=Sum('points'))
        .order_by('-total_karma')[:5]
    )

    return Response(data)
