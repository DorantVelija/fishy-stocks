from save_bought_stocks import read_row
from stock_api import get_stocks
from video import video, video_line_up

def run_main_loop():
    while True:
        s1, s2= get_stocks()
        win = video(50,1000, s1[0], s2[0], s1[2], s2[2])

        if win == 0:
            read_row(*s1)
        else:
            read_row(*s2)


while True:
    x = input("Press 'Y' to start...")
    if x == "y":
        video_line_up()
        run_main_loop()
    else:
        break
