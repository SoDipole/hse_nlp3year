Сложности/особенности корпуса, принципы работы токенизатора:
https://docs.google.com/document/d/1Gid_PxCeHGWN-1C0KPWDV96rbDJrAW24ttxZ6b1kifs/edit?usp=sharing

- reviews.txt - 400 необработанных текстов рецензий
- split_reviews.py - разбивает тексты на отдельные файлы, убирает метаданные; создаётся папка "reviews"
- clean_reviews.py - нормализует тексты, убирет мусор; создаётся папка "reviews_clean"
- tokenizer.py - разбивает все тексты на токены
- abbreviations.txt - сокращения с точкой из корпуса
- tokens.txt - итоговый файл с токенами
