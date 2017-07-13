def word_rev():
    s = raw_input("Input sentence of your choise:")
    l = s.split(' ')
    nl = []
    i = 0
    while i < len(l):
        j = l[-i-1]
        nl.append(j)
        i += 1
        return nl
print word_rev()
print " ".join(word_rev())
