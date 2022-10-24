from django.urls import path
from ads.views import SelectionCreateView, SelectionListView, SelectionDetailView, SelectionDeleteView, SelectionUpdateView


urlpatterns = [
    path('', SelectionListView.as_view(), name='selection_list'),
    path('create/', SelectionCreateView.as_view(), name='selection_create'),
    path('<int:pk>/', SelectionDetailView.as_view()),
    path('<int:pk>/update/', SelectionUpdateView.as_view()),
    path('<int:pk>/delete/', SelectionDeleteView.as_view()),
]