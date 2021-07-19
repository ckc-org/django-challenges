from django.contrib.auth import authenticate, login, get_user_model
from rest_framework import views, status, mixins
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from users.serializers import LoginSerializer, UserSerializer

User = get_user_model()


# TODO: Add to api docs ??
class LoginView(views.APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=self.request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            email=serializer.validated_data.get('email'),
            password=serializer.validated_data.get('password')
        )

        if user is not None:
            # Set expiry (in seconds) BEFORE inactivity logs you out.
            if serializer.validated_data['remember_me']:
                expiry = 60 * 60 * 24 * 7 * 2  # 2 weeks
            else:
                expiry = 0  # Session only cookie
            request.session.set_expiry(expiry)  # set_expiry must be called before login!

            login(request, user)

            return Response(status=status.HTTP_200_OK)
        else:
            raise ValidationError({"non_field_errors": ["Incorrect login information."]})


class UserViewSet(
    mixins.ListModelMixin,
    GenericViewSet,
):
    permission_classes = []
    queryset = User.objects.all().prefetch_related('companies__addresses')
    serializer_class = UserSerializer
