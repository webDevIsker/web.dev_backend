from rest_framework import viewsets, permissions, status
from .serializers import CustomUserSerializer, ProfileCustomUserSerializer, VacationsSerializer, LogListSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .models import Vacations, LogList


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAdminUser]


class ProfileCustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = ProfileCustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        profile = self.get_queryset().get(pk=self.request.user.pk)
        serializer = self.get_serializer(profile)
        return Response({'user': serializer.data})

    # def get_queryset(self):
    #     if self.request.user:
    #         user = get_user_model().objects.filter(pk=self.request.user.pk)
    #         if user is None:
    #             raise exceptions.AuthenticationFailed('Пользователь не найден')
    #         return user


class LogoutView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data['refresh']
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class VacationsViewSet(viewsets.ModelViewSet):
    queryset = Vacations.objects.all()
    serializer_class = VacationsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        vacations = Vacations.objects.get()
        data = request.data

        vacations.vacation_status = data.get("vacation_status", vacations.vacation_status)

        vacations.save()
        serializer = VacationsSerializer(vacations)

        return Response(serializer.data)


class LogListViewSet(viewsets.ModelViewSet):
    queryset = LogList.objects.all()
    serializer_class = LogListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        loglist = LogList.objects.get()
        data = request.data

        loglist.doc_status = data.get("vacation_status", loglist.doc_status)

        loglist.save()
        serializer = VacationsSerializer(loglist)

        return Response(serializer.data)
