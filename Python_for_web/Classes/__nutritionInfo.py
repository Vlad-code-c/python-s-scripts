class NutritionInfo:
    def __init__(self, proteins, carbs, fats):
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats
    
    def energy(self):
        return int(self.fats * 9 + (self.carbs + self.proteins) * 4.2)

    def __add__ (self, other):
        total_proteins = self.proteins + other.proteins
        total_carbs = self.carbs + other.carbs
        total_fats = self.fats + other.fats
        return NutritionInfo(total_proteins, total_carbs, total_fats)


tvorog_9 = NutritionInfo(18, 10, 9)
apple = NutritionInfo(2, 5, 1)
breackfast = NutritionInfo(0, 0, 0)

breackfast = tvorog_9 + apple

energy = NutritionInfo.energy(breackfast)
#print(energy)