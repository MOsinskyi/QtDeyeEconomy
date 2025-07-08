from PySide6.QtCore import QObject


class Device(QObject):
    def __init__(self, sn: str, gen: list[float], consumption: list[float], charge: list[float], discharge: list[float]):
        super().__init__()
        self._sn: str = sn

        self._generation: list[float] = gen
        self._consumption: list[float] = consumption
        self._charge_energy: list[float] = charge
        self._discharge_energy: list[float] = discharge

    @property
    def sn(self) -> str:
        return self._sn

    @property
    def generation(self) -> list[float]:
        return self._generation

    @property
    def consumption(self) -> list[float]:
        return self._consumption

    @property
    def charge_energy(self) -> list[float]:
        return self._charge_energy

    @property
    def discharge_energy(self) -> list[float]:
        return self._discharge_energy