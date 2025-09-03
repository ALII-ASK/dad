from django.urls import path
from . import views
urlpatterns=[
    path('compiler/',views.compiler,name="compiler"),
    path('automata/',views.automata,name="automata"),
    path('discrete/',views.discrete,name='discrete'),
    path('microprocessor/',views.microprocessor,name='microprocessor'),
    path('internet/',views.internet,name='internet'),
    path('fundamentals/',views.fundamentals,name='fundamentals'),
    path('softwaretest/',views.softwaretest,name='softwaretest'),
    path('speciallanguage/',views.speciallanguage,name='speciallanguage'),
    path('redirect/', views.subject_page_redirect, name='subject_page_redirect'),
]
