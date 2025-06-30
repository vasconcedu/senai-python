def eh_palindromo(s):
    s_inv = ""
    for i in range(0, len(s)):
        s_inv = s[i] + s_inv
    return s_inv == s

s = input("s> ")
if eh_palindromo(s):
    print("Eh palindromo")
else:
    print("Nao eh palindromo")
