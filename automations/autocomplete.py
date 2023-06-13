class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True

    def search(self, prefix):
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        return self._get_words(current, prefix)

    def _get_words(self, node, prefix):
        results = []
        if node.is_end_of_word:
            results.append(prefix)
        for char, child in node.children.items():
            results.extend(self._get_words(child, prefix + char))
        return results


trie = Trie()
words = ["acute", "bevel", "approve", "ball", "crane", "crib", "dog", "drone", "evolve"]
for word in words:
    trie.insert(word)

prefix = input("Enter a letter: ")
autocomplete_results = trie.search(prefix)
print("Results:", autocomplete_results)



#built on a very little collection of words. Can be expanded according to desired goal
