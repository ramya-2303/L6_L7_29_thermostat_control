
from thermostat_control import target_temperature, hvac_action, energy_alert


# TARGET TEMPERATURE TESTS

def test_away():
    assert target_temperature("away", True, 12) == 16

def test_sleep_before_6():
    assert target_temperature("sleep", True, 5) == 18

def test_sleep_after_22():
    assert target_temperature("sleep", True, 22) == 18

def test_sleep_daytime():
    assert target_temperature("sleep", True, 12) == 20

def test_unoccupied():
    assert target_temperature("home", False, 12) == 18

def test_morning():
    assert target_temperature("home", True, 7) == 22

def test_evening():
    assert target_temperature("home", True, 18) == 21

def test_normal_temperature():
    assert target_temperature("home", True, 12) == 20


# HVAC ACTION TESTS

def test_idle():
    assert hvac_action(20, 20.5, 15) == "idle"

def test_heat_boost():
    assert hvac_action(18, 22, 2) == "heat_boost"

def test_heat():
    assert hvac_action(18, 22, 15) == "heat"

def test_cool_boost():
    assert hvac_action(25, 20, 35) == "cool_boost"

def test_cool():
    assert hvac_action(25, 20, 20) == "cool"


# ENERGY ALERT TESTS

def test_no_readings():
    assert energy_alert([], 10) == "ok"

def test_no_reading_over_limit():
    assert energy_alert([5, 8, 10], 10) == "ok"

def test_warning():
    assert energy_alert([15, 5, 6, 7], 10) == "warning"

def test_critical():
    assert energy_alert([15, 16, 17, 5], 10) == "critical"
