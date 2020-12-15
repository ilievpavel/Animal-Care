from django.shortcuts import render, redirect

from animal.animal_form import AnimalForm
from animal.models import Animal


def persist_animal(request, animal, template_name):
    if request.method == 'GET':
        form = AnimalForm(instance=animal)

        context = {
            'form': form,
            'animal': animal,
        }

        return render(request, f'{template_name}.html', context)
    else:
        form = AnimalForm(request.POST, instance=animal)
        if form.is_valid():
            form.save()
            # Like.objects.filter(pet_id=pet.id) \
            #     .delete()
            return redirect('home')

        context = {
            'form': form,
            'animal': animal,
        }

        return render(request, f'{template_name}.html', context)


def home(request):
    if len(Animal.objects.all()) == 0:
        return render(request, 'home_with_no_animals.html')
    else:
        cured_animals = Animal.objects.filter(is_cured=True)
        sick_animals = Animal.objects.filter(is_cured=False).order_by('priority')

        context = {
            'cured_animals': cured_animals,
            'sick_animals': sick_animals,
        }

        return render(request, 'home_with_sick_and_cured.html', context)


def create_animal(request):
    animal = Animal()
    return persist_animal(request, animal, 'create')


def edit_animal(request, pk):
    animal = Animal.objects.get(pk=pk)
    return persist_animal(request, animal, 'edit')


def delete_animal(request, pk):
    animal = Animal.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'animal': animal,
        }

        return render(request, 'delete.html', context)
    else:
        animal.delete()
        return redirect('home')


def animal_details(request, pk):
    animal = Animal.objects.get(pk=pk)

    context = {
        'animal': animal
    }

    return render(request, 'details.html', context)


def cure_animal(request, pk):
    animal = Animal.objects.get(pk=pk)
    animal.is_cured = True
    animal.save()

    return redirect('home')
