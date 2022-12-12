"""
Activity level multipliers (Mifflin-St Jeor TDEE):
    1.2   — Sedentary (little or no exercise, desk job)
    1.375 — Lightly Active (light exercise 1-3 days/week)
    1.55  — Moderately Active (exercise 3-5 days/week)
    1.725 — Very Active (hard exercise 6-7 days/week)
    1.9   — Extremely Active (2x daily training)
"""


class Person:
    def __init__(self, gender, age, weight_kg=0, height_m=0, activity_level=0):
        self.gender = gender
        self.age = age
        self.weight_kg = weight_kg
        self.height_m = height_m
        self.activity_level = activity_level

    def calc_bmr(self):
        """
        Mifflin-St Jeor BMR equation.
        Male:   BMR = (10 × kg) + (6.25 × cm) - (5 × age) + 5
        Female: BMR = (10 × kg) + (6.25 × cm) - (5 × age) - 161
        """
        base = (10 * self.weight_kg) + (6.25 * (self.height_m * 100)) - (5 * self.age)
        adjustment = 5 if self.gender == "male" else -161
        self.bmr = round(base + adjustment, 1)
        return self.bmr

    def calc_tdee(self):
        """Returns Total Daily Energy Expenditure based on BMR and activity level."""
        bmr = self.calc_bmr()
        return round(bmr * float(self.activity_level), 1)
