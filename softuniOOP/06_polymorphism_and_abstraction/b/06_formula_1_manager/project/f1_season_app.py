from typing import Optional

from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    def __init__(self):
        self.red_bull_team: RedBullTeam = None
        self.mercedes_team: MercedesTeam = None

    def register_team_for_season(self, team_name: str, budget: int) -> Optional[str]:
        if team_name == RedBullTeam.VALID_TEAM_NAME:
            self.red_bull_team = RedBullTeam(budget)
        elif team_name == MercedesTeam.VALID_TEAM_NAME:
            self.mercedes_team = MercedesTeam(budget)
        else:
            raise ValueError("Invalid team name!")
        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception("Not all teams have registered for the season.")

        return f"Red Bull: {RedBullTeam.calculate_revenue_after_race(self.red_bull_team, red_bull_pos)}." \
               f" Mercedes: {MercedesTeam.calculate_revenue_after_race(self.mercedes_team, mercedes_pos)}." \
               f" {'Red Bull' if red_bull_pos<mercedes_pos else 'Mercedes'} is ahead at the {race_name} race."
