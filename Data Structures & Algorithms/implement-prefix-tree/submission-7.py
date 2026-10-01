class TrieNode():

    def __init__(self):
        self.children={}
        self.is_end=False



class PrefixTree:

    def __init__(self):
        self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        cur=self.root
        for i in word:
            if i not in cur.children:
                cur.children[i]=TrieNode()
                cur=cur.children[i]
            else:
                cur=cur.children[i]
        cur.is_end=True
        


    def search(self, word: str) -> bool:
        cur=self.root
        for i in word:
            if i not in cur.children:
                return False
            else:
                cur=cur.children[i]
        return cur.is_end

        

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for i in prefix:
            if i not in cur.children:
                return False
            cur=cur.children[i]
        return True
        
        