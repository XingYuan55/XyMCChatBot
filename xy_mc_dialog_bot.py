from inspurai import Yuan, set_yuan_account, Example
import pyperclip as p
import os
import random
from simhash import Simhash
import heapq
import pyautogui
import time
import subprocess
import sys
from pprint import pprint


def read_csv(file_name):
    f = open(file_name, 'r')
    content = f.read()
    final_list = list()
    rows = content.split('\n')
    for row in rows:
        final_list.append(row.split(','))
    return final_list


EXAMPLE_NUM = 26

sys.path.append("..")
sys.path.append(os.path.abspath(os.curdir))

cor_list = read_csv("corpuses.csv")

example = [
    ("拿一部分回我家 烧吧，这样效率高", "嗯，用自己的熔炉烧东西效率还是高"),
    ("拿一部分回我家 烧吧，这样效率高", "我带了大量熔炉"),
    ("踩住压力板可以获取经验", "这是什么原理"),
    ("压力板提供红石信号以锁住熔炉", "我记得不可以吧"),
    ("然后就是等了吗", "对啊，"),
    ("我去钓会鱼", "半个小时后回来"),
    ("这里的区块得有人加载", 'ee'),
    ("钓鱼佬永不空军", "我也喜欢钓鱼"),
    ("钓鱼为什么钓不出附魔书来了", """
    在Java版中，钓鱼时，宝藏战利品只能通过在开阔水域钓鱼获得。开阔水域的检测机制如下：
    浮漂周围5×4×5区域[注 1]中的每一层都必须满足以下两个条件中的一个：
    这一层全部是水（必须是水源方块、无碰撞箱的含水方块，可以是气泡柱）。
    这一层全部是空气或睡莲。
    """),
    ("o", "懂"),
    ("ok", 'oKay'),
    ("死了", '我的天哪，太可惜了。'),


]

for row in cor_list[:-1]:
    example.append(tuple(row))

example = random.sample(example, EXAMPLE_NUM)

# 1. set account
set_yuan_account("Xingyuan55", "13199577499")  # 输入您申请的账号和手机号

# 2. initiate yuan api
# 注意：engine必需是['base_10B','translate','dialog','rhythm_poems']之一，'base_10B'是基础模型，'translate'是翻译模型，'dialog'是对话模型，'rhythm_poems'是古文模型
yuan = Yuan(engine='dialog',
            input_prefix="问：“",
            input_suffix="”",
            output_prefix="答：“",
            output_suffix="”",
            append_output_prefix_to_query=True,
            topK=5,
            temperature=1,
            topP=0.8,
            frequencyPenalty=1.2)


# 3. add examples if in need.
for inpu, output in example:
    yuan.add_example(Example(inp=inpu,
                             out=output))
# yuan.add_example(Example(inp="不过去这里我不知道需不需要门票？",out="我知道，不需要，是免费开放。"))
# yuan.add_example(Example(inp="你还可以到它边上的观复博物馆看看，我觉得那里很不错。",out="观复博物馆我知道，是马未都先生创办的新中国第一家私立博物馆。"))


print("====AiChater====")
while (1):
    prompt = input("玩家消息：") + 'Minecraft'
    response = yuan.submit_API(prompt=prompt, trun="”")
    try:
        responses = response.split(">")[1]
    except:
        responses = response
    p.copy(responses)
    print(responses)
    pyautogui.hotkey("Alt", "Tab")
    pyautogui.click()
    # time.sleep(2.8)
    pyautogui.hotkey("Ctrl", "V")
    pyautogui.press('Enter')
    pyautogui.hotkey("Alt", "Tab")


# h_dialog = []   # 存放历史对话：元素为ex


# def get_relative_qa(prompt, h_dialog, topN=2):
#     """
#     可以添加相关性计算，这里简单使用最近的一次对话。
#     :topN: 需要返回的相关对话轮数。
#     """
#     def simhash(query, text,):
#         """
#         采用局部敏感的hash值表示语义。
#         """
#         q_simhash = Simhash(query)
#         t_simhash = Simhash(text)
#         max_hashbit = max(len(bin(q_simhash.value)), len(bin(t_simhash.value)))

#         distance = q_simhash.distance(t_simhash)
#         # print(distance)

#         similar = 1 - distance / max_hashbit
#         return similar

#     h_num = len(h_dialog)
#     sim_values = []
#     tm_effs = []
#     rel_effs = []
#     gamma = 0.8  # time effect coefficient

#     if not h_dialog:
#         return []
#     else:
#         for indx, dialog in enumerate(h_dialog):
#             text = "|".join((dialog.input, dialog.output))
#             sim_value = simhash(prompt, text)
#             tm_eff = gamma ** ((h_num - indx)/h_num)
#             rel_eff = sim_value * tm_eff
#             sim_values.append(sim_value)
#             tm_effs.append(tm_eff)
#             rel_effs.append(rel_eff)

#         top_idx = heapq.nlargest(topN, range(
#             len(rel_effs)), rel_effs.__getitem__)
#         mst_dialog = [h_dialog[idx] for idx in top_idx]
#         mst_dialog.reverse()
#         return mst_dialog


# def update_example(yuan, exs):
#     ex_ids = []
#     for ex in exs:
#         ex_ids.append(ex.get_id())
#         yuan.add_example(ex)
#     return yuan, ex_ids


# # game_bat_file = r'C:\Users\L\Desktop\wanghany-1.16-OF-Fb.minecraft-luncher.bat'


# # game = subprocess.Popen(game_bat_file)
# p.copy("半自动人工智障机器人已启动。")

# while 1:
#     # print("输入Q退出")
#     prompt = input("玩家消息：")
#     # if ("Ciupui" in prompt or "Cui" in prompt or "ciupui" in prompt or "Ciu" in prompt or "ciu" in prompt or "CIUPUI" in prompt):

#     # if prompt != '':
#     #     # if prompt.lower() == "q":
#     #     #     break
#     #     if prompt[-1] == "”":
#     #         prompt = prompt[:-1]
#     #     exs = get_relative_qa(prompt, h_dialog)
#     #     yuan, ex_ids = update_example(yuan, exs)
#     #     response = yuan.submit_API(prompt=prompt, trun="”")
#     #     if len(h_dialog) < 10:    # 设置保存最多不超过10轮最近的历史对话
#     #         h_dialog.append(Example(inp=prompt, out=response))
#     #     else:
#     #         del (h_dialog[0])
#     #         h_dialog.append(Example(inp=prompt, out=response))
#     #     for ex_id in ex_ids:
#     #         yuan.delete_example(ex_id)


#     try:
#         responses = response.split(">")[1]
#     except:
#         responses = response

#         # 对结果进行复制……
#         p.copy(responses)
#         print(response, responses, sep=' | ')
#         pyautogui.hotkey("Alt", "Tab")
#         pyautogui.click()
#         time.sleep(2.8)
#         # pyautogui.press('Enter')
#         pyautogui.hotkey("Alt", "Tab")
#     else:
#         continue
