from src.use_case.my_usecase import MyUsecase
from src.database.some_database_1 import Database1

use_case = MyUsecase(Database1())

use_case.search_something()
use_case.insert_something()
