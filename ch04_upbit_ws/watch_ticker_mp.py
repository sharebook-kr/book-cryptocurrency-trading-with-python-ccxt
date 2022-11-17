import ccxt.pro as ccxtpro
import asyncio
import multiprocessing as mp
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

async def ws_client(q):
    exchange = ccxtpro.upbit()

    while True:
        ticker = await exchange.watch_ticker(symbol="BTC/KRW")
        q.put(ticker)

def producer(q):
    asyncio.run(ws_client(q))

class Consumer(QThread):
    poped = pyqtSignal(dict)

    def __init__(self, q):
        super().__init__()
        self.q = q

    def run(self):
        while True:
            #if not self.q.empty():
            data = self.q.get()
            self.poped.emit(data)

class MyWindow(QMainWindow):
    def __init__(self, q):
        super().__init__()
        self.setGeometry(200, 200, 400, 200)
        self.setWindowTitle("Upbit Websocket with PyQt")

        self.consumer = Consumer(q)
        self.consumer.poped.connect(self.pop_data)
        self.consumer.start()

    @pyqtSlot(dict)
    def pop_data(self, data):
        close = int(data['close'])
        self.statusBar().showMessage(f"BTC/KRW {close: ,}")

if __name__ == "__main__":
    q = mp.Queue()
    p = mp.Process(name="Producer", target=producer, args=(q,), daemon=True)
    p.start()

    # MainProcess
    app = QApplication(sys.argv)
    win = MyWindow(q)
    win.show()
    app.exec_()





