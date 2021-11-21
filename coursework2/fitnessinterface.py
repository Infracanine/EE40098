from typing import List

class FitnessFunctionInterface:
    def evaluate(self, individual: List[str], target) -> int:
        # Given a target and an individual encoded as a list of binary strings, evaluate fitness and return int verdict
        pass