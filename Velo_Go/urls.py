
from django.contrib import admin
from django.urls import path

from Velo_Go import views

urlpatterns = [
   path('login/',views.login),

    path('login_post/',views.login_post),

    path('admin_change_password/', views.admin_change_password),

    path('admin_change_password_post/', views.admin_change_password_post),

    path('admin_driver_review/', views.admin_driver_review),

    path('driver_review/',views.driver_review),

    path('admin_view_app_ratingandreview/',views.admin_view_app_ratingandreview),

    path('view_app_rating_and_review/', views.view_app_rating_and_review),

    path('admin_view_approved_drivers/', views.admin_view_approved_drivers),

    path('view_approved_drivers/', views.view_approved_drivers_post),

    path('admin_view_driver_complaints/', views. admin_view_driver_complaints),

    path('view_driver_complaints/', views.view_driver_complaints),
    path('reply_post/', views.reply_post),
    path('admin_reply/<id>', views.admin_reply),

    path('admin_view_monthly_payments_from_drivers/', views.admin_view_monthly_payments_from_drivers),

    path('view_monthly_payments_from_drivers/',views.view_monthly_payments_from_drivers),

    path('admin_view_pending_drivers/',views.admin_view_pending_drivers),
    path('view_pending_drivers/',views.view_pending_drivers),

    # path('admin_view_rejected_drivers/', views.admin_view_rejected_drivers),
    #
    # path(' view_rejected_drivers/', views. view_rejected_drivers),

    path('view_reject_driver/', views.view_reject_driver),
    path('view_reject_driver_post/', views.view_reject_driver_post),
    path('admin_view_user/', views.admin_view_user),

    path('view_user/', views.view_user),

    path('admin_home/',views.admin_home),

    path('approve_drivers/<id>',views.approve_drivers),

    path('reject_drivers/<id>', views.reject_drivers),

    path('DriverLogin/', views.DriverLogin),
    path('driver_Signup/', views.driver_Signup),
    path('DriverChangepasswd/', views.DriverChangepasswd),
    path('DriversViewProfile/', views.DriversViewProfile),
    path('DriversEditProfile/', views.DriversEditProfile),
    path('Driver_edit_profile_post/', views.Driver_edit_profile_post),
    path('AddVehicle/', views.AddVehicle),
    path('DriverViewVehicle/', views.DriverViewVehicle),
    path('DriverEditVehicle/', views.DriverEditVehicle),
    path('EditVehicle_post/', views.EditVehicle_post),
    path('Driver_Add_Seat/', views.Driver_Add_Seat),
    path('Driver_view_seats/', views.Driver_view_seats),
    path('Driver_edit_seats/', views.Driver_edit_seats),
    path('Driver_edit_seats_post/', views.Driver_edit_seats_post),
    path('Driver_view_allocated_booking/', views.Driver_view_allocated_booking),
    path('Driver_otp_Verification/', views.Driver_otp_Verification),

]
