import random
from bmr import Person
from data.breakfast import BREAKFAST
from data.maindishes import MAINDISHES
from data.snacks import SNACKS


def _shuffle(d):
    items = list(d.items())
    random.shuffle(items)
    return dict(items)


def _pick_meals(data, keys, partitions, target_cals):
    """
    Picks `partitions` items from `data` whose calorie keys are closest
    to an even split of `target_cals`.
    """
    keys = [int(k) for k in keys]
    cals_each = round(target_cals / partitions)
    result = []
    for _ in range(partitions):
        if not keys:
            break
        closest = min(keys, key=lambda x: abs(x - cals_each))
        item = dict(data[str(closest)])
        item["cals"] = str(closest)
        result.append(item)
        keys.remove(closest)
    return result


def generate_diet_plan(meals, gender, age, weight, height, activity_level):
    person = Person(
        gender=gender,
        age=age,
        weight_kg=weight,
        height_m=height / 100,
        activity_level=activity_level,
    )
    daily_cals = person.calc_tdee()

    # Build calorie budget per meal slot
    if meals == 1:
        slots = {"Breakfast": daily_cals}
    elif meals == 2:
        slots = {"Breakfast": daily_cals * 0.5, "Dinner": daily_cals * 0.5}
    elif meals == 3:
        slots = {
            "Breakfast": daily_cals / 3,
            "Lunch": daily_cals / 3,
            "Dinner": daily_cals / 3,
        }
    else:  # 4
        slots = {
            "Breakfast": daily_cals * 0.35,
            "Lunch": daily_cals * 0.25,
            "Snack": daily_cals * 0.20,
            "Dinner": daily_cals * 0.20,
        }

    plan = {}
    for slot, cals in slots.items():
        if slot == "Breakfast":
            pool = _shuffle(BREAKFAST)
            plan["Breakfast"] = _pick_meals(pool, pool.keys(), random.randint(1, 2), cals)
        elif slot == "Lunch":
            pool = _shuffle(MAINDISHES)
            plan["Lunch"] = _pick_meals(pool, pool.keys(), 2, cals)
        elif slot == "Dinner":
            pool = _shuffle(MAINDISHES)
            plan["Dinner"] = _pick_meals(pool, pool.keys(), 1, cals)
        elif slot == "Snack":
            pool = _shuffle(SNACKS)
            plan["Snack"] = _pick_meals(pool, pool.keys(), 1, cals)

    plan["calories"] = round(daily_cals)
    return plan
