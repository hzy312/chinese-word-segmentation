def evaluate(gold, prediction):
    '''
    compute the precision, recall, f1-score of the segmentation result
    params:
    gold: ground truth
    prediction: the segmentation result of BM algorithm

    return:
    precision, recall, f1
    '''

    gold_size = len(gold)
    pred_size = len(prediction)
    right_size = len([x for x in prediction if x in gold])

    precesion = right_size / pred_size
    recall = right_size / gold_size
    f1 = (2 * precesion * recall) / (precesion + recall)

    return precesion, recall, f1
