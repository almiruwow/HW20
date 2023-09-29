from unittest.mock import MagicMock
import pytest
from dao.director import DirectorDAO
from service.director import DirectorService

@pytest.fixture
def director_dao():
    director = DirectorDAO(None)
    director.get_one = MagicMock()
    director.get_all = MagicMock()
    director.create = MagicMock()
    director.update = MagicMock()
    director.delete = MagicMock()

    return director


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.director_service = DirectorService(dao=director_dao)

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

    @pytest.mark.parametrize('did, director', parameters)
    def test_get_one(self, did,  director):
        self.director_service.dao.get_one.return_value = director

        assert self.director_service.get_one(did) == director

    parameters = (([{'id': 1, 'name': "Name1"}, {'id': 2, 'name': "Name2"}]),)

    @pytest.mark.parametrize('director', parameters)
    def test_get_all(self, director):

        self.director_service.dao.get_all.return_value = director

        assert self.director_service.get_all() == director

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

    @pytest.mark.parametrize('director', parameters)
    def test_create(self, director):
        self.director_service.dao.create.return_value = director
        assert self.director_service.create(director) == director

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

    @pytest.mark.parametrize('origin_director, new_director', parameters)
    def test_update(self, origin_director, new_director):
        self.director_service.dao.update.return_value = new_director

        assert self.director_service.update(new_director) == new_director

    def test_delete(self):
        self.director_service.delete(1)
        self.director_service.dao.delete.assert_called_once_with(1)
