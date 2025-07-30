from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt, QPersistentModelIndex
from models.device import Device


class MonthlyDeviceTableModel(QAbstractTableModel):
    def __init__(self, devices: list[Device], total_consumption: list[float]) -> None:
        super().__init__()
        self.__devices = devices
        self.__total_consumption = total_consumption

        self.__headers = ["День"]

        for device in devices:
            self.__headers.extend([
                f"{device.sn}\nЗгенеровано\nелектроенергії\nвід сонця кВт",
                f"{device.sn}\nЗаряд АКБ\nкВт",
                f"{device.sn}\nРозряд АКБ\nкВт",
                f"{device.sn}\nСпожито кВт",
            ])

        self.__headers.extend([
            "Спожито\nзагалом кВт",
        ])

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()) -> int:
        return 31

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex = QModelIndex()) -> int:
        return len(self.__headers)

    def data(self, index, role: int = Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            row = index.row()
            col = index.column()

            if col == 0:
                return str(row + 1)

            data_col = col - 1
            device_index = data_col // 4
            data_type = data_col % 4

            if device_index < len(self.__devices):
                device = self.__devices[device_index]

                data_type_value = ""

                match data_type:
                    case 0:
                        data_type_value = f"{device.generation[row]:.1f}" if device.generation[row] != 0 else "0"
                    case 1:
                        data_type_value = f"{device.charge_energy[row]:.1f}" if device.charge_energy[row] != 0 else "0"
                    case 2:
                        data_type_value = f"{device.discharge_energy[row]:.1f}" if device.discharge_energy[row] != 0 else "0"
                    case 3:
                        data_type_value = f"{device.consumption[row]:.1f}" if device.consumption[row] != 0 else "0"

                return data_type_value

            if col == len(self.__headers) - 1:
                return f"{self.__total_consumption[row]:.1f}" if self.__total_consumption[row] != 0 else "0"

        elif role == Qt.ItemDataRole.TextAlignmentRole:
            return Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter

        return None

    def headerData(self, section, orientation, role: int = Qt.ItemDataRole.DisplayRole):
        if orientation == Qt.Orientation.Horizontal and role == Qt.ItemDataRole.DisplayRole:
            return self.__headers[section]
        if orientation == Qt.Orientation.Vertical and role == Qt.ItemDataRole.DisplayRole:
            return ""
        return None
