from DOMAIN.undo_redo_operation import UndoRedoOperation
from REPOSITORY.file_repository import FileRepository
class UpdateOperation(UndoRedoOperation):
    def __init__(self, repository: FileRepository, updated_object,unchanged_object):
        super().__init__(repository)
        self.__updated_object = updated_object
        self.__unchanged_object=unchanged_object

    def undo(self):
        self._repository.modifica(self.__unchanged_object)

    def redo(self):
        self._repository.modifica(self.__updated_object)