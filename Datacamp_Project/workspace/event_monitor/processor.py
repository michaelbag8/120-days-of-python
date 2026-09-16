"""Event processing classes."""
import pandas as pd
from config import SEVERITY_LEVELS


class EventProcessor:
    """Filter server events by minimum severity level."""

    def __init__(self, events, min_severity="INFO"):
        self.events = events
        self.min_severity = min_severity
        self._processed = None

    def process(self):
        """Filter events at or above min_severity, sorted by timestamp."""
        threshold = SEVERITY_LEVELS.get(self.min_severity, 0)
        self._processed = [
            e for e in self.events
            if SEVERITY_LEVELS.get(e.get("severity", ""), 0) >= threshold
        ]
        self._processed.sort(key=lambda e: e.get("timestamp", ""))
        return self._processed


class AlertProcessor(EventProcessor):
    """Process events and flag alerts."""

    def __init__(self, events, min_severity="WARNING"):
        super().__init__(events, min_severity)

    def process(self):
        filtered = super().process()
        for event in filtered:
            event["is_alert"] = event.get("severity", "") in ("ERROR", "CRITICAL")
        return filtered


class BatchProcessor(EventProcessor):
    """Process events loaded from multiple CSV log files.

    You may assume each CSV file is well-formed: correct columns,
    valid severity values, and no missing fields.

    Parameters
    ----------
    file_paths : list[str]
        Paths to CSV log files.
    min_severity : str
        Minimum severity to include. Default is "INFO".

    The process() method should:
    1. Load each CSV file using pd.read_csv.
    2. Convert each DataFrame to a list of dicts.
    3. Combine all events into self.events.
    4. Filter to events at or above min_severity.
    5. Sort the filtered events by severity descending (most severe
       first), then by timestamp ascending (earliest first) within
       each severity level.
    Return the filtered, sorted list.

    Also implement:
    - __len__: return the number of processed events. Return 0 if
      process() has not yet been called.
    - __repr__: return a string in the format
      "BatchProcessor(<n> files, <m> events processed)"
      where <n> is the number of file paths and <m> is the number of
      processed events (0 if not yet processed).
    """
    pass
