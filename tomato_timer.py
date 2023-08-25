import time

def tomato_timer(total_time, break_time):
    print("番茄时钟开始")
    while total_time > 0:
        # 倒计时
        mins, secs = divmod(total_time, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        total_time -= 1

    print("番茄时间结束，休息{}分钟".format(break_time))
    time.sleep(break_time * 60)
    print("休息结束，继续下一个番茄时间")

if __name__ == "__main__":
    tomato_timer(25, 5)
