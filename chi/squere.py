def data_separate(y, complement=False):
    kelas = sorted(set(y))
    dict_index = dict()
    for c in kelas:
        index = list()
        for ix, c_ in enumerate(y):
            if complement==False and c==c_:
                index.append(ix)
            elif complement==True and c!=c_:
                index.append(ix)
        dict_index.update({c:index})
    return dict_index