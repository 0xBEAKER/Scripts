import itertools

def permute_words(words):
    permutations = []
    
    for word in words:
        for capitalize in [False, True]:
            for number in range(10000):
                permuted_word = word
                if capitalize:
                    permuted_word = permuted_word.capitalize()
                permuted_word += str(number)
                permutations.append(permuted_word)
                
                permuted_word_with_exclamation = permuted_word + "!"
                permutations.append(permuted_word_with_exclamation)
    
    return permutations

word_list = ["PauSus"]
permutations = permute_words(word_list)

for permutation in permutations:
    print(permutation)
