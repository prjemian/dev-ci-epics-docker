"""
test the connection with the EPICS IOC
"""

import ophyd
# import pytest

IOC = "gp:"


def test_uptime_connection():
    uptime = ophyd.EpicsSignalRO(f"{IOC}UPTIME", name="uptime")
    uptime.wait_for_connection()
    assert uptime.connected


def test_motors():
    for i in range(56):
        motor = ophyd.EpicsMotor(f"{IOC}m{i+1}", name="motor")
        motor.wait_for_connection()
        assert motor.position == 0.0, f"motor {i+1}"
