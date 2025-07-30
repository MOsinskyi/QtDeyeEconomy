import asyncio
from datetime import datetime, timedelta

import xlwings as xw
from PySide6.QtCore import QObject, QDate

from utils import get_resource_path


async def wait_for_refresh_complete(wb, timeout_seconds=300):
    """
    Wait for all web resources to refresh in Excel workbook
    """
    # Start the refresh
    wb.api.RefreshAll()

    start_time = datetime.now()
    timeout = timedelta(seconds=timeout_seconds)

    while datetime.now() - start_time < timeout:
        # Check if any queries are still refreshing
        try:
            # Check WorkbookConnection objects
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

        except Exception as e:
            print(f"Error checking refresh status: {e}")

        # Wait before checking again
        await asyncio.sleep(1)

    return False  # Timeout reached

class ElectricityPrice(QObject):
    def __init__(self):
        super().__init__()

        self._prices: list[float] = []
        self._app = xw.App(visible=False)
        self._workbook = self._app.books.open(get_resource_path("ElectricityPrices.xlsx"), read_only=True)
        self._worksheet = self._workbook.sheets[0]
        self._already_updated = False

    async def get_prices(self, target_date: str) -> list[float]:
        date: str = QDate.fromString(target_date, "yyyy-MM-dd").toString("dd.MM.yyyy")

        if not self._already_updated:
            await wait_for_refresh_complete(self._workbook)
            self._already_updated = True

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

