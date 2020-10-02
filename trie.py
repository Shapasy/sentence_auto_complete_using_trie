class Node:
    def __init__(self):
        self.map = {}
        self.is_end_word = False

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add_word(self,word):
        curr = self.root
        for char in word:
            if(char not in curr.map.keys()):
                curr.map[char] = Node()
            curr = curr.map[char]
        curr.is_end_word = True

    def predict_words(self,sub_word):
        curr = self.root
        for char in sub_word:
            if(char not in curr.map):
                print("failed in prediction 🤐")
                return
            curr = curr.map[char]
        results = []
        queue = [(curr,sub_word)]
        while(queue != []):
            curr,curr_sub_word = queue.pop(0)
            if(curr.is_end_word): results.append(curr_sub_word)
            for son_char in curr.map.keys():
                queue.append((curr.map[son_char],curr_sub_word+son_char))
        return results
    
    

