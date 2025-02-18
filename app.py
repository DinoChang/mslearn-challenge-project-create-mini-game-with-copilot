import random
import keyboard

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return '平手'
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'rock'):
        return '玩家贏'
    else:
        return '電腦贏'

def map_arrow_keys_to_choice():
    if keyboard.is_pressed('up'):
        return 'rock'
    elif keyboard.is_pressed('left'):
        return 'paper'
    elif keyboard.is_pressed('right'):
        return 'scissors'
    return None

def main():
    print("歡迎來到剪刀、石頭、布小遊戲！")
    print("使用方向鍵快速選擇：上鍵 = 石頭，左鍵 = 布，右鍵 = 剪刀。")
    print("輸入 'bye' 來結束遊戲。")

    rounds = 0
    player_wins = 0
    computer_wins = 0

    while True:
        player_choice = map_arrow_keys_to_choice()
        if player_choice is None:
            player_choice = input("請輸入你的選擇：").lower()
        if player_choice == 'bye':
            break
        if player_choice not in ['rock', 'paper', 'scissors']:
            print("輸入錯誤！請輸入 'rock'、'paper' 或 'scissors'。")
            continue

        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)

        rounds += 1
        if result == '玩家贏':
            player_wins += 1
        elif result == '電腦贏':
            computer_wins += 1

        print(f"你出的是 {player_choice}，電腦出的是 {computer_choice}。結果：{result}")
        print(f"目前回合數：{rounds}，玩家贏：{player_wins}，電腦贏：{computer_wins}")

    print("遊戲結束！")
    print(f"總回合數：{rounds}，玩家贏：{player_wins}，電腦贏：{computer_wins}")

if __name__ == "__main__":
    main()
