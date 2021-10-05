def FMM(sentence, dict):
    '''
    use the forward maximum match to segment the sentence

    params:
    sentence: the sentence you want to segment
    dict: chinese word dictionary

    return:
    the list of sentence segmentation result
    '''
    MAX_LEN = max([len(x) for x in dict])
    segmentation_result = []
    line = sentence.strip()
    match_word = ''
    l = len(line)
    while l != 0:
        match_word = line[0:MAX_LEN]
        while match_word not in dict:
            if(len(match_word) == 1):
                break
            else:
                match_word = line[0:len(match_word) -1]
        segmentation_result.append(match_word)
        line = line[len(match_word):]
        l = len(line)
    return segmentation_result