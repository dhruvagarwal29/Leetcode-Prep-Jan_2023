# Given a string s and a dictionary of strings word_dict, add spaces in s to construct a sentence
#  where each word is a valid dictionary word. Return all such possible sentences in any order.


def word_break(string, word_dict):
    result = []

    for word in word_dict: 
        if string.startswith(word):
            sub_words = []
            sub_words.append(word)
            # we are sending the string after the word  string[len(word):]
            # cat ---> sanddog
            dfs(string[len(word):], word_dict, sub_words, result)

    return result

def dfs(sub_string, word_dict, sub_words, result):
    if not sub_string:  # if substring is empty
        sentence = " ".join(sub_words)
        result.append(sentence)

    for word in word_dict:
        if sub_string.startswith(word):
            sub_words.append(word)
            dfs(sub_string[len(word):], word_dict, sub_words, result)
            sub_words.pop()


if __name__ == "__main__":
    string = "catsanddog"
    word_dict = subs = ["an", "book", "car", "cat", "cook", "cookbook", "crash", 
            "cream", "high", "highway", "i", "ice", "icecream", "low", 
            "scream", "veg", "vegan", "way", "hello", "from", "what", 
            "cats", "and", "dog", "sand", "pineapple", "pine", "apple",
            "pen", "applepen"]

    print(word_break(string, word_dict))

