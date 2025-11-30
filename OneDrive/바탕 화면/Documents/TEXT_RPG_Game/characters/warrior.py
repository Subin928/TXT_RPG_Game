from .character import Character

class Warrior(Character):
    def __init__(self, name="전사", level=1):
        super().__init__(name, level, health=100, attack_power=15)

    def attack(self, target):
        """기본 공격"""
        damage = self.attack_power
        print(f"{self.name}의 일반 공격! {target.get_name()}에게 {damage}의 피해!")
        target.take_damage(damage)

    def special_attack(self, target):
        """특수 공격"""
        damage = self.attack_power * 2
        print(f"{self.name}의 강력한 일격! {target.get_name()}에게 {damage}의 피해!")
        target.take_damage(damage)

        # 자신도 피해를 입음
        self.take_damage(5)
        print(f"{self.name}은(는) 반동으로 5의 피해를 입었습니다.")