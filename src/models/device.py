from PySide6.QtCore import QObject


class Device(QObject):
    def __init__(self, sn: str, generation: list[float], consumption: list[float], charge: list[float], discharge: list[float]) -> None:
        super().__init__()
        self.__sn = sn

        self.__generation = generation
        self.__consumption = consumption
        self.__charge_energy = charge
        self.__discharge_energy = discharge

    @property
    def sn(self) -> str:
        return self.__sn

    @property
    def generation(self) -> list[float]:
        return self.__generation

    @property
    def consumption(self) -> list[float]:
        return self.__consumption

    @property
    def charge_energy(self) -> list[float]:
        return self.__charge_energy

    @property
    def discharge_energy(self) -> list[float]:
        return self.__discharge_energy