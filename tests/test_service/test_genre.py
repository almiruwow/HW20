from unittest.mock import MagicMock
import pytest
from dao.genre import GenreDAO
from service.genre import GenreService

@pytest.fixture
def genre_dao():
    genre = GenreDAO(None)
    genre.get_one = MagicMock()
    genre.get_all = MagicMock()
    genre.create = MagicMock()
    genre.update = MagicMock()
    genre.delete = MagicMock()

    return genre


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    parameters = (
        (
            1,
            {
                'id': 1,
                'name': "EntetyName"
            }
        ),
        (
            2,
            {
                'id': 2,
                'title': "EntetyName"
            }
        ),

    )

    @pytest.mark.parametrize('gid, genre', parameters)
    def test_get_one(self,gid,  genre):
        self.genre_service.dao.get_one.return_value = genre

        assert self.genre_service.get_one(gid) == genre

    parameters = (([{'id': 1, 'name': "Name1"}, {'id': 2, 'name': "Name2"}]),)

    @pytest.mark.parametrize('genre', parameters)
    def test_get_all(self, genre):

        self.genre_service.dao.get_all.return_value = genre

        assert self.genre_service.get_all() == genre

    parameters = (
        (1,
         {
             'id': 3,
             'name': "NewName"
         }
         ),
        (2,
         {
             'id': 4,
             'name': "NewName"
         }
         ),
    )

    @pytest.mark.parametrize('genre', parameters)
    def test_create(self, genre):
        self.genre_service.dao.create.return_value = genre
        assert self.genre_service.create(genre) == genre

    parameters = (
        (1,
         {
                'id': 3,
                'name': "NewName"
            }
         ),
        (2,
         {
                'id': 4,
                'name': "NewName"
            }
         ),
    )

    @pytest.mark.parametrize('origin_genre, new_genre', parameters)
    def test_update(self, origin_genre, new_genre):
        self.genre_service.dao.update.return_value = new_genre

        assert self.genre_service.update(new_genre) == new_genre

    def test_delete(self):
        self.genre_service.delete(1)
        self.genre_service.dao.delete.assert_called_once_with(1)
