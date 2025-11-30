from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, level, health, attack_power):
        self.name = name
        self.level = level
        self.health = health
        self.max_health = health         # 초기 체력 저장
        self.attack_power = attack_power

    @abstractmethod
    def attack(self, target):
        """기본 공격"""
        pass

    @abstractmethod
    def special_attack(self, target):
        """특수 공격"""
        pass

    def take_damage(self, damage):
        """피해를 입음"""
        self. health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        """생존 여부 확인"""
        return self.health > 0
    
    def show_status(self):
        """캐릭터 상태 출력"""
        print(f"[{self.name}] 레벨: {self.level} 체력: {self.health}/{self.max_health} 공격력: {self.attack_power}")

    def reset_health(self):
        """체력 초기화"""
        self.health = self.max_health

    def get_name(self):
        """이름 반환"""
        return self.name