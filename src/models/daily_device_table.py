from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt

from models.device import Device


class DailyDeviceTableModel(QAbstractTableModel):
    def __init__(self, devices: list[Device], total_consumption: list[float], price_per_kwh: list[float]) -> None:
        super().__init__()
        self._devices: list[Device] = devices
        self._total_consumption: list[float] = total_consumption
        self._price_per_kwh: list[float] = price_per_kwh

        self._headers = ["Година"]

        for device in devices:
            self._headers.extend([
                f"{device.sn}\nЗгенеровано\nелектроенергії\nвід сонця кВт",
                f"{device.sn}\nЗаряд АКБ\nкВт",
                f"{device.sn}\nРозряд АКБ\nкВт",
                f"{device.sn}\nСпожито з\nмережі кВт",
            ])

        self._headers.extend([
            "Спожито\nзагалом кВт",
            "Ціна за кВт\nРДН"
        ])

    def rowCount(self, parent=QModelIndex()) -> int:
        return 24

    def columnCount(self, parent=QModelIndex()) -> int:
        return len(self._headers)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            row = index.row()
            col = index.column()

            if col == 0:
                return str(row + 1)

            data_col = col - 1
            device_index = data_col // 4
            data_type = data_col % 4

            if device_index < len(self._devices):
                device = self._devices[device_index]

                if data_type == 0:
                    return f"{device.generation[row]:.1f}" if device.generation[row] != 0 else "0"
                elif data_type == 1:
                    return f"{device.charge_energy[row]:.1f}" if device.charge_energy[row] != 0 else "0"
                elif data_type == 2:
                    return f"{device.discharge_energy[row]:.1f}" if device.discharge_energy[row] != 0 else "0"
                elif data_type == 3:
                    return f"{device.consumption[row]:.1f}" if device.consumption[row] != 0 else "0"

            elif col == len(self._headers) - 2:
                return f"{self._total_consumption[row]:.1f}" if self._total_consumption[row] != 0 else "0"

            elif col == len(self._headers) - 1:
                try:
                    return f"{self._price_per_kwh[row]:.2f} ₴"
                except IndexError:
                    return "Немає даних"

        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight | Qt.AlignVCenter

        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._headers[section]
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return ""
        return None
