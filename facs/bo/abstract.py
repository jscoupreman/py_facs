from datetime import datetime, timezone, timedelta
from dateutil import parser
from facs.entity.timeline import TimelineEntity


class AbstractBo():
    _PARTITION_MBR = 'mbr'
    _PARTITION_GPT = 'gpt'

    _STORAGE_INTERNAL_DRIVE = 'internal storage'
    _STORAGE_EXTERNAL_DRIVE = 'uas_mass_storage'
    _STORAGE_MSC = 'usb_mass_storage'
    _STORAGE_MTP = 'mtp'
    _STORAGE_VIRTUAL = 'virtual_drive'

    _STORAGE_DRIVERS = {
        _STORAGE_EXTERNAL_DRIVE: 'uaspstor.inf',
        _STORAGE_MSC: 'usbstor.inf',
        _STORAGE_MTP: 'wpdmtp.inf',
    }

    def __init__(self):
        pass

    def _append_to_timeline(self, event: TimelineEntity, timeline):
        if event is None:
            return timeline

        # ensure no duplicates
        formatted = event.to_dict()
        if formatted not in timeline:
            timeline.append(formatted)

        return timeline

    def _systemtime_to_datetime(self, systemtime: bytes):
        chunks = []
        for i in range(0, len(systemtime) - 1, 2):
            chunks.append(systemtime[i:i+2][::-1])

        year = int.from_bytes(chunks[0], byteorder='big', signed=False)
        month = int.from_bytes(chunks[1], byteorder='big', signed=False)
        day = int.from_bytes(chunks[3], byteorder='big', signed=False)
        hour = int.from_bytes(chunks[4], byteorder='big', signed=False)
        minute = int.from_bytes(chunks[5], byteorder='big', signed=False)
        second = int.from_bytes(chunks[6], byteorder='big', signed=False)
        microsec = int.from_bytes(chunks[7], byteorder='big', signed=False)

        return datetime(year, month, day, hour, minute, second, microsec, timezone.utc)

    def _filetime_to_datetime(self, filetime: int):
        if filetime == 0:
            return None

        try:
            dt = datetime(1601, 1, 1, tzinfo=timezone.utc) + timedelta(microseconds=filetime/10)
        except OverflowError:
            # because sometimes the value is just shit ^^
            return None
        return dt

    def _unixepoch_to_datetime(self, timestamp: int):
        return datetime.fromtimestamp(timestamp, timezone.utc)

    def _isoformat_to_datetime(self, dt: str):
        return parser.isoparse(dt)
