def get_setting(settings: dict[str, str], name: str, default: str = "") -> str:
    try:
        return settings[name]
    except KeyError:
        return default
