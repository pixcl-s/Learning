from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    SPONSORS = {"Petronas": {1: 1_000_000, 3: 500_000},
                "TeamViewer": {5: 100_000, 7: 50_000}}
#                 sponsor: {place: money_prize}
    EXPANSES = 200_000
    VALID_TEAM_NAME = "Mercedes"
