from django.contrib import admin
from django.urls import path, include
from .views import HomepageView, signup, recipeList, RecipeListView, subscriptionPaymentView, subscribeView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomepageView.as_view(), name='homepage'), 
    path('subscribe/payment/', subscriptionPaymentView.as_view(), name='subscribe_payment'),
    path('subscribe/', subscribeView.as_view(), name='subscribe'),
    path('accounts/signup/',  signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('recipe/select/', recipeList, name="recipe_select"), # change this name
    path('recipe/', RecipeListView.as_view(), name="recipeList"),

    #path('login/', auth_views.LoginView.as_view(), name='login'),
    #path('logout/', auth_views.logout, {'template_name': 'core/login.html'}, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)