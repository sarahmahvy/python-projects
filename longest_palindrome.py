def longestPalindrome(s: str):
        palindrome=""
        #if s == ''.join(reversed(s)):
        #    return s
        #if len(s) == 1:
        #     return s
        #if len(s) == 2:
        #    if s[0] == s[1]:
        #        return s
        #    else:
        #        return s[0]

        #if len(s) == s.count(s[0]):
        #    return s
        start = 0
        for j in range(len(s)):
            loop = s
            start += 1
            for i in range(len(loop)):
                temp = s[i:start]
                if temp == ''.join(reversed(temp)) and len(palindrome) < len(temp):
                
                    palindrome = temp
                else:
                    continue
            
            continue            
        #if palindrome == ''.join(reversed(palindrome)):
        return palindrome
        #else:
            #return s[0]

print(longestPalindrome("cbbd"))
print(longestPalindrome("babad"))
print(longestPalindrome("abb"))
print(longestPalindrome("abbcccba"))
print(longestPalindrome("aacabdkacaa"))
print(longestPalindrome("abcda"))
print(longestPalindrome("rgczcpratwyqxaszbuwwcadruayhasynuxnakpmsyhxzlnxmdtsqqlmwnbxvmgvllafrpmlfuqpbhjddmhmbcgmlyeypkfpreddyencsdmgxysctpubvgeedhurvizgqxclhpfrvxggrowaynrtuwvvvwnqlowdihtrdzjffrgoeqivnprdnpvfjuhycpfydjcpfcnkpyujljiesmuxhtizzvwhvpqylvcirwqsmpptyhcqybstsfgjadicwzycswwmpluvzqdvnhkcofptqrzgjqtbvbdxylrylinspncrkxclykccbwridpqckstxdjawvziucrswpsfmisqiozworibeycuarcidbljslwbalcemgymnsxfziattdylrulwrybzztoxhevsdnvvljfzzrgcmagshucoalfiuapgzpqgjjgqsmcvtdsvehewrvtkeqwgmatqdpwlayjcxcavjmgpdyklrjcqvxjqbjucfubgmgpkfdxznkhcejscymuildfnuxwmuklntnyycdcscioimenaeohgpbcpogyifcsatfxeslstkjclauqmywacizyapxlgtcchlxkvygzeucwalhvhbwkvbceqajstxzzppcxoanhyfkgwaelsfdeeviqogjpresnoacegfeejyychabkhszcokdxpaqrprwfdahjqkfptwpeykgumyemgkccynxuvbdpjlrbgqtcqulxodurugofuwzudnhgxdrbbxtrvdnlodyhsifvyspejenpdckevzqrexplpcqtwtxlimfrsjumiygqeemhihcxyngsemcolrnlyhqlbqbcestadoxtrdvcgucntjnfavylip"))

#temp1 = ""
        #temp2 = ""
        #for character in s:
        #    temp1 = s
            #if temp1 == ''.join(reversed(temp1)):
            #    palindrome = temp1
         #   for char in s:
          #      ind = temp1.index(char)
           #     temp2 = temp1[:ind] + temp1[ind+1:]
            #    if temp2 == ''.join(reversed(temp2)):
             #       palindrome = temp2
                #temp3 = temp1[:ind]
                #temp4 = temp1[ind:]
                #temp5 = temp3 + temp4
                #if temp5 == ''.join(reversed(temp3)):
                #    palindrome = temp3