from trie import Trie

if __name__ == "__main__":
    
    target="what was" # only change this variable
    
    print("Given Input :",target)
    
    print("Loading dataset....")
    with open('./dataset.txt',encoding="UTF-8") as f:
        dataset = f.read().split('\n')
        
    trie = Trie()
    # Another example of using trie is "Spelling checker"
    
    print("Start feeding dataset to the trie....")
    for word in dataset: 
        trie.add_word(word)
        
    print("predicting the results....")
    results = trie.predict_words(target)
    if(results):
        print("Results 👀 :-")
        for i,result in enumerate(results):
            print(f"{i+1}) {result}")
    