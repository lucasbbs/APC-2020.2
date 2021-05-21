string1 = list(input())
string2 = list(input())
print(sorted(string1)== sorted(string2))

# string1 = input()
# string2 = input()
# def histogram(s):
# 	d = dict()
# 	for c in s:
# 		d[c] = d.get(c,0)+1
# 	return d
# print(sorted(histogram(string1).items())==sorted(histogram(string2).items()))

def ans(s, t):
    letters = {}
    for ch in s:
        letters[ch] = letters.get(ch, 0) + 1
    for ch in t:
        letters[ch] = letters.get(ch, 0) - 1
    for v in letters.values():
        if v != 0:
            return False
    return True

s = input()
t = input()
print(ans(s, t))

'''Solução alternativa:

s, t = input(), input()
freq_s, freq_t = {}, {}
for letra in s:
    freq_s[letra] = freq_s.get(letra, 0) + 1
for letra in t:
    freq_t[letra] = freq_t.get(letra, 0) + 1
print(freq_s == freq_t)
'''
