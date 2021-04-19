from django.urls import path

from . import views

app_name = 'appweb'
urlpatterns = [
    # name dung cho viec goi duong dan trong html, vd viewdb se duoc thay the bang duong dan viewDB
    path('qs/<int:question_id>', views.detailQuestion, name='detqs'),
    path('as', views.answer, name='answer'),
    path('viewDB', views.viewDB, name='viewdb'),
    path('testAddForm', views.add_post, name='addFormModels'),
    path('testEmailForm', views.email_handler, name='emailForm'),
    path('demoCBV', views.IndexClass.as_view(), name='demo'),
    path('login/', views.LoginClass.as_view(), name='login'),
    path('afterLI', views.ViewUser.as_view(), name='afterLI'),
    path('requiredLIdeco', views.demoDecorators, name='requiredLIdeco'),
    path('requiredLImixin', views.DemoLoginRequiredMixin.as_view(), name='requiredLImixin')
]