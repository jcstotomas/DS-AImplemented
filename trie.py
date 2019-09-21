

class TrieNode:
    def __init__(self):
        self.children = [None] * 26;
        self.isEnd = False;


class Trie:

    def __init__(self):
        self.root = TrieNode();

    def getNode(self):
        return TrieNode();

    def getChar(self, c):

        return ord(c) - ord('a');


    def insert(self, word):
        ogNode = self.root;

        for i in range(len(word)):
            index = self.getChar(word[i]);
            if ogNode.children[index] == None:
                ogNode.children[index] = self.getNode();

            ogNode = ogNode.children[index];
    
        ogNode.isEnd = True;

    def findWord(self,word):
        ogNode = self.root;
        for i in range(len(word)):
            index = self.getChar(word[i]);
            if ogNode.children[index] == None:
                return False;
            ogNode = ogNode.children[index];
        return True;



        

trie = Trie();
trie.insert("hello");
trie.insert("hellp")
print(trie.findWord("hellp"))

