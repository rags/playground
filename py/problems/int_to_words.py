UNIQUE_WORDS = {0: '', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 
                7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', 11: 'Eleven',
                12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 
                16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Ninteen',
                20: 'Twenty', 30: 'Thirty', 40: 'Forty', 60: 'Sixty', 70: 'Seventy',
                80: 'Eighty', 90: 'Ninty', 100: 'Hundred', 1000: 'Thousand', 
                1000 ** 2: 'Million', 1000 ** 3: 'billion', 1000 ** 4: 'trillion'}

def wordify(num):
    num = int(num)
    weight = 1
    word_rep = []
    while num > 0:
        three_digits = num % 1000
        two_digits = num % 100
        hundreds = three_digits // 100
        cur_words = []
        if hundreds:
            cur_words.append(UNIQUE_WORDS[hundreds])
            cur_words.append(UNIQUE_WORDS[100])
        if two_digits < 21:
            cur_words.append(UNIQUE_WORDS[two_digits])
        else:
            last_digit = two_digits % 10
            if last_digit:
                cur_words.append(
                    UNIQUE_WORDS[two_digits - last_digit] + '-' + UNIQUE_WORDS[last_digit])

            else:
                cur_words.append(UNIQUE_WORDS[two_digits - last_digit])
                
        if weight > 1:
            cur_words.append(UNIQUE_WORDS[weight])
        word_rep = cur_words + word_rep
        weight = weight * 1000
        num = num // 1000

    return ' '.join(word_rep)


import sys
if __name__ == '__main__':
    print wordify(int(sys.argv[1]))
        
        
############################## TESTS ##############################
import pytest
@pytest.mark.parametrize(('num', 'words'), [
    (35, 'Thirty-Five'), 
    (44435, 'Forty-Four Thousand Four Hundred Thirty-Five'), 
    (5444544, 'Five Million Four Hundred Forty-Four Thousand Five Hundred Forty-Four'),
    (72005444544, 'Seventy-Two billion Five Million Four Hundred Forty-Four' +
     ' Thousand Five Hundred Forty-Four'),
    (6672005444513, 'Six trillion Six Hundred Seventy-Two billion Five Million' +
     ' Four Hundred Forty-Four Thousand Five Hundred Thirteen'), 
    (1002003, 'One Million Two Thousand Three'),
    (6005004003001, 'Six trillion Five billion Four Million Three Thousand One')
    
])
def should_wordify(num, words):
    assert wordify(num) == words
        
        
            