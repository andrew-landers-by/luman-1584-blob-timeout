"""
Generate payloads for the Ocean PTA service. Extend this class
to provide different types of payloads
"""
import random
from typing import Dict, Iterable, List, Tuple
from .helpers import modeled_od_pairs, random_od_pairs
from .payloads import Payloads


class PayloadGenerator:
    """
    Creates custom payloads with origin/
    destination routes that can be randomized
    """
    unique_ods = modeled_od_pairs()

    single_input_template = Payloads.SINGLE_INPUT
    batch_input_template = Payloads.BATCH_INPUT

    departure_port_key = Payloads.Keys.DEPARTURE_PORT
    arrival_port_key = Payloads.Keys.ARRIVAL_PORT

    def __init__(self, randomize_routes: bool = False):
        """
        Optionally randomize the origin/destination ports
        """
        self.randomize_routes = randomize_routes

    def single_payload(self, route: Tuple[str, str] = None) -> Dict:
        """
        Returns a single input payload with optional custom
        values for arrival port and departure port. Route will
        not be randomized if one is provided by the caller.
        """
        payload = self.single_input_template

        if route is None and self.randomize_routes:
            route = random_od_pairs(pairs=self.unique_ods, n=1).pop()

        if route:
            payload[self.departure_port_key] = route[0]
            payload[self.arrival_port_key] = route[1]

        return payload

    def batch_payload(self,
                      routes: Iterable[Tuple[str, str]] = None,
                      size: int = None
                      ) -> List[Dict]:
        """
        Returns a batch input payload with optional custom
        values for arrival port and departure port. Route will
        not be randomized if one is provided by the caller, and
        in that case size will be ignored.
        """
        if routes is None and self.randomize_routes:
            routes = random_od_pairs(pairs=self.unique_ods, n=size)

        if routes:
            sample = random.choices(
                population=self.batch_input_template, k=len(routes)
            )
            for idx, route in enumerate(routes):
                sample[idx][Payloads.Keys.DEPARTURE_PORT] = route[0]
                sample[idx][Payloads.Keys.ARRIVAL_PORT] = route[1]
            return sample
        elif size:
            return random.choices(
                population=self.batch_input_template, k=size
            )
        else:
            return self.batch_input_template
