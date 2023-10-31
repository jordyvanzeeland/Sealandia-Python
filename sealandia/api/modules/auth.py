import jwt
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['POST'])
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    User = get_user_model()

    try:
        user = User.objects.get(username=username)

        if user.check_password(password):
            payload = {'id': user.id, 'username': user.username, 'email': user.email}
            jwt_token = {'token': jwt.encode(payload, 'secret', algorithm='HS256')}
            return JsonResponse({
                "user": payload,
                "token": jwt_token["token"]})
        else:
            return JsonResponse({'error': 'Wrong credentials'})
    except User.DoesNotExist:
        return JsonResponse({'error': 'User does not exist'})