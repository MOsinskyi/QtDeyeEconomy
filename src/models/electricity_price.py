import xlwings as xw
from PySide6.QtCore import QObject, QDate

from utils import DATE_FORMAT, get_resource_path


class ElectricityPrice(QObject):
    def __init__(self):
        super().__init__()

        self._prices: list[float] = []
        self._app = xw.App(visible=False)
        self._workbook = self._app.books.open(get_resource_path("ElectricityPrices.xlsx"), read_only=True)
        self._worksheet = self._workbook.sheets[0]

    def get_prices(self, target_date: str) -> list[float]:
        date: str = QDate.fromString(target_date, DATE_FORMAT).toString("dd.MM.yyyy")
        self._workbook.api.RefreshAll()

        last_row: int = self._worksheet.range("A" + str(self._worksheet.cells.last_cell.row)).end("up").row

        for row_num in range(1, last_row + 1):
            cell_value = self._worksheet.range(f"A{row_num}").value

            if cell_value == date:
                price_range = self._worksheet.range(f"B{row_num}:Y{row_num}").value
                for price in price_range:
                    self._prices.append(float(price / 1000))


        return self._prices

    def _close(self) -> None:
        self._workbook.close()

    def quit(self) -> None:
        self._close()
        xw.apps.active.quit()

