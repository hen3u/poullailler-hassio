from homeassistant.helpers.discovery import load_platform
DOMAIN = 'myrcdoor'

DATA_MRCD = 'MRCD'

def setup(hass, config):
    """Your controller/hub specific code."""
    hass.data[DATA_MRCD] = SomeObjectToInitialiseGlobal()
