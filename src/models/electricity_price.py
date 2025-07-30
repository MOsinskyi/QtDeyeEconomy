import asyncio

from datetime import datetime, timedelta
import xlwings as xw
from PySide6.QtCore import QObject, QDate
from utils import get_resource_path

async def wait_for_refresh_complete(wb, timeout_seconds=300):
    wb.api.RefreshAll()

    start_time = datetime.now()
    timeout = timedelta(seconds=timeout_seconds)

    while datetime.now() - start_time < timeout:
        try:
            still_refreshing = False
            for connection in wb.api.Connections:
                if hasattr(connection, 'OLEDBConnection'):
                    if connection.OLEDBConnection.Refreshing:
                        still_refreshing = True
                        break
                elif hasattr(connection, 'ODBCConnection'):
                    if connection.ODBCConnection.Refreshing:
                        still_refreshing = True
                        break

            if not still_refreshing:
                return True

        except (AttributeError, RuntimeError) as e:
            print(f"Error checking refresh status: {e}")

        await asyncio.sleep(1)

    return False


class ElectricityPrice(QObject):
    def __init__(self):
        super().__init__()

        self.__prices = []
        self.__app = xw.App(visible=False)
        self.__workbook = self.__app.books.open(get_resource_path("ElectricityPrices.xlsx"), read_only=True)
        self.__worksheet = self.__workbook.sheets[0]
        self.__already_updated = False

    async def get_prices(self, target_date: str) -> list[float]:
        date = QDate.fromString(target_date, "yyyy-MM-dd").toString("dd.MM.yyyy")

        if not self.__already_updated:
            await wait_for_refresh_complete(self.__workbook)
            self.__already_updated = True

        last_row = self.__worksheet.range("A" + str(self.__worksheet.cells.last_cell.row)).end("up").row

        for row_num in range(1, last_row + 1):
            cell_value = self.__worksheet.range(f"A{row_num}").value

            if cell_value == date:
                price_range = self.__worksheet.range(f"B{row_num}:Y{row_num}").value
                for price in price_range:
                    self.__prices.append(float(price / 1000))
        return self.__prices

    def quit(self) -> None:
        self.__close()
        if xw.apps.active is not None:
            xw.apps.active.quit()

    def __close(self) -> None:
        self.__workbook.close()

