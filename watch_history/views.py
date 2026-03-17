from rest_framework import viewsets
from .models import WatchHistory
from .serializers import WatchHistorySerializer
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class WatchHistoryViewSet(viewsets.ModelViewSet):

    serializer_class = WatchHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return WatchHistory.objects.filter(user=self.request.user)

    # 🎬 CONTINUE WATCHING
    @action(detail=False, methods=["get"])
    def continue_watching(self, request):

        history = self.get_queryset()

        serializer = self.get_serializer(history, many=True)

        return Response(serializer.data)

    # ⏱️ SALVAR PROGRESSO
    @action(detail=False, methods=["post"])
    def save_progress(self, request):

        user = request.user
        movie_id = request.data.get("movie")
        progress = request.data.get("progress")

        if not movie_id or progress is None:
            return Response({"error": "movie and progress are required"}, status=400)

        history, created = WatchHistory.objects.get_or_create(
            user=user,
            movie_id=movie_id
        )

        history.progress = progress
        history.save()

        return Response({"status": "progress saved"})

# Create your views here.
