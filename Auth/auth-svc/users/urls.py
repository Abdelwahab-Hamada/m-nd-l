from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    Registration,
    Authentication,
    AccessTokenClaiming,
    AccessTokenVerification,
    UserIDClaiming
)

urlpatterns = format_suffix_patterns([
    path('register/',Registration.as_view(),name='register'),
    path('auth/',Authentication.as_view(),name='auth'),
    path('at/',AccessTokenClaiming.as_view(),name='access-token'),
    path('vat/',AccessTokenVerification.as_view(),name='verify-access-token'),
    path('uid/',UserIDClaiming.as_view(),name='user-id'),
    
])