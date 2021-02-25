def encryption(abc, word):
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

def perm2(word, shift):
    word1 = ''
    step = shift % len(word)
    word1 += word[step:] + word[:step]
    return word1

def sentenseTru(sentence):
    sentenceOk = sentence[1:]
    return  sentenceOk


list_abc = list('abcdefghijklmnopqrstuvwxyz')
text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'

list_text = encryption(list_abc, text).split(' ')

shift = -3
flag_title = True

for i in range(len(list_text)):
    list_text[i]= perm2(list_text[i], shift)
    if flag_title:
        list_text[i] = list_text[i].title()
        flag_title = False
    if '.' in list_text[i] or '!' in list_text[i]:
        shift -= 1
        flag_title =True

list_text = ' '.join(list_text).split('.')

list_text = [sentenseTru(sentence) if sentence.startswith(' ') else sentence for sentence in list_text]

print('.\n'.join(list_text))

