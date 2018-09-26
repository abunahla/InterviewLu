from django.conf.urls import url
from profiles import views as profiles_views

from . import views


urlpatterns = [
    url(r"^signup/$", profiles_views.signup, name="account/signup"),

    url(r"^login/$", profiles_views.login, name="account/login"),
    url(r"^logout/$", profiles_views.logout, name="account/logout"),

    url(r"^password/change/$", profiles_views.password_change,
        name="account_change_password"),
    url(r"^password/set/$", profiles_views.password_set, name="account/set_password"),

    url(r"^inactive/$", profiles_views.account_inactive, name="account/inactive"),

    # E-mail
    url(r"^email/$", profiles_views.email, name="account/email"),
    url(r"^confirm-email/$", profiles_views.email_verification_sent,
        name="account/email_verification_sent"),
    url(r"^confirm-email/(?P<key>[-:\w]+)/$", profiles_views.confirm_email,
        name="account/confirm_email"),

    # password reset
    url(r"^password/reset/$", profiles_views.password_reset,
        name="account/reset_password"),
    url(r"^password/reset/done/$", profiles_views.password_reset_done,
        name="account/reset_password_done"),
    url(r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        profiles_views.password_reset_from_key,
        name="account/reset_password_from_key"),
    url(r"^password/reset/key/done/$", profiles_views.password_reset_from_key_done,
        name="account/reset_password_from_key_done"),

]
