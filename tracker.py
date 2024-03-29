from ByteTrack.yolox.tracker.byte_tracker import BYTETracker
from dataclasses import dataclass

@dataclass(frozen=True)
class BYTETrackerArgs:
  track_thresh: float = 0.25
  track_buffer: int = 30
  match_thresh: float = 0.8
  aspect_ratio_thresh: float = 3.0
  min_box_area: float = 1.0
  mot20: bool = False
    
byte_tracker = BYTETracker(BYTETrackerArgs())