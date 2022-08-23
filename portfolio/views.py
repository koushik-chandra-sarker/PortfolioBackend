from rest_framework import generics
from rest_framework.response import Response

from author.models import User
from portfolio.serializers.serializers import AllData
from django.utils.translation import gettext as _


class InfoByLoggedInUserApi(generics.RetrieveAPIView):
    # queryset = User.objects.all()
    serializer_class = AllData

    def get_queryset(self):
        try:
            return User.objects.get(username=self.kwargs['username'])
        except User.DoesNotExist:
            return None

    def retrieve(self, request, *args, **kwargs):
        if self.get_queryset():
            return Response(self.get_serializer(self.get_queryset()).data)
        else:
            return Response({'error': _('User not found')})
