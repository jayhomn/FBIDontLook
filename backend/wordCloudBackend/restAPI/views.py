# Create your views here.
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import piazza_api as p


from .serializers import HeroSerializer, UserSerializer
from .models import Hero, UserProfile


class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all().order_by('userName')
    serializer_class = UserSerializer


@api_view(['GET', 'PUT'])
def userRequest(request):
    """
    Retrieve, update or delete a code snippet.
    """
    user = UserProfile
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            response = p.login(request.data['userName'], request.body['password'])
            serializer.data['listCourses'] = response
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)