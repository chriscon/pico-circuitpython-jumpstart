import microcontroller
import struct

# https://docs.circuitpython.org/en/latest/shared-bindings/microcontroller/index.html#microcontroller.Processor.uid
board_id = int.from_bytes(microcontroller.cpu.uid, "little")

print(f"CPU ID: {board_id}")
