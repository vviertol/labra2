import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    s += "x" * (1000 - origlen)
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    if origlen > 1000 or origlen == 0:
        raise IndexError
    for c in s:
        if 97 <= ord(c) <= 122 or 65 <= ord(c) <= 90:
            if c.islower():
                c=c.upper()
            else:
                c=c.lower()
            # Rot13 the character for maximum security
        elif c in digitmapping:
            c=digitmapping[c]
        else:
            raise ValueError
            
        crypted += codecs.decode(c, 'rot13')
    return crypted[:origlen]

def decode(s):
    return encode(s)

