from rest_framework import viewsets
from .models import WatchHistory
from .serializers import WatchHistorySerializer
from rest_framework.decorators import action
from rest_framework.response import Response


class WatchHistoryViewSet(viewsets.ModelViewSet):

    queryset = WatchHistory.objects.all()

    serializer_class = WatchHistorySerializer

    @action(detail=False, methods=["get"])
    def continue_watching(self, request):

        user = request.user

        history = WatchHistory.objects.filter(user=user)

        serializer = WatchHistorySerializer(history, many=True)

        return Response(serializer.data)

# Create your views here.
