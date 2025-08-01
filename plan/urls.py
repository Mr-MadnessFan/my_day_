from django.urls import path
from plan.views import detail_page, done_page, not_done_page, CreatePlanView, DeletePlanView, UpdatePlanView

urlpatterns = [
    path('', not_done_page, name='not_done_planes'),
    path('done_plans/', done_page, name='done_planes'),
    path('create/', CreatePlanView.as_view(), name='create_page'),
    path('/<slug:slug>/', detail_page, name='details'),
    path('/<slug:slug>/delete/', DeletePlanView.as_view(), name='delete_page'),
    path('/<slug:slug>/update/', UpdatePlanView.as_view(), name="update_page"),
]