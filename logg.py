import logging
import time
from pymodbus.client import ModbusTcpClient

TesleadSmartSyncX = None

def hmi_sync():
    global TesleadSmartSyncX
    # ip_address = teslead_db.execute("select ip_address from master_ip_address;").fetchone()[0]
    TesleadSmartSyncX = ModbusTcpClient('127.0.0.1')
    TesleadSmartSyncX.connect()
hmi_sync()

# Configure logging
logging.basicConfig(filename='microseconds_log.log', level=logging.INFO, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Function to log messages every microsecond
def log_microseconds():
    global TesleadSmartSyncX
    while True:
        logging.info(TesleadSmartSyncX.read_holding_registers(2000, 1).registers[0])
        # print(TesleadSmartSyncX.read_holding_registers(2000, 1).registers[0])
        time.sleep(1e-6)  # Sleep for 1 microsecond

if __name__ == "__main__":
    log_microseconds()