from enum import Enum


class DeviceType(str, Enum):
    IP_CAMERA = "IP_CAMERA"
    NVR = "NVR"
    DVR = "DVR"
    RTSP_SOURCE = "RTSP_SOURCE"
    USB_CAMERA = "USB_CAMERA"


class DeviceStatus(str, Enum):
    UNKNOWN = "UNKNOWN"
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"
    CONNECTING = "CONNECTING"
    ERROR = "ERROR"


class StreamType(str, Enum):
    MAIN = "MAIN"
    SUB = "SUB"


class StreamProtocol(str, Enum):
    RTSP = "RTSP"
    HTTP = "HTTP"