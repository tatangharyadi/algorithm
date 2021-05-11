def anagrams(S):
    d = {}
    for word in S:
        s = ''.join(sorted(word))
        if s in d:
            d[s].append(word)
        else:
            d[s] = [word]
    return [d[s] for s in d if len(d[s]) > 1]

def main():
    input = ("below the car is a rat drinking cider and bending its elbow while this thing"
        " is an arc that can act like a cat which cried during the night casued by pain in its"
        " bowel")
    S = set(input.split())
    A = anagrams(S)
    print(A)

if __name__ == '__main__':
    main()