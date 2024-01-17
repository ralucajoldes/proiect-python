from DOMAIN.undo_redo_operation import UndoRedoOperation
class UndoRedoService:
    def __init__(self):
        self.__undo_stack = []
        self.__redo_stack = []

    def add_to_undo(self,operation: UndoRedoOperation):
        self.__undo_stack.append(operation)

    def add_to_redo(self,operation: UndoRedoOperation):
        self.__redo_stack.append(operation)

    def do_undo(self):
        if len(self.__undo_stack) > 0:
            operation=self.__undo_stack.pop()
            self.add_to_redo(operation)
            operation.undo()

    def do_redo(self):
        if len(self.__redo_stack) > 0:
            operation=self.__redo_stack.pop()
            self.add_to_undo(operation)
            operation.redo()
