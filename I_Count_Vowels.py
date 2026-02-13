def vowel(n , vouwel , coun , idx):
        if idx == len(n):
                return coun
        m = n[idx].lower()
        if m in vouwel:
                return vowel(n , vouwel , coun , idx + 1) + coun + 1
        return vowel(n , vouwel , coun , idx + 1)
n = input()
vouwel = "aeiou"
coun = 0
idx = 0
print(vowel(n , vouwel , coun , idx))