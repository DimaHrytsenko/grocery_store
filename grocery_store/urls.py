from django.urls import path

from grocery_store.views import store_homepage, login_page, logout_page, auth_page, employee_page, feedback_page, \
    supplier_info, EmployeeInfoView, GameView, time_encode, FeedbackListView, FeedbackGetView, \
    FeedbackCreateView, FeedbackDeletingView

urlpatterns = [
    path('', store_homepage, name='store_homepage'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page, name='logout_page'),
    path('secret/', auth_page, name='auth_page'),
    path('employee/', employee_page, name='employee_page'),
    path('feedback/', feedback_page, name='feedback_page'),
    path('supplier_info/', supplier_info, name='supplier_info'),
    path('api/employee_json/', EmployeeInfoView.as_view(), name='employee_json'),

    path('api/feedback_sorted/', FeedbackListView.as_view(), name='feedback_sorted'),
    path('api/feedback_id/<int:pk>/', FeedbackGetView.as_view(), name='feedback_id'),
    path('api/feedback_add/', FeedbackCreateView.as_view(), name='feedback_add'),
    path('api/feedback_delete/<int:pk>/', FeedbackDeletingView.as_view(), name='feedback_delete'),

    path('api/game/<str:user>/', GameView.as_view(), name='game'),
    path('api/v1/time/', time_encode, name='time'),
]
