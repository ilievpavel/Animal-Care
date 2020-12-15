from django.urls import path

from animal.views import home, create_animal, edit_animal, delete_animal, animal_details, cure_animal

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_animal, name='create animal'),
    path('edit/<int:pk>/', edit_animal, name='edit animal'),
    path('delete/<int:pk>/', delete_animal, name='delete animal'),
    path('details/<int:pk>/', animal_details, name='animal details'),
    path('cure/<int:pk>', cure_animal, name='cure animal'),
]

# •	'/' - home page
# •	'/create' – add animal page
# •	'/edit/:id' - edit animal page
# •	'/delete/:id' – confirm delete page
# •	'/details/:id' - animal details page
# •	'/cure/:id' – cure the animal and redirect to home
