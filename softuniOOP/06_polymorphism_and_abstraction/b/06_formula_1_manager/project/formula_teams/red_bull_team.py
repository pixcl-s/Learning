from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    SPONSORS = {"Oracle": {1: 1_500_000, 2: 800_000},
                "Honda": {8: 20_000, 10: 10_000}}
#               sponsor: {place: money_prize}
    EXPANSES = 250_000
    VALID_TEAM_NAME = "Red Bull"
