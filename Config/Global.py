class ConfigurationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            cls._instance._settings = {}
        return cls._instance

    def set_setting(self, key: str, value: any) -> None:
        self._settings[key] = value

    def get_setting(self, key: str) -> any:
        return self._settings.get(key)

    def remove_setting(self, key: str) -> None:
        if key in self._settings:
            del self._settings[key]

    def list_settings(self) -> None:
        for key, value in self._settings.items():
            print(f"{key}: {value}")
