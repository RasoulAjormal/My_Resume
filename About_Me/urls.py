from django.urls import path

from About_Me.views import AboutMeView, portfolio_details, Add_Message

urlpatterns = [
    path('', AboutMeView.as_view(), name='AboutMeUrl'),
    path('portfolio/<portfolio_id>', portfolio_details, name='Portfolio'),
    path('add-message/', Add_Message, name='add-message'),
]
