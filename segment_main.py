from make_dict import chinese_word_dict
from BM import BM
from metrics import evaluate
from tqdm import tqdm
import time
if __name__ == '__main__':
    file_path1 = 'pku_test.utf8'
    file_path2 = 'pku_test_gold.utf8'
    with open(file_path1, 'r', encoding='utf-8') as f:
        try:
            sentences = f.readlines()
        finally:
            f.close()
    with open(file_path2, 'r', encoding = 'utf-8') as f:
        try:
            answers = f.readlines()
        finally:
            f.close()


    precision = []
    recall = []
    f1 = []

    with open('results.txt', 'w', encoding='utf-8') as f:
        try:
            start_time = time.time()
            for i in tqdm(range(len(sentences))):
                pred_i = BM(sentences[i], chinese_word_dict)
                gold_i = answers[i].split()
                f.write(' '.join(pred_i))
                f.write('\n')
                p, r, ff = evaluate(gold_i, pred_i)
                precision.append(p)
                recall.append(r)
                f1.append(ff)
                f.write(str([p, r, ff]))
                f.write('\n')
            end_time = time.time()
            interval = end_time - start_time
            print(f'total time: {interval}')
            l = len(f1)
            precision_avg = sum(precision) / l
            recall_avg = sum(recall) / l
            f1_avg = sum(f1) / l
            print(f"average metrics:\nprecision: {precision_avg}\nrecall: {recall_avg}\nF1{f1_avg}")
        finally:
            f.close()

