import json


class DataBase:
    """
    This class works with the database
    As a parameter, it takes the path to the database in the form of a json file
    """

    def __init__(self, db_file: str):
        self.db_file = db_file

        with open(self.db_file, 'r', encoding="utf-8") as file:
            self.data = json.load(file)

    def get_all_questions(self) -> list:
        """Getting all questions from the database"""
        return self.data

    def get_questions_by_level(self, level: int) -> list:
        """Receive questions at a specified level"""
        questions = []
        for question in self.data:
            if question['level'] == level:
                questions.append(question)
        return questions
