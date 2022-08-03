import smbus
import time


class ads1115:
    def __init__(self, address):
          self.bus = smbus.SMBus(0)
          self.pins_addresses = [[0xC4,0x83], [0xD4,0x83], [0xE4,0x83], [0xF4,0x83]]

    def read_pin_raw(self, pin):
        self.bus.write_i2c_block_data(0x48, 0x01, self.pins_addresses[pin])
        time.sleep(0.5)
        response = self.bus.read_i2c_block_data(0x48, 0x00, 2)
        return response

    def read_pin_converted(self, pin):
        response = self.read_pin_raw(pin)
        raw_data = response[0] * 256 + response[1]

        if raw_data > 32767:
            raw_data -= 65535
    
        return raw_data