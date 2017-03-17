Сложности/особенности корпуса, принципы работы токенизатора:
\t https://docs.google.com/document/d/1Gid_PxCeHGWN-1C0KPWDV96rbDJrAW24ttxZ6b1kifs/edit?usp=sharing
  
reviews.txt \t 400 необработанных текстов рецензий
split_reviews.py \t разбивает тексты на отдельные файлы, убирает метаданные; создаётся папка "reviews"
clean_reviews.py \t нормализует тексты, убирет мусор; создаётся папка "reviews_clean"
tokenizer.py \t разбивает все тексты на токены
abbreviations.txt \t сокращения с точкой из корпуса
tokens.txt \t итоговый файл с токенами
