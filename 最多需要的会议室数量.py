import random
import matplotlib.pyplot as plt

# 生成15个随机会议时间
meet = list()
for i in range(20):
    start = random.randint(1, 20)
    end = start + random.randint(1, 10)
    meet.append([start, end])

# 时间标记
times = list()
flags = list()  # 存放对应时间的标记
meet.sort()
print("show meeting time\n",meet)
for time in meet:
    if time[0] in times:
        start_index_num = times.index(time[0])
        flags[start_index_num].append(1)
        if time[1] in times:
            end_index_num = times.index(time[1])
            flags[end_index_num].append(-1)
        else:
            times.append(time[1])
            flags.append([-1, ])
    else:
        times.append(time[0])
        flags.append([1, ])
        if time[1] in times:
            end_index_num = times.index(time[1])
            flags[end_index_num].append(-1)
        else:
            times.append(time[1])
            flags.append([-1, ])
print("sequence before sort")
print(times)
print(flags)

# 对时间点进行排序
sorted_times = sorted(times)
sorted_flags = list()
for time in sorted_times:
    time_index_num = times.index(time)
    # 按时间顺序对flag进行排序
    sorted_flags.append(flags[time_index_num])
print("sequence after sort")
print(sorted_times)
print(sorted_flags)

# 以时间点为单位，对每个flag列表进行求和累加，过程中得到的max就是需要的会议室数量
max_room = 0
sum_room = 0
for flag in sorted_flags:
    sum_room = sum(flag)+sum_room
    max_room = max(max_room, sum_room)

print("meeting-room need ", max_room)

'''
在图像中把线段画出来
每个会议在meet中的索引+1为y轴值
'''
for time in meet:
    y = meet.index(time)+1
    y_data = [y, y]
    plt.plot(time, y_data,)

plt.title("meeting time")
plt.xlabel("time")
plt.ylabel("meet")
plt.show()
