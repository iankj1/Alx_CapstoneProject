from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.utils import timezone
from .models import Task
from .serializers import TaskSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["status", "priority", "due_date"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "due_date", "priority"]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=["patch"], url_path="complete")
    def complete(self, request, pk=None):
        task = self.get_object()
        if task.status == Task.STATUS_COMPLETED:
            return Response({"detail": "Task already completed."}, status=status.HTTP_400_BAD_REQUEST)

        task.status = Task.STATUS_COMPLETED
        task.save()

        # Update user streak logic
        user = request.user
        today = timezone.localdate()

        last_date = user.last_task_completed_date
        if last_date is None:
            user.streak_count = 1
        else:
            yesterday = today - timezone.timedelta(days=1)
            if last_date == today:
                # already updated today (multiple tasks same day) -> no change
                pass
            elif last_date == yesterday:
                user.streak_count += 1
            else:
                user.streak_count = 1
        user.last_task_completed_date = today
        user.save()

        return Response(self.get_serializer(task).data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["get"])
    def streak(self, request):
        user = request.user
        return Response({"streak_count": user.streak_count, "last_task_completed_date": user.last_task_completed_date})
