from rest_framework import viewsets
from .models import WatchHistory
from .serializers import WatchHistorySerializer


class WatchHistoryViewSet(viewsets.ModelViewSet):

    queryset = WatchHistory.objects.all()

    serializer_class = WatchHistorySerializer
    
# Create your views here.
