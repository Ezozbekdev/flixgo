from django.urls import path, include
from .views import Movie_View, Movie_Detail, Main_List, Faqs, error404, Login, Register
from django.contrib.auth.views import LogoutView
from .views import MovieListApi, Moviedetailapi, AuthToken
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='flixgo',
        default_version='v1.1.0',
        description='This documentation',
        contact=openapi.Contact(email="ezozbekh8@gmail.com"),
        license=openapi.License(name="FLX Licens"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register('movie-api', MovieListApi)
router.register('detail-api', Moviedetailapi)

urlpatterns = [
    #documentation
    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='FLX-redoc'),
    # api
    path('list-auth-token/', AuthToken.as_view()),
    path('login-api/', obtain_auth_token),
    path('api/', include(router.urls)),

    path('logout/', LogoutView.as_view(next_page='main'), name='logout'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),

    path('error/404/error/page/404/', error404, name='error'),

    path('movie/help/faq/', Faqs.as_view(), name='faq'),
    path('detail-movie-play/<int:pk>/', Movie_Detail.as_view(), name='detail'),
    path('all/', Movie_View.as_view(), name='movie-a'),
    path('', Main_List.as_view(), name='main'),
]
