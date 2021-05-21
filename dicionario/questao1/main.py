string = input()
def histogram(s):
	d = dict()
	for c in s:
		d[c] = d.get(c,0)+1
	return d

def invert_dict(s):
    i={}
    for key in s:
        v=s[key]
        i.setdefault(v, []).append(key)
    return i
print(histogram(string))
print(invert_dict(histogram(string)))

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def invert_dict(d):
    """Inverts a dictionary, returning a map from val to a list of keys.
    If the mapping key->val appears in d, then in the new dictionary
    val maps to a list that includes key.
    d: dict
    Returns: dict
    """
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

a = input()
h = histogram(a)
print(h)
print(invert_dict(h))
