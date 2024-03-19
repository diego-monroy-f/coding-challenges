class TrieNode:
    def __init__(self, keys=None) -> None:
        self.is_end = False
        self.keys = keys or {}

class Trie:
    def __init__(self) -> None:
        self.p = TrieNode()
    def insert(self, word: str) -> None:
        current_node = self.p
        for c in word:
            if c in current_node.keys:
                current_node = current_node.keys[c]
            else:
                current_node.keys[c] = TrieNode()
                current_node = current_node.keys[c]
        current_node.is_end = True
    def search(self, word: str) -> bool:
        current_node = self.p
        for c in word:
            if c not in current_node.keys:
                return False
            else:
                current_node = current_node.keys[c]
        return current_node.is_end
    def starts_with(self, prefix: str) -> bool:
        current_node = self.p
        for c in prefix:
            if c not in current_node.keys:
                return False
            else:
                current_node = current_node.keys[c]
        return True