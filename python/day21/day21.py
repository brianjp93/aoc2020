import pathlib
from collections import defaultdict

filename = pathlib.PurePath(pathlib.Path(__file__).parent.absolute(), 'data')
with open(filename) as f:
    data = [x.strip() for x in f.read().strip().splitlines()]
datastring = ''.join(data)

foods = []
all_ingredients = []
ing_dict = defaultdict(lambda: [])
aller_dict = defaultdict(lambda: [])
for i, line in enumerate(data):
    if 'contains' in line:
        p1, p2 = line.split(' (contains ')
        p2 = p2.strip(')').split(',')
        ingredients = set(p1.split())
        allergens = set(x.strip() for x in p2)
        foods.append([ingredients, allergens])
        for ing in ingredients:
            ing_dict[ing].append(i)
            all_ingredients.append(ing)
        for aller in allergens:
            aller_dict[aller].append(i)


count = 0
unknown = set()
for allergen, indexes in aller_dict.items():
    ings = set.intersection(*[foods[x][0] for x in indexes])
    unknown |= ings

no_allergen = set(ing_dict.keys()) - unknown
print(f'Part 1: {sum(all_ingredients.count(x) for x in no_allergen)}')

for food in foods:
    new_ing = set(food[0])
    for ing in food[0]:
        if ing in no_allergen:
            new_ing.remove(ing)
    food[0] = new_ing


possible = {}
for allergen, indexes in aller_dict.items():
    ings = set.intersection(*[foods[x][0] for x in indexes])
    possible[allergen] = ings

while any(len(x) > 1 for x in possible.values()):
    for allergen, ingredients in possible.items():
        if len(ingredients) == 1:
            ing = list(ingredients)[0]
            for other in possible:
                if allergen != other:
                    possible[other] = possible[other] - {ing}

possible = [(a, b.pop()) for a,b in possible.items()]
possible.sort()
canonical = ','.join([x[1] for x in possible])
print(f'Part 2: {canonical}')
