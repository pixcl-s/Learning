from abc import ABC


class FormulaTeam(ABC):
    MINIMUM_BUDGET = 1_000_000

    def __init__(self, budget: int):
        self.budget = budget

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < self.MINIMUM_BUDGET:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = -self.EXPANSES

        for sponsor in self.SPONSORS.values():
            for position, prize in sponsor.items():
                if race_pos <= position:
                    revenue += prize
                    break

        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

