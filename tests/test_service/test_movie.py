from unittest.mock import MagicMock
import pytest
from dao.movie import MovieDAO
from service.movie import MovieService

@pytest.fixture
def movie_dao():
    movie = MovieDAO(None)
    movie.get_one = MagicMock()
    movie.get_all = MagicMock()
    movie.create = MagicMock()
    movie.update = MagicMock()
    movie.delete = MagicMock()

    return movie


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    parameters = (
        (
            1,
            {
                'id': 1,
                'title': "Title1"
            }
        ),
        (
            2,
            {
                'id': 2,
                'title': "Title2"
            }
        ),

    )

    @pytest.mark.parametrize('mid, movie', parameters)
    def test_get_one(self,mid,  movie):
        self.movie_service.dao.get_one.return_value = movie

        assert self.movie_service.get_one(mid) == movie

    parameters = (([{'id': 1, 'title': "Title1"}, {'id': 2, 'title': "Title2"}]),)

    @pytest.mark.parametrize('movie', parameters)
    def test_get_all(self, movie):

        self.movie_service.dao.get_all.return_value = movie

        assert self.movie_service.get_all() == movie

    parameters = (
        (1,
         {
             'id': 3,
             'title': "NewTitle"
         }
         ),
        (2,
         {
             'id': 4,
             'title': "NewTitle"
         }
         ),
    )

    @pytest.mark.parametrize('movie', parameters)
    def test_create(self, movie):
        self.movie_service.dao.create.return_value = movie
        assert self.movie_service.create(movie) == movie

    parameters = (
        (1,
         {
                'id': 3,
                'title': "NewTitle"
            }
         ),
        (2,
         {
                'id': 4,
                'title': "NewTitle"
            }
         ),
    )

    @pytest.mark.parametrize('origin_movie, new_mov', parameters)
    def test_update(self, origin_movie, new_mov):
        self.movie_service.dao.update.return_value = new_mov

        assert self.movie_service.update(new_mov) == new_mov

    def test_delete(self):
        self.movie_service.delete(1)
        self.movie_service.dao.delete.assert_called_once_with(1)
