from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView
from django.views.generic.edit import UpdateView
from .forms import *
from .models import *


class FoodItemCreateView(LoginRequiredMixin, CreateView):
    model = FoodItem
    template_name = 'foodItem_create.html'
    fields = "__all__"
    success_url = reverse_lazy('profile')


@login_required(login_url='login')
def select_food_create_view(request):
    usernow = CustomUser.objects.get(id=request.user.id)
    form = SelectFoodForm(request.user, instance=usernow)
    food_list = FoodItem.objects.filter(person=request.user)
    if food_list.count() == 0:
        f1 = FoodItem(name='pizza',
                      calorie=239, person=request.user)
        f1.save()
        f1 = FoodItem(name='ghorme Sabzi',
                      calorie=208, person=request.user)
        f1.save()
        f1 = FoodItem(name='gheme',
                      calorie=130, person=request.user)
        f1.save()
        f1 = FoodItem(name='pasta',
                      calorie=265, person=request.user)
        f1.save()
        f1 = FoodItem(name='zeresh polo ba morgh',
                      calorie=155, person=request.user)
        f1.save()
        f1 = FoodItem(name='sabzi polo ba mahi',
                      calorie=42, person=request.user)
        f1.save()
        f1 = FoodItem(name='adash polo',
                      calorie=246, person=request.user)
        f1.save()
        f1 = FoodItem(name='dampokhtak',
                      calorie=282, person=request.user)
        f1.save()
        f1 = FoodItem(name='makarani',
                      calorie=143, person=request.user)
        f1.save()
        f1 = FoodItem(name='salad makarani',
                      calorie=59, person=request.user)
        f1.save()

        return redirect('/manage/selectfooditem')
        context = {
            'food_list': food_list,
        }

    if request.method == "POST":
        form = SelectFoodForm(request.user, request.POST, instance=usernow)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            category = form.cleaned_data.get('category')
            quantity = form.cleaned_data.get('quantity')
            person = form.cleaned_data.get('person')
            selectedfood = SelectFoodItem.objects.create(
                name=name, quantity=quantity, category=category, person=person)
            selectedfood.save()
            return redirect('/manage/profile')
        else:
            form = SelectFoodForm(request.user)
    context = {'form': form}
    return render(request, 'addFood_create.html', context)


@login_required(login_url='login')
def profile_view(request):
    usernow = CustomUser.objects.get(id=request.user.id)
    calorielimit = usernow.calorielimit
    selectedfood = SelectFoodItem.objects.filter(person=request.user)

    calorieconsumed = 0
    calorieleft = calorielimit

    for food in selectedfood:
        calorieconsumed += (food.name.calorie * food.quantity)
        calorieleft = calorielimit - calorieconsumed

    context = {'selectedfood': selectedfood, 'Calorielimit': calorielimit, 'Calorieconsumed': calorieconsumed,
               'calorieleft': calorieleft}

    return render(request, 'profile.html', context)


class EditCalorielimitView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    template_name = 'calorielimit_edit.html'
    fields = ['calorielimit']
    success_url = reverse_lazy('profile')


class DeleteFood(LoginRequiredMixin, DeleteView):
    model = SelectFoodItem
    template_name = 'deleteFood.html'
    fields = "__all__"
    success_url = reverse_lazy('profile')