from typing import List


class Node:
    def __init__(self):
        self.child = [-1] * 26
        self.idx = -1


class Solution:
    def updateIndex(self, stored_idx, new_idx, words_container):
        if stored_idx == -1:
            return new_idx

        old_len = len(words_container[stored_idx])
        new_len = len(words_container[new_idx])

        if new_len < old_len:
            return new_idx

        if new_len == old_len and new_idx < stored_idx:
            return new_idx

        return stored_idx

    def stringIndices(self, words_container: List[str], words_query: List[str]) -> List[int]:
        trie = [Node()]

        for i in range(len(words_container)):
            word = words_container[i][::-1]

            node = 0

            trie[node].idx = self.updateIndex(trie[node].idx, i, words_container)

            for ch in word:
                c = ord(ch) - ord("a")

                if trie[node].child[c] == -1:
                    trie[node].child[c] = len(trie)
                    trie.append(Node())

                node = trie[node].child[c]

                trie[node].idx = self.updateIndex(trie[node].idx, i, words_container)

        result = []

        for query in words_query:
            query = query[::-1]

            node = 0

            for ch in query:
                c = ord(ch) - ord("a")

                if trie[node].child[c] == -1:
                    break

                node = trie[node].child[c]

            result.append(trie[node].idx)

        return result
