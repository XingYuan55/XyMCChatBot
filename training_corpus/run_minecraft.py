import subprocess
import capture_message


game_bat_file = r'C:\Users\L\Desktop\wanghany-1.16-OF-Fb.minecraft-luncher.bat'
output = open("game_msg.txt", 'w', encode='gb2312')

game = subprocess.Popen(game_bat_file, stdout=output)
game.wait()
output.close()

message = open("game_msg.txt", 'r', encoding='utf-8')
corpuses = open("corpuses.txt", 'a', encoding='utf-8')
capture_message.capture_corpuses(message, corpuses)
