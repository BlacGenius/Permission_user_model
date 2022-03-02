from django.shortcuts import render
from mainapp.serializers import PostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from mainapp.models import Post
from rest_framework import generics, viewsets
from mainapp.permissions import IsAdminUserOrReadOnly


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAdminUserOrReadOnly, )


class PostAPIUpdate(APIView):
    """
    здесь я реализовал ограничение при котором изменять запись может только тот кто создал эту запись
    """
    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)# здесь я полючаю id записи
        if not pk:
            return Response({"error": "Этой записи не существует"})
        instance = Post.objects.get(pk=pk)
        if request.user == instance.user: # здесь я проверяю является ли пользователь который хочет изменить эту запись его создателем
            serializer = PostSerializer(data=request.data, instance=instance)
            serializer.is_valid()
            serializer.save()
            return Response({"title": serializer.data})
