class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:

        recipy_left = set(recipes)
        supply_set = set(supplies)
        result = []

        while recipy_left:
            new_recipy = []
            for recipy, ing_list in zip(recipes, ingredients):
                if recipy in recipy_left and all(incredient in supply_set for incredient in ing_list):
                    result.append(recipy)
                    new_recipy.append(recipy)
                    supply_set.add(recipy)

            if not new_recipy:
                break
            recipy_left -= set(new_recipy)

        return result
