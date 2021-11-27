from django.shortcuts import render, reverse
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}

def dish_view(request, dish):
    template_name = 'index.html'
    new_data = dict()
    response = request.GET.get('servings', '1').isnumeric()
    for ingredient, amount in DATA.get(dish, {}).items():
        if response:
            new_data[ingredient] = f"{amount * int(request.GET.get('servings', 1)):.1f}"
        else:
            new_data[ingredient] = amount
    context = {
        'recipe': new_data
    }
    return render(request, template_name, context)
