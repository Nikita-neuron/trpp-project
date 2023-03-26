import json


class DataBase:
    """
    Данный класс работает с базой данных
    В качестве параметра принимает путь до базы данных в виде json файла
    """
    def __init__(self, db_file: str):
        self.db_file = db_file

        with open(self.db_file, 'r', encoding="utf-8") as file:
            self.data = json.load(file)

    def get_all_questions(self) -> list:
        """Получение всех вопросов из базы данных"""
        return self.data

    def get_questions_by_level(self, level: int) -> list:
        """Получение вопросов по указанному уровню"""
        questions = []
        for question in self.data:
            if question['level'] == level:
                questions.append(question)
        return questions
