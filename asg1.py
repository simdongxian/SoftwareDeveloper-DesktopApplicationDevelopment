"""
// PROBLEM DEFINITION
// ------------------
// Reverse each word in the input string.
// The order of the words will be unchanged.
// A word is made up of letters and/or numbers.
 Other characters (spaces, punctuation) will not be reversed.
"""
def reverse_words(str):
    result = ""
    temp = ""
    for i in range(len(str)):
        #check if alphanumeric string
        if str[i].isalnum():
            temp += str[i]
        else:
            #if symbol/space append reversed temp string and symbol/space to result
            result += temp[::-1]
            result += str[i]
            temp = ""
    # append reversed temp string handles cases when ends with string
    if temp:
        result += temp[::-1]
    return result


if __name__ == '__main__':
    assert reverse_words("abc def") == "cba fed"
    assert reverse_words("!abc !def") == "!cba !fed"
    assert reverse_words("abc! def!") == "cba! fed!"
    assert reverse_words("!abc! !def!") == "!cba! !fed!"
    assert reverse_words("123 456") == "321 654"
    assert reverse_words("123! 456?") == "321! 654?"
    assert reverse_words("!123 !456") == "!321 !654"
    assert reverse_words("!123! !456?") == "!321! !654?"
    assert reverse_words("!Test1! !Te5T!") == "!1tseT! !T5eT!"
    assert reverse_words("!Tes?t1! !Te?5T!") == "!seT?1t! !eT?T5!"
    assert reverse_words("   space   test ") == "   ecaps   tset "
    assert reverse_words("") == ""