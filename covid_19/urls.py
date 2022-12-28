from django.urls import path
from .views import WorldTotalStatistics,Summary,LocalStatistics,Covid19ListView,Covid19DetailView
urlpatterns=[

    path('',Covid19ListView.as_view()),
    path('<pk>',Covid19DetailView.as_view()),
    path('global/',WorldTotalStatistics.as_view()),
    path('local/',LocalStatistics.as_view()),
    path('summary/',Summary.as_view()),
]