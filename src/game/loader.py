import importlib


class ModuleInterface:
    
    @staticmethod
    def register() -> None:
        raise NotImplementedError()
    
def import_module(module_name: str) -> ModuleInterface:
    module = importlib.import_module(module_name)
    return module # type: ignore

def load_modules(plugins : list[str]) -> None:
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.register()