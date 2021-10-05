from make_dict import chinese_word_dict
from BM import BM
from metrics import evaluate
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
    list = BM(sentences[7], chinese_word_dict)
    print(list)
    with open('results.txt', 'w', encoding = 'utf-8') as f:
        f.write(' '.join(list))


