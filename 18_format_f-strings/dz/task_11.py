def encryption(abc, word):
    word1 = ''
    ready_word = ''
    if len(word) == 2:
        step = -1
    elif len(word) == 3:
        step = -2
    elif len(word) >= 4:
        step = -3
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
        else:
            sym1 = sym.lower()
            id = abc.index(sym1) - 1
            if id > len(abc) - 1:
                id -= len(abc)
            symbol = abc[id]
        word1 += symbol
    ready_word += word1[step:] + word1[:step]
    return ready_word


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
text_list = ('vujgvmCfb tj ufscfu ouib z/vhm').split(' ')
test2_list = ('bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip').split(' ')

new_textList = [encryption(list_abc, word) for word in test2_list]

print(new_textList)