class InvalidControlException(Exception):
    """Raised when an invalid control action is requested."""
    pass


class InvalidDeviceStateException(Exception):
    """Raised when a device is in an invalid state for the requested operation."""
    pass
