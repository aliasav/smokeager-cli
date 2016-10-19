import os


class TestInitiation():

    home_path = os.path.expanduser("~")

    def test_smokeager_directory_exists(self):
        assert os.path.isdir(self.home_path + "/.smokeager") == True

    def test_smokeagerDB_is_created(self):
        assert os.path.isfile(self.home_path + "/.smokeager/smokeagerDB.db") == True
