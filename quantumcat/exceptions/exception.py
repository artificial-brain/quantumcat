class QuantumCatError(Exception):
    """Base class for other exceptions"""
    def __init__(self, *message):
        """Set the error message."""
        super().__init__(' '.join(message))
        self.message = ' '.join(message)

    def __str__(self):
        """Return the message."""
        return repr(self.message)


class QuantumCatIndexError(QuantumCatError, IndexError):
    """Raised when a sequence subscript is out of range."""
    pass
