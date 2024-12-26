class Memento:
    def __init__(self, state) -> None:
        self._state = state.copy()

    def get_state(self) -> dict:
        return self._state
