from DOMAIN.undo_redo_operation import UndoRedoOperation
from REPOSITORY.file_repository import FileRepository
class DeleteOperation(UndoRedoOperation):
    def __init__(self, repository: FileRepository, deleted_object):
        super().__init__(repository)
        self.__deleted_object = deleted_object

    def undo(self):
        self._repository.adauga(self.__deleted_object)

    def redo(self):
        self._repository.sterge(self.__deleted_object.id_entitate)