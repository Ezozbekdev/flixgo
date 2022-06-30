from django.contrib.auth import login
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.views import LoginView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.authentication import TokenAuthentication
from .models import Movie, Faq
from .forms import CreateUserForm
from .serializers import MovieSerializer
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class AuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


class Moviedetailapi(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class MovieListApi(ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


# not rest
class Register(FormView):
    template_name = 'all/signup.html'
    form_class = CreateUserForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)


class Login(LoginView):
    template_name = 'all/signin.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')


class Faqs(ListView):
    model = Faq
    context_object_name = 'faqs'
    template_name = 'all/faq.html'


class Main_List(ListView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'all/index.html'


class Movie_View(ListView):
    model = Movie
    context_object_name = 'movie'
    template_name = 'all/catalog2.html'

    def get_context_data(self, **kwargs):
        context = super(Movie_View, self).get_context_data(**kwargs)
        context['count'] = context['movie'].filter(id=False).count()
        search_p = self.request.GET.get('search_p') or ''
        if search_p:
            context['movie'] = context['movie'].filter(
                title__contains=search_p
            )
        context['search_p'] = search_p
        return context


class Movie_Detail(LoginRequiredMixin, DetailView):
    model = Movie
    context_object_name = 'one'
    template_name = 'all/details1.html'


def error404(request):
    return render(request, 'all/404.html')
