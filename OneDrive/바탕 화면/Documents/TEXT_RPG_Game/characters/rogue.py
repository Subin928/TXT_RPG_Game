import random
from .character import Character

class Rogue(Character):
    def __init__(self, name="도적", level = 1):
        super().__init__(name, level, health = 90, attack_power = 12)

    def attack(self, target):
        """기본 공격"""
        damage = self.attack_power
        print(f"{self.name}의 빠른 공격! {target.get_name()}에게 {damage}의 피해!")
        target.take_damage(damage)

    def special_attack(self, target):
        """특수 공격: 급습 (70% 확률로 3배 데미지)"""
        if random.random() < 0.7:     # 70% 확률
            damage = self.attack_power * 3
            print(f"{self.name}의 급습 성공! {target.get_name()}에게 {damage}의 치명타!")
            target.take_damage(damage)

        else:
            print(f"{self.name}의 급습 실패! 공격이 빗나갔다!")