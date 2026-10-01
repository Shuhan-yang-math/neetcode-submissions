class TriNode():
    def __init__(self):
        self.children={}
        self.is_end=False

class WordDictionary:

    def __init__(self):
        self.root=TriNode()

    def addWord(self, word: str) -> None:
        cur=self.root
        for i in word:
            if i not in cur.children:
                cur.children[i]=TriNode()
            cur=cur.children[i]
        cur.is_end=True
    def search(self, word: str) -> bool:
        n=len(word)
        def dfs(i,node):
            if i==n and node.is_end==True:
                return True
            elif i==n and node.is_end==False:
                return False
            if word[i]==".":
                for a in node.children.values():
                    if dfs(i+1,a):
                        return True
                return False
            elif word[i] in node.children:
                return dfs(i+1,node.children[word[i]])
            else:
                return False
        return dfs(0,self.root)


