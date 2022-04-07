from django.contrib import admin
from django.urls import *
from database.views_folder.basic_views import *
from database.views_folder.student_views import *
from database.views_folder.advisor_views import *
from database.views_folder.caretaker_views import * 
import database.views_folder.department_views as clr 
import database.views_folder.pgblock_views as pgb 
import database.views_folder.registrar_views as reg 
from django.conf.urls import *
import notifications.urls
from parivahan_gndec import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [ 
	path('admin/',admin.site.urls),
	path('select2/', include('django_select2.urls')),
	url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
	url(r'^tinymce/', include('tinymce.urls')),

	path('',home_view),
	path('login/',login),
	path('add/student/',add_new_student),
	path('add/care_taker/', add_new_care_taker),
	path('add/advisor/', add_new_advisor),

	path('portal/student/<str:urno>/apply_bus_pass/', prtc_form_application),
	path('portal/student/<str:urno>/', student_navbar),
	path('portal/student/<str:urno>/view_details/', student_details),
	path('portal/student/<str:urno>/notification/', display_notifications.as_view()),
	path('portal/student/<str:urno>/complaint_advisor/', complaint_advisor),

	path('portal/advisor/<str:urno>/', adv_navbar),
	path('portal/advisor/<str:urno>/view_details/', advisor_details),
	path('portal/advisor/<str:advisor>/students/', StudentListView.as_view(), name = "student-list"),
	path('portal/advisor/<str:advisor>/students/<int:urno>/', StudentDetailView, name = "student-detail"),
	path('portal/advisor/<str:advisor>/applications/recommended/', recommended_application_view.as_view(), name = "recommended_appls_list_adv"),
	path('portal/advisor/<str:advisor>/applications/recommended/<str:appid>/accept/', accept_form_application),
	path('portal/advisor/<str:advisor>/applications/accepted/', accepted_application_view.as_view()),
	path('portal/advisor/<str:advisor>/applications/recommended/<str:appid>/reject/', reject_form_application),
	path('portal/advisor/<str:advisor>/applications/rejected/', rejected_application_view.as_view()),
	
	path('portal/caretaker/<str:urno>/', crt_navbar),
	path('portal/caretaker/<str:urno>/view_details/', caretaker_details),
	path('portal/caretaker/<str:crt>/students/', stdlist.as_view(), name = "hostel-std-list"),

	path('portal/department/<str:urno>/', clr.dept_navbar),
	path('portal/department/<str:urno>/details/', clr.dept_details),
	path('portal/department/<str:deptid>/applications/recommended/', clr.recommended_application_view.as_view(), name = "recommended_appls_list_dept"),	
	path('portal/department/<str:deptid>/applications/recommended/<str:appid>/accept/', clr.accept_form_application),
	path('portal/department/<str:deptid>/students/', clr.StudentListView.as_view(), name = "student-list-of-dept"),
	path('portal/department/<str:deptid>/students/<int:urno>/', clr.StudentDetailView, name = "student-detail"),
	path('portal/department/<str:deptid>/advisors/', clr.AdvisorListView.as_view(), name = "student-list-of-dept"),
	path('portal/department/<str:deptid>/advisors/<str:advid>/', clr.AdvisorDetailView, name = "student-detail"),
	path('portal/department/<str:deptid>/applications/accepted/', clr.accepted_application_view.as_view()),
	path('portal/department/<str:deptid>/applications/rejected/', clr.rejected_application_view.as_view()),	

	path('portal/academics/department/<str:empid>/',pgb.pgb_navbar),
	path('portal/academics/department/<str:empid>/applications/recommended/',pgb.recommended_application_view.as_view(), name = "recommended_appls_list_pgb"),
	path('portal/academics/department/<str:empid>/applications/recommended/<str:appid>/accept/', pgb.accept_form_application),			

	path('portal/registrar/<str:uid>/', reg.reg_navbar),
	path('portal/registrar/<str:uid>/applications/recommended/', reg.recommended_application_view.as_view()),
	path('portal/registrar/<str:uid>/applications/recommended/<str:appid>/generate/pdf/', reg.GeneratePdf.as_view()),			
]


 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)