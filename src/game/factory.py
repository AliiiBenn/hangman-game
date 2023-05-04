from typing import Callable, Any


creation_functions : dict[str, Callable[..., Any]] = {}


def register(type_name : str, creation_function : Callable[..., Any]) -> None:
    creation_functions[type_name] = creation_function
    
def unregister(type_name : str) -> None:
    creation_functions.pop(type_name)
    
def create(arguments : dict[str, Any]) -> Any:
    args_copy = arguments.copy()
    type_name = args_copy.pop("type")
    try:
        creation_function = creation_functions[type_name]
    except KeyError:
        raise ValueError(f"Unknown type {type_name}")
    
    return creation_function(**args_copy)