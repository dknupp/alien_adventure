import textwrap

class Locations(object):
    """Base class for a room."""

    def __init__(self, description, long_description, items=None):
        self.description = description
        self.long_description = long_description
        self.items = []
        self.encloses = []
        self.enclosed_by = []

        if items is not None:
          self.items = items

PLACES = {
    "medical lab": Place(
        description="the medical lab",
        long_description=textwrap.dedent('''\
        You're in the medical lab for the ship. The room smells slightly
        antiseptic. Along one wall is a row of beds. In the corner of the room
        is a desk. Against the far wall is a tall medicine cabinet.
        '''),
        encloses=["chief medical officer's desk", "tall medicine cabinet"]
    ),
}