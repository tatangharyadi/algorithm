t9 = '22233344455566677778889999'
#     abcdefghijklmnopqrstuvwxyz mapping to phone

def letter_to_digit(x):
    assert 'a' <= x <= 'z'
    return t9[ord(x) - ord('a')]

def code_word(word):
    return ''.join(map(letter_to_digit, word))

def predictive_text(dic):
    # total_weight[p] = total weight of words having prefix p
    total_weight = {}
    for word, weight in dic.items():
        prefix = ''
        for x in word:
            prefix += x
            if prefix in total_weight:
                total_weight[prefix] += weight
            else:
                total_weight[prefix] = weight

    # prop[s] = prefix to display for s
    prop = {}
    for prefix in total_weight:
        code = code_word(prefix)
        if (code not in prop
            or total_weight[prop[code]] < total_weight[prefix]):
            prop[code] = prefix
    return prop

def propose(prop, seq):
    if seq in prop:
        return prop[seq]
    return None

def main():
    words = {'hell':3, 'hello': 4, 'idea':8, 'next':8, 'super':3}
    prop = predictive_text(words)
    
    for digits in ('43556', '4332'):
        seq = ''
        for digit in digits:
            seq += digit
            print(f'{seq}: {propose(prop, seq)}')

if __name__ == '__main__':
    main()