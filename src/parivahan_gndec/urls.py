from django.contrib import admin
from django.urls import path
from database.views import *

urlpatterns = [ 
	path('admin/',admin.site.urls),
	path('',home_view),
	path('add/student/',add_new_student),
	path('add/care_taker/', add_new_care_taker),
	path('add/advisor/', add_new_advisor),
	path('apply/bus/paas/<str:urno>/', prtc_form_application),
]

