def encryption(abc, word):
    word1 = ''
    ready_text = ''
    for sym in word:
        if sym == '/':
            symbol = '.'
        elif sym == '(':
            symbol = "'"
        elif sym == '.':
            symbol = '-'
        elif sym == '+':
            symbol = '*'
        elif sym == '"':
            symbol = '!'
        elif sym == '-':
            symbol = ','
        elif sym == ' ':
            symbol = ' '
        else:
            sym1 = sym.lower()
            id = abc.index(sym1) - 1
            if id > len(abc) - 1:
                id -= len(abc)
            symbol = abc[id]
        ready_text += symbol

    return ready_text


def point_transfer(word):
    word1 = word.replace('.', '')
    word1 += '.'
    return word1


def permutation_of_symbols(sentence, shift):
    list_sentence = sentence.split(' ')
    list_sentence = [list_sentence[i] for i in range(len(list_sentence)) if list_sentence[i] != '']
    word1 = ''
    for i in range(len(list_sentence)):
        # if list_sentence[i] != '':
        word = list_sentence[i]
        step = shift % len(word) * -1
        word1 += word[step:] + word[:step]
        if i == 0:
            word1 = word1.title()
        list_sentence[i] = word1
        word1 = ''
    return ' '.join(list_sentence)


list_abc = list('abcdefghijklmnopqrstuvwxyz')
# text = 'vujgvmCfb tj ufscfu ouib z/vhm ' \
#        'jdjuFyqm jt fscfuu uibo jdju/jnqm ' \
#        'fTjnqm tj scfuuf ibou fy/dpnqm ' \
#        'yDpnqmf jt cfuufs boui dbufe/dpnqmj ' \
#        'uGmb tj fuufsc ouib oftufe/' \
#        'bstfTq jt uufscf uibo otf/ef ' \
#        'uzSfbebcjmj vout/dp ' \
#        'djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ' \
#        'ipvhiBmu zqsbdujdbmju fbutc uz/qvsj ' \
#        'Fsspst tipvme wfsof qbtt foumz/tjm ' \
#        'omfttV mjdjumzfyq odfe/tjmf' \
#        'Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv ' \
#        'Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ ' \
#        'Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud ' \
#        'xOp tj scfuuf ibou /ofwfs ' \
#        'uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op' \
#        'gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb ' \
#        'Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ ' \
#        'bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
text = 'vujgvmCfb tj ufscfu ouib z/vhm '

text1 = point_transfer(encryption(list_abc, text))

print(text1)
# text_list = text.split(' ')
#
# new_textList = [encryption(list_abc, word) for word in text_list]
# new_textList = ' '.join([point_transfer(word) if '.' in word else word for word in new_textList]).split('.')
# print(new_textList)
#
# shift = 3
#
# for sentence in new_textList:
#     sentence = permutation_of_symbols(sentence, shift)
#     print(sentence)
#     shift += 1

# print(new_textList)