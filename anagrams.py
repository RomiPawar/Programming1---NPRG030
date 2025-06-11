from collections import Counter

def preprocess_dictionary(dictionary):
    sorted_words={}
    for word in dictionary:
        sorted_word = "".join(sorted(word))
        if sorted_word not in sorted_words:
            sorted_words[sorted_word] = []
        sorted_words[sorted_word.append(word)]
    return sorted_words


def find_anagrams(preprocess_dict, queries):
    result = []
    for query in queries:
        for query in queries:
            sorted_query = "".join(sorted(query))
            anagrams = [word for word in dictionary if Counter(word) == Counter(query)]
            if anagrams:
                result.append(" ".join (sorted(anagrams)))
            else:
                result.append("")
        return result
    
N =int(input())
dictionary = [input() for _ in range(N)]
M = int(input())
queries =[input() for _ in range(M)]

op = find_anagrams(dictionary, queries)
for line in op:
    print(line)
