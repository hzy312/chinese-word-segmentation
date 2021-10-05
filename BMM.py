def BMM(sentence, dict):
    '''
    use the backward maximum match to segment the sentence

    params:
    sentence: the sentence you want to segment
    dict: chinese word dictionary

    return:
    the list of sentence segmentation result
    '''
    MAX_LEN = max([len(x) for x in dict])
    segmentation_result = []
    line = sentence.strip()
    l = len(line)
    match_word = ''
    while l != 0:
        match_word = line[l - MAX_LEN:]
        while match_word not in dict:
            if(len(match_word) == 1):
                break
            else:
                match_word = line[l-len(match_word)+1:]
        segmentation_result.append(match_word)
        line = line[0:l-len(match_word)]
        l = len(line)
    return list(reversed(segmentation_result))