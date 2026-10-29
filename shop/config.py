def get_setting(name:str,settings:dict[str,str],default:str='') -> str:
    try:
        return settings[name]
    except KeyError:
        return default
