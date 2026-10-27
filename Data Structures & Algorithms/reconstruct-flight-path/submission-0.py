from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        destinations = defaultdict(list)

        # Reverse order lets pop() take the smallest destination.
        for source, target in sorted(tickets, reverse=True):
            destinations[source].append(target)

        stack = ["JFK"]
        route = []

        while stack:
            airport = stack[-1]

            if destinations[airport]:
                stack.append(destinations[airport].pop())
            else:
                # Finalize this airport when no tickets remain.
                route.append(stack.pop())

        return route[::-1]