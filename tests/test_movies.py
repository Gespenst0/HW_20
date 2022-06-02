from unittest.mock import MagicMock
import pytest
from dao.model.movie import Movie
from dao.movie import MovieDAO
from service.movie import MovieService
import os
from tests.test_genres import genre_dao
from tests.test_directors import director_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    movie_1 = Movie(id=1,
                    title="Омерзительная восьмерка",
                    description="США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке "
                                "Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько "
                                "путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, "
                                "где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, "
                                "ковбой… И один из них - не тот, за кого себя выдает.",
                    trailer="https://www.youtube.com/watch?v=lmB9VWm0okU",
                    year=2015,
                    rating=7.8)
    movie_2 = Movie(id=2,
                    title="Сияние",
                    description="Джек Торренс с женой и сыном приезжает в элегантный отдалённый отель, чтобы работать "
                                "смотрителем во время мертвого сезона. Торренс здесь раньше никогда не бывал. Или это "
                                "не совсем так? Ответ лежит во мраке, сотканном из преступного кошмара.",
                    trailer="https://www.youtube.com/watch?v=NMSUEhDWXH0",
                    year=1980,
                    rating=8.4)
    movie_3 = Movie(id=3,
                    title="Джанго освобожденный",
                    description="Эксцентричный охотник за головами, также известный как Дантист, промышляет отстрелом "
                                "самых опасных преступников. Работенка пыльная, и без надежного помощника ему не "
                                "обойтись. Но как найти такого и желательно не очень дорогого? Освобождённый им раб по "
                                "имени Джанго – прекрасная кандидатура. Правда, у нового помощника свои мотивы – кое с "
                                "чем надо сперва разобраться.",
                    trailer="https://www.youtube.com/watch?v=2Dty-zwcPv4",
                    year=2012,
                    rating=8.4)

    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_all = MagicMock(return_value=[movie_1, movie_2, movie_3])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock()
    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)

        assert movie is not None
        assert movie.id is not None
        assert movie.title is not None
        assert movie.description is not None
        assert movie.trailer is not None
        assert "https://www.youtube.com/" in movie.trailer
        assert movie.rating is not None
        assert movie.year is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movie_new = {
            "title": "Три билборда на границе Эббинга, Миссури",
            "description": "Потеряв дочь, героиня пытается достучаться до шерифа с помощью наружной рекламы",
            "trailer": "https://www.youtube.com/watch?v=3iRsvVne6zw",
            "year": "2017",
            "rating": "8.1"
        }

        movie = self.movie_service.create(movie_new)

        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        movie_up = {
            "id": "2",
            "title": "Три билборда на границе Эббинга, Миссури",
            "description": "Потеряв дочь, героиня пытается достучаться до шерифа с помощью наружной рекламы",
            "trailer": "https://www.youtube.com/watch?v=3iRsvVne6zw",
            "year": "2017",
            "rating": "8.1"
        }
        self.movie_service.update(movie_up)


if __name__ == "__main__":
    os.system("pytest")
