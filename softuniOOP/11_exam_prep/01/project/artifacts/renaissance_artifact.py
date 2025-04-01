from project.artifacts.base_artifact import BaseArtifact


class RenaissanceArtifact(BaseArtifact):
    def __init__(self, name, price, space_required):
        super().__init__(name, price, space_required)

    def artifact_information(self):
        return f"{str(self)}: {self.name}; Price: {self.price:.2f}; Required space: {self.space_required}"

    def __str__(self):
        return "Renaissance Artifact"
