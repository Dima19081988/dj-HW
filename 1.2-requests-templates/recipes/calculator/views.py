from django.http import HttpResponse
from django.shortcuts import render

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

def recipe_view(request, dish):
	recipe_data = DATA.get(dish)
	if not recipe_data:
		return HttpResponse("Такого рецепта нет", status=404)

	servings = request.GET.get("servings", 1)
	try:
		servings = int(servings)
		if servings <= 0:
			servings = 1
	except ValueError:
		servings = 1

	scaled_recipe = {}
	for ingredient, amount in recipe_data.items():
		scaled_recipe[ingredient] = amount * servings

	context = {
		"recipe": scaled_recipe
	}

	return render(request, "calculator/index.html", context)


