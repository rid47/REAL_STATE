from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *


@api_view(['POST',])
def register_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        print(request.data)
        data = {}
        if serializer.is_valid():
            print("Valid serializer")
            user = serializer.save()
            data['response'] = "Successfully done"
            data['username'] = user.username
        else:
            print(serializer.errors)
            data = serializer.errors

        return Response(data)



