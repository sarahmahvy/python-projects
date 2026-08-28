def longestPalindrome(s:str):
    palindrome = ""
    palindromelen  = 0
    for i in range(len(s)):
        l = i
        r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > palindromelen:
                palindrome = s[l:r+1]
                palindromelen = r-l + 1
            l -= 1
            r += 1

        l = i
        r = i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > palindromelen:
                palindrome = s[l:r+1]
                palindromelen = r - l + 1
            l -= 1
            r += 1

    return palindrome

#print(longestPalindrome("cbbd"))
#print(longestPalindrome("babad"))
#print(longestPalindrome("abb"))
#print(longestPalindrome("abbcccba"))
#print(longestPalindrome("aacabdkacaa"))
#print(longestPalindrome("abcda"))
#print(longestPalindrome("rgczcpratwyqxaszbuwwcadruayhasynuxnakpmsyhxzlnxmdtsqqlmwnbxvmgvllafrpmlfuqpbhjddmhmbcgmlyeypkfpreddyencsdmgxysctpubvgeedhurvizgqxclhpfrvxggrowaynrtuwvvvwnqlowdihtrdzjffrgoeqivnprdnpvfjuhycpfydjcpfcnkpyujljiesmuxhtizzvwhvpqylvcirwqsmpptyhcqybstsfgjadicwzycswwmpluvzqdvnhkcofptqrzgjqtbvbdxylrylinspncrkxclykccbwridpqckstxdjawvziucrswpsfmisqiozworibeycuarcidbljslwbalcemgymnsxfziattdylrulwrybzztoxhevsdnvvljfzzrgcmagshucoalfiuapgzpqgjjgqsmcvtdsvehewrvtkeqwgmatqdpwlayjcxcavjmgpdyklrjcqvxjqbjucfubgmgpkfdxznkhcejscymuildfnuxwmuklntnyycdcscioimenaeohgpbcpogyifcsatfxeslstkjclauqmywacizyapxlgtcchlxkvygzeucwalhvhbwkvbceqajstxzzppcxoanhyfkgwaelsfdeeviqogjpresnoacegfeejyychabkhszcokdxpaqrprwfdahjqkfptwpeykgumyemgkccynxuvbdpjlrbgqtcqulxodurugofuwzudnhgxdrbbxtrvdnlodyhsifvyspejenpdckevzqrexplpcqtwtxlimfrsjumiygqeemhihcxyngsemcolrnlyhqlbqbcestadoxtrdvcgucntjnfavylip"))


def shortestPalindrome(s:str):
    palindrome = ""
    temp = longestPalindrome(s)
    start = s.index(temp)
    end = len(temp) - 1
    
    transform = "" 
    
    if temp in s and len(temp)>1:
        transform = s[end:]
    
    else:
        transform = s[1:]
    transform = ''.join(reversed(transform))
    palindrome = transform + s
    return palindrome        
        #l=i
        #r=i+1
        #while l >= 0 and r < len(s):
        #    if s[l] != s[r] and (l!=start or r!=end):
        #        temp += s[r]
        #    l -= 1
        #    r += 1

    #palindrome = temp + s
    #return palindrome
#    palindromelen = 0


#    for i in range(1,len(s)):
#        transform = ""
#        temp = ""
#        l = i - 1
#        r = i
#        while l >= 0 and r < len(s):
#            if s[l] != s[r]:
#                transform = s[r]
#            else:
#                transform = s[l]
#            l -= 1
#            r += 1
#            temp += transform

#        l = i
#        r = i + 1
#        while l >= 0 and r < len(s):
#            if s[l] != s [r]:
#                transform = s[r]
#            else:
#                transform = s[l]
#            l -= 1
#            r += 1
#            temp += transform
        


#    palindrome = temp + s

#    return palindrome
print(shortestPalindrome("aacecaaa"))
print(shortestPalindrome("abb"))
print(shortestPalindrome("abcd"))
