class Student:
    def __init__(self, name: str, surname: str, group: int, year_of_birth: int, rating: int):
        self.name = name
        self.surname = surname
        self.group = group
        self.year_of_birth = year_of_birth
        self.rating = rating

    def __str__(self) -> str:
        return f"Name: {self.name}, rating: {self.rating}, group:{self.group}"




