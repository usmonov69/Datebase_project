from django.urls import path
from . import views

urlpatterns = [ 
	path('', views.home, name='home'),
	path('join/', views.join, name='join'),
	path('delete/<int:pk>/', views.MemberDelete.as_view(), name='delete'),
	path('edit/<int:pk>/', views.MemberUpdateView.as_view(), name='edit'),#func
	path('detail/<int:pk>', views.MemberDetailView.as_view(), name='detail'),
	path('about', views.About.as_view(), name='about' )
	
] 

