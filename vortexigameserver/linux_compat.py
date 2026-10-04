import os

class MockRegistry:
    HKEY_LOCAL_MACHINE = None
    HKEY_CURRENT_USER = None
    KEY_READ = None
    KEY_SET_VALUE = None
    REG_SZ = None

    @staticmethod
    def OpenKey(*args, **kwargs):
        return None

    @staticmethod
    def QueryValueEx(key, name):
        try:
            with open("/tmp/vortexi_access_key", "r") as f:
                return f.read().strip(), None
        except FileNotFoundError:
            return "", None

    @staticmethod
    def SetValueEx(key, name, reserved, regtype, value):
        with open("/tmp/vortexi_access_key", "w") as f:
            f.write(value)

    @staticmethod
    def CloseKey(key):
        pass

class MockWin32GUI:
    WM_CLOSE = 16
    SW_MINIMIZE = 6

    @staticmethod
    def GetWindowText(hwnd):
        return ""

    @staticmethod
    def PostMessage(*args, **kwargs):
        pass

    @staticmethod
    def EnumWindows(callback, lparam):
        pass

    @staticmethod
    def ShowWindow(*args, **kwargs):
        pass

class MockWin32Con:
    WM_CLOSE = 16
    SW_MINIMIZE = 6
