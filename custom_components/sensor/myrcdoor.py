import custom_components.myrcdoor as myrcdoor
from homeassistant.helpers.entity import Entity

def setup_platform(hass, config, add_devices, discovery_info=None):
    """Your switch/light specific code."""
    add_devices([ExampleSensor()])


class ExampleSensor(Entity):
    """Representation of a Sensor."""

    def __init__(self):
        """Initialize the sensor."""
        self._state = None

    @property
    def name(self):
        """Return the name of the sensor."""
        return 'Etat'

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state

    def update(self):
        """Fetch new state data for the sensor.

        This is the only method that should fetch new data for Home Assistant.
        """
        self._state = "Ouvert"
