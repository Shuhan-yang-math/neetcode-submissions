from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        if endWord not in wordList:
            return 0

        word_length = len(beginWord)
        buckets = defaultdict(list)

        # Group words that differ at one position.
        for word in wordList:
            for i in range(word_length):
                pattern = word[:i] + "*" + word[i + 1:]
                buckets[pattern].append(word)

        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            word, distance = queue.popleft()

            if word == endWord:
                return distance

            for i in range(word_length):
                pattern = word[:i] + "*" + word[i + 1:]

                for neighbor in buckets[pattern]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, distance + 1))

                # This bucket cannot provide shorter paths later.
                buckets[pattern].clear()

        return 0