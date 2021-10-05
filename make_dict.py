dict_path = "pku_training_words.utf8"

with open(dict_path, 'r', encoding='utf-8') as f:
    try:
        file_content = f.read().split()
    finally:
        f.close()
chinese_word_dict = list(set(file_content))