from .character import Character

class Mage(Character):
    def __init__(self, name="마법사", level=1):
        super().__init__(name, level, health=80, attack_power=18)
        self.mana = 100
        self.max_mana = 100

    def attack(self, target):
        """기본 공격"""
        damage = self.attack_power
        print(f"{self.name}의 마법 공격! {target.get_name()}에게 {damage}의 피해!")
        target.take_damage(damage)

    def special_attack(self, target):
        """특수 공격: 파이어볼 (1.5배 데미지, 마나 20 소모)"""
        if self.mana < 20:
            raise Exception(f"{self.name}의 마나가 부족합니다! (현재 마나: {self.mana})")
        
        damage = int(self.attack_power * 1.5)
        self.mana -= 20
        print(f"{self.name}의 파이어볼! {target.get_name()}에게 {damage}의 피해!")
        print(f"(마나 소모: 20, 남은 마나: {self.mana})")
        target.take_damage(damage)

    def show_status(self):
        """마법사 상태 출력 (마나 포함)"""
        print(f"[{self.name}] 레벨: {self.level} 체력: {self.health}/{self.max_health} 공격력: {self.attack_power} 마나: {self.mana}/{self.max_mana}")