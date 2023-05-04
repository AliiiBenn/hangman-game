


class InvalidMonsterAnimation(Exception):
    def __init__(self, monster_name : str, animation_name : str) -> None:
        self.monster_name = monster_name
        self.animation_name = animation_name
        super().__init__(f"Invalid monster animation: {monster_name}_{animation_name}")