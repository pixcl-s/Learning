from typing import List

from project.artifacts.base_artifact import BaseArtifact
from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.base_collector import BaseCollector
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    VALID_ARTIFACTS = {ContemporaryArtifact.__name__: ContemporaryArtifact,
                       RenaissanceArtifact.__name__: RenaissanceArtifact}
    VALID_COLLECTORS = {Museum.__name__: Museum,
                        PrivateCollector.__name__: PrivateCollector}

    def __init__(self):
        self.artifacts: List[BaseArtifact] = []
        self.collectors: List[BaseCollector] = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        an_artifact = next((x for x in self.artifacts if x.name == artifact_name), None)
        if an_artifact:
            raise ValueError(f"{artifact_name} has been already registered!")

        if artifact_type not in self.VALID_ARTIFACTS:
            raise ValueError("Unknown artifact type!")

        self.artifacts.append(self.VALID_ARTIFACTS[artifact_type](artifact_name, artifact_price, artifact_space))

        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        an_collector = next((x for x in self.collectors if x.name == collector_name), None)
        if an_collector:
            raise ValueError(f"{collector_name} has been already registered!")

        if collector_type not in self.VALID_COLLECTORS:
            raise ValueError("Unknown collector type!")

        self.collectors.append(self.VALID_COLLECTORS[collector_type](collector_name))
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        the_collector = next((x for x in self.collectors if x.name == collector_name), None)
        the_artifact = next((x for x in self.artifacts if x.name == artifact_name), None)

        if the_collector is None:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        if the_artifact is None :
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if the_collector.can_purchase(the_artifact.price, the_artifact.space_required):
            self.artifacts.remove(the_artifact)
            the_collector.purchased_artifacts.append(the_artifact)
            the_collector.available_money -= the_artifact.price
            the_collector.available_space -= the_artifact.space_required

            return f"{collector_name} purchased {artifact_name} for a price of {the_artifact.price:.2f}."

        return "Purchase is impossible."

    def remove_artifact(self, artifact_name: str):
        the_artifact = next((x for x in self.artifacts if x.name == artifact_name), None)

        if the_artifact:
            self.artifacts.remove(the_artifact)

            return f"Removed {the_artifact.artifact_information()}"

        return "No such artifact."

    def fundraising_campaigns(self, max_money: float):
        participants = [x for x in self.collectors if x.available_money <= max_money]

        for x in participants:
            x.increase_money()

        return f"{len(participants)} collector/s increased their available money."

    def get_auction_report(self):
        to_return = f"**Auction statistics**\n" \
                    f"Total number of sold artifacts: {sum(len(x.purchased_artifacts) for x in self.collectors)}\n" \
                    f"Available artifacts for sale: {len(self.artifacts)}\n" \
                    f"***\n"

        for x in sorted(self.collectors, key=lambda collectors: (-len(collectors.purchased_artifacts), collectors.name)):
            to_return += f"{str(x)}\n"

        return to_return.strip()
