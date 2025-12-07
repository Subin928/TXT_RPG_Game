from characters import Warrior, Mage, Rogue
from battle import BattleManager

def choose_character(prompt):
    """캐릭터 선택 함수"""
    print(f"\n{prompt}")
    print("1. 전사 (체력: 100, 공격력: 15)")
    print("2. 마법사 (체력: 80, 공격력: 18, 마나: 100)")
    print("3. 도적 (체력: 90, 공격력: 12)")

    while True:
        choice = input("선택 (1-3):").strip()

        if choice == "1":
            return Warrior()
        elif choice =="2":
            return Mage()
        elif choice =="3":
            return Rogue()
        else:
            print("잘못된 입력입니다. 1, 2, 3 중 하나를 선택하세요.")

def main():
    """게임 메인 함수"""
    print("=" * 50)
    print("🎮  RPG 전투 게임에 오신 것을 환영합니다! 🎮")
    print("=" * 50)

    # 플레이어 캐릭터 선택
    player = choose_character("플레이어 캐릭터를 선택하세요:")
    print(f"\n {player.get_name()}을(를) 선택하셨습니다!")

    battle_manager = BattleManager()

    # 전투 루프
    while True:
        # 적 캐릭터 선택
        enemy = choose_character("\n적 캐릭터를 선택하세요: ")
        print(f"\n⚔️  적 {enemy.get_name()}이(가) 나타났다!")

        result = battle_manager.start_battle(player, enemy)

        if result: # 승리
            # 플레이어 체력 회복
            player.reset_health()
            print(f"\n {player.get_name()}의 체력이 회복되었습니다!")

            # 계속 진행 여부
            while True:
                continue_game = input("\n다음 전투를 진행하시겠습니까? (y/n: ").strip()
                if continue_game == "y":
                    break
                elif continue_game == "n":
                    print("\n게임을 종료합니다. 플레이해주셔서 감사합니다! 👋")
                    return
                else:
                    print("y 또는 n을 입력해주세요.")

        else: # 패배
            print(f"\n💀 Game Over 💀")
            print("게임을 종료합니다.")
            return

if __name__ == "__main__":
    main()