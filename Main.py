class Node:
    def init(self):
        self.mark = False
        self.edges = [None] * 26


def trie_insert(node, string, idx=0):
    if idx == len(string):
        node.mark = True
        return
    e = ord(string[idx]) - ord('a')
    if node.edges[e] is None:
        node.edges[e] = Node()
    trie_insert(node.edges[e], string, idx+1)


def trie_search(node, string, idx=0):
    if idx == len(string):
        print(node.mark)
        return
    e = ord(string[idx]) - ord('a')
    if node.edges[e] is None:
        print(False)
        return
    trie_search(node.edges[e], string, idx + 1)


def trie_delete(node, string, idx=0):
    if idx == len(string):
        if node.mark is False:
            raise Exception("item not found")
        node.mark = False
        return
    e = ord(string[idx]) - ord('a')
    if node.edges[e] is None:
        raise Exception("item not found")
    trie_delete(node.edges[e], string, idx + 1)


root = Node()
trie_insert(root, "pooyan")
trie_insert(root, "kiomars")
trie_search(root, "pooyan")
trie_search(root, "pooyan")
trie_search(root, "kio")
trie_search(root, "kioma")
trie_delete(root, "pooyan")
trie_search(root, "pooyan")