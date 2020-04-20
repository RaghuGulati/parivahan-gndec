from django.contrib import admin
from django.urls import path
from database.views_folder.basic_views import *
from database.views_folder.student_views import *
from database.views_folder.advisor_views import *
from database.views_folder.caretaker_views import * 
from django.conf.urls import include

urlpatterns = [ 
	path('admin/',admin.site.urls),
	path('select2/', include('django_select2.urls')),
	path('',home_view),
	path('add/student/',add_new_student),
	path('add/care_taker/', add_new_care_taker),
	path('add/advisor/', add_new_advisor),
	path('portal/student/apply_bus_paas/<str:urno>/', prtc_form_application),
	path('portal/student/<str:urno>/', student_navbar),
	path('portal/student/view_details/<str:urno>/', student_details),

	path('portal/advisor/<str:urno>/', adv_navbar),
	path('portal/advisor/<str:urno>/view_details/', advisor_details),
	path('portal/advisor/<str:advisor>/students/', StudentListView.as_view(), name = "student-list"),
	path('portal/advisor/<str:advisor>/students/<int:urno>/', StudentDetailView, name = "student-detail"),
	
	path('portal/caretaker/<str:urno>/', crt_navbar),
	path('portal/caretaker/<str:urno>/view_details/', caretaker_details),
	path('portal/caretaker/<str:crt>/students/', stdlist.as_view(), name = "hostel-std-list"),
	path('portal/caretaker/<str:crt>/applications/recommended/', recommended_application_view.as_view(), name = "recommended_appls_list")
]
