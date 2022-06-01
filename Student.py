class Student:
    def __init__(self, name: str, surname: str, group: int, year_of_birth: int, rating: int):
        self._name = name
        self._surname = surname
        self._group = group
        self._year_of_birth = year_of_birth
        self._rating = rating

    def __str__(self) -> str:
        return f"Name: {self._name}, rating: {self._rating}, group:{self._group}"

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        self._rating = rating
    #
    @property
    def group(self):
        return self._group



