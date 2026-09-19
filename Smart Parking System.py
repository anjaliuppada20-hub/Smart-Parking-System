# Raspberry Pi GPIO example
# Change these GPIO numbers according to your circuit.

try:
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)

    DEVICES = {
        "light": 17,
        "fan": 27,
        "appliance": 22
    }

    for pin in DEVICES.values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

    REAL_HARDWARE = True

except ImportError:
    # Allows the program to run on a normal computer for testing.
    DEVICES = {
        "light": 17,
        "fan": 27,
        "appliance": 22
    }

    STATES = {
        "light": "off",
        "fan": "off",
        "appliance": "off"
    }

    REAL_HARDWARE = False


def get_devices():
    if REAL_HARDWARE:
        return {
            name: "on" if GPIO.input(pin) else "off"
            for name, pin in DEVICES.items()
        }

    return STATES.copy()


def set_device(name, state):
    if name not in DEVICES:
        return False

    if REAL_HARDWARE:
        GPIO.output(
            DEVICES[name],
            GPIO.HIGH if state == "on" else GPIO.LOW
        )
    else:
        STATES[name] = state

    return True
