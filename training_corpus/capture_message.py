import subprocess


def capture_message(messages: str):
    if "<" not in messages:  # 不是玩家消息，跳过
        return None
    else:
        msg_index = messages.index("<")
        player_msg = messages[msg_index:]

    return player_msg


def capture_corpuses(message, corpuses):
    # message = open("game_msg.txt", 'r', encoding='utf-8')
    # corpuses = open("corpuses.txt", 'a', encoding='utf-8')
    for m in message.readlines():
        cated_msg = '' if not capture_message(
            m) else capture_message(m)
        corpuses.write(cated_msg)
    message, corpuses.close()
