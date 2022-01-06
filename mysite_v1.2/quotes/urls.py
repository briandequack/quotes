from django.urls import path
from quotes import views
app_name = "quotes"

urlpatterns = [
    path('author/', views.AuthorListView.as_view(), name='author_list'),
    path('author/<slug:slug>/',views.AuthorDetailView.as_view(), name='author_detail'),
    path('author/add',views.AuthorCreateView.as_view(),name="author_add"),

    path('quote/', views.QuoteListView.as_view(), name='quote_list'),
    path('quote/<int:pk>/',views.QuoteDetailView.as_view(), name='quote_detail'),
    path('add',views.QuoteCreateView.as_view(),name="quote_add"),

    path('', views.RandomView.as_view(), name="random"),


    path('login/', views.user_login,name="login"),

    path('register/', views.register,name="register"),

    path('logout', views.user_logout, name="logout"),

    path('user/<int:pk>/',views.UserDetailView.as_view(), name='user_detail'),

]
