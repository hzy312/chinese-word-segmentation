from BMM import BMM
from FMM import FMM
def BM(sentence, dict):
    '''
    use the bidirectional match to segment the sentence
    contrast the segmentation results of FMM and BMM to get the final results

    heuristics:
    1. if two results differ in the number of words, choose the sentence with fewer words
    2. if two results have the same number of words, choose the sentence with fewer single characters

    params:
    sentence: the sentence you want to segment
    dict: chinese word dictionary

    return:
    the list of sentence segmentation result
    '''
    result1 = FMM(sentence, dict)
    result2 = BMM(sentence, dict)
    l1 = len(result1)
    l2 = len(result2)
    segmentation_result = result1 if l1 < l2 else result2
    if (l1 == l2):
        num_of_single_char_1 = len([x for x in result1 if len(x) == 1])
        num_of_single_char_2 = len([x for x in result2 if len(x) == 1])
        segmentation_result = result1 if num_of_single_char_1 < num_of_single_char_2 else result2
    return segmentation_result