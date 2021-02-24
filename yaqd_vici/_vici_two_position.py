__all__ = ["ViciTwoPosition"]

import asyncio
from typing import Dict, Any, List

from yaqd_core import IsDiscrete, HasPosition, IsDaemon


class ViciTwoPosition(IsDiscrete, HasPosition, IsDaemon):
    _kind = "vici-two-position"

    def __init__(self, name, config, config_filepath):
        super().__init__(name, config, config_filepath)
        # Perform any unique initialization


    def _set_position(self, position):
        ...


    async def update_state(self):
        """Continually monitor and update the current daemon state."""
        # If there is no state to monitor continuously, delete this function
        while True:
            # Perform any updates to internal state
            self._busy = False
            # There must be at least one `await` in this loop
            # This one waits for something to trigger the "busy" state
            # (Setting `self._busy = True)
            # Otherwise, you can simply `await asyncio.sleep(0.01)`
            await self._busy_sig.wait()
