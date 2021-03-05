def revers(sym_dict):
    rev_hist = dict()
    for i_key in sym_dict:
        if sym_dict[i_key] in rev_hist:
            rev_hist[sym_dict[i_key]].append(i_key)
        else:
            rev_hist[sym_dict[i_key]] = [i_key]
    return rev_hist

hist = {
    'к': 3,
    'а': 1,
    'о': 1,
    'й': 1,
    ' ': 3,
    'т': 5,
    'у': 2,
    'б': 1,
    'д': 1,
    'е': 2,
    'с': 1
}

rev_histogram = revers(hist)
print(rev_histogram)