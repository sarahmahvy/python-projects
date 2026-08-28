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

print(longestPalindrome("cbbd"))
print(longestPalindrome("babad"))
print(longestPalindrome("abb"))
print(longestPalindrome("abbcccba"))
print(longestPalindrome("aacabdkacaa"))
print(longestPalindrome("abcda"))
print(longestPalindrome("rgczcpratwyqxaszbuwwcadruayhasynuxnakpmsyhxzlnxmdtsqqlmwnbxvmgvllafrpmlfuqpbhjddmhmbcgmlyeypkfpreddyencsdmgxysctpubvgeedhurvizgqxclhpfrvxggrowaynrtuwvvvwnqlowdihtrdzjffrgoeqivnprdnpvfjuhycpfydjcpfcnkpyujljiesmuxhtizzvwhvpqylvcirwqsmpptyhcqybstsfgjadicwzycswwmpluvzqdvnhkcofptqrzgjqtbvbdxylrylinspncrkxclykccbwridpqckstxdjawvziucrswpsfmisqiozworibeycuarcidbljslwbalcemgymnsxfziattdylrulwrybzztoxhevsdnvvljfzzrgcmagshucoalfiuapgzpqgjjgqsmcvtdsvehewrvtkeqwgmatqdpwlayjcxcavjmgpdyklrjcqvxjqbjucfubgmgpkfdxznkhcejscymuildfnuxwmuklntnyycdcscioimenaeohgpbcpogyifcsatfxeslstkjclauqmywacizyapxlgtcchlxkvygzeucwalhvhbwkvbceqajstxzzppcxoanhyfkgwaelsfdeeviqogjpresnoacegfeejyychabkhszcokdxpaqrprwfdahjqkfptwpeykgumyemgkccynxuvbdpjlrbgqtcqulxodurugofuwzudnhgxdrbbxtrvdnlodyhsifvyspejenpdckevzqrexplpcqtwtxlimfrsjumiygqeemhihcxyngsemcolrnlyhqlbqbcestadoxtrdvcgucntjnfavylip"))
