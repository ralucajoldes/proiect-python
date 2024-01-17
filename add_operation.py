from DOMAIN.undo_redo_operation import UndoRedoOperation
from REPOSITORY.file_repository import FileRepository
class AddOperation(UndoRedoOperation):
    def __init__(self, repository: FileRepository, added_object):
        super().__init__(repository)
        self.__added_object = added_object

    def undo(self):
        self._repository.sterge(self.__added_object.id_entitate)

    def redo(self):
        self._repository.adauga(self.__added_object)