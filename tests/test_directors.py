from unittest.mock import MagicMock
import pytest
from dao.model.director import Director
from dao.director import DirectorDAO
from service.director import DirectorService
import os


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    director_1 = Director(id=1, name='Тейлор Шеридан')
    director_2 = Director(id=2, name='Квентин Тарантино')
    director_3 = Director(id=3, name='Владимир Вайншток')

    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = MagicMock(return_value=[director_1, director_2, director_3])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.delete = MagicMock()
    director_dao.update = MagicMock()
    return director_dao


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)

        assert director is not None
        assert director.id is not None
        assert director.name is not None

    def test_get_all(self):
        directors = self.director_service.get_all()

        assert len(directors) > 0

    def test_create(self):
        director_new = {
            "name": "Кристофер Нолан"
        }

        director = self.director_service.create(director_new)

        assert director.id is not None

    def test_delete(self):
        self.director_service.delete(1)

    def test_update(self):
        director_up = {
            "id": 2,
            "name": "Федор Бондарчук"
        }
        self.director_service.update(director_up)


if __name__ == "__main__":
    os.system("pytest")
