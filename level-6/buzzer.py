import board
import pwmio
import time

buzzer = pwmio.PWMOut(board.GP18, variable_frequency=True)

OFF = 0
ON = 2**15

buzzer.duty_cycle = ON
buzzer.frequency = 262 # C4
time.sleep(1)
buzzer.frequency = 294 # D4
time.sleep(1)
buzzer.frequency = 330 # E4
time.sleep(1)
buzzer.frequency = 349 # F4
time.sleep(1)
buzzer.frequency = 392 # G4
time.sleep(1)
buzzer.frequency = 440 # A4
time.sleep(1)
buzzer.frequency = 494 # B4
time.sleep(1)
buzzer.duty_cycle = OFF
