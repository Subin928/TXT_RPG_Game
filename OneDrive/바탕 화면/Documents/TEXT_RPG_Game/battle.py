import random
import time

class BattleManager:
    def start_battle(self, player, enemy):
        """전투 시작"""
        print("\n" + "=" * 50)
        print("⚔️  전투 시작! ⚔️")
        print("=" * 50)

        player.show_status()
        enemy.show_status()
        print()

        # 선공 결정
        first_attacker, second_attacker = self._decide_first_attacker(player, enemy)

        turn = 1
        while player.is_alive() and enemy.is_alive():
            print(f"\n---턴 {turn} ---")
            time.sleep(1)

            # 첫 번째 공격자 공격
            self._execute_attack(first_attacker, second_attacker)
            time.sleep(1.5)

            if not second_attacker.is_alive():
                break

            # 두 번째 공격자 반격
            self._execute_attack(second_attacker, first_attacker)
            time.sleep(1.5)

            turn += 1

        # 전투 결과
        print("\n" + "=" * 50)
        if player.is_alive():
            print(f"🎉 승리! {player.get_name()}이(가) 승리했습니다!")
            return True
        else:
            print(f"💀 패배... {enemy.get_name()}에게 패배했습니다...")
            return False
        
    def _decide_first_attacker(self, player, enemy):
        """선공 결정"""
        if random.random() < 0.5:
            print(f"{player.get_name()}이(가) 선공합니다!\n")
            return player, enemy
        else:
            print(f"{enemy.get_name}이(가) 선공합니다!\n")
            return enemy, player

    def _execute_attack(self, attacker, target):
        """공격 실행 (70% 기본 공격, 30% 특수 공격)"""
        try:
            if random.random() < 0.7:   # 70% 확률로 기본 공격
                attacker.attack(target)

            else: # 30% 확률로 특수 공격
                attacker.special_attack(target)
        except Exception as e:
            # 마나 부족 등의 예외 처리
            print(f"⚠️  {e}")
            print(f"{attacker.get_name()}은(는) 기본 공격을 사용합니다!")
            attacker.attack(target)

        # 공격 후 상태 표시
        target.show_status()