import numpy as np
import cv2 as cv
print("CV2 version:", cv.__version__)

def video_line_up():
    # camera set up / line up
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        ret, frame = cap.read()
        cv.putText(frame, f"Press 'C' after you are done lining up your camera.",
                   (50, 80), cv.FONT_HERSHEY_SIMPLEX, 1.4,
                   (0, 0, 255),
                   3)
        cv.imshow('Line up your fish', frame)

        if cv.waitKey(1) == ord('c'):
            cap.release()
            cv.destroyAllWindows()
            break
    cap.release()
    cv.destroyAllWindows()
def video(limit=10, fish_size = 1000, stock1_symbol='', stock2_symbol='', stock1_price=0, stock2_price=0):
    # fish detection camera
    most_side_spent_on = [0, 0]
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    while True:
        # capture frame-by-frame
        ret, frame = cap.read()

        # bounds
        lower_bound1 = np.array([10, 150, 80])
        upper_bound1 = np.array([20, 255, 255])

        lower_bound2 = np.array([20, 140, 70])
        upper_bound2 = np.array([30, 255, 255])

        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # make the frame to a hsv frame
        hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # mask out within our bounds

        mask_a = cv.inRange(hsv_frame, lower_bound1, upper_bound1)
        mask_b = cv.inRange(hsv_frame, lower_bound2, upper_bound2)
        mask = mask_a + mask_b

        # mask out the frame using mask obv
        result = cv.bitwise_and(frame, frame, mask=mask)

        # get res
        width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
        fps = int(cap.get(cv.CAP_PROP_FPS))

        # display resolution on video
        cv.putText(result, f"Resolution: {width} x {height} FPS: {fps}.",
                   (50, 80),
                   cv.FONT_HERSHEY_SIMPLEX, 1.4,
                   (0, 0, 255),
                   2)
        cv.putText(result, "Press 'q' to quit.",
                   (width - 500, 80),
                   cv.FONT_HERSHEY_SIMPLEX, 1.4,
                   (0, 0, 255),
                   2)

        # check where is on screen
        contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        def get_side(width, x):
            if width / 2 > x:
                most_side_spent_on[0] += 0.1
                return "left"
            else:
                most_side_spent_on[1] += 0.1
                return "right"

        for contour in contours:
            if cv.contourArea(contour) > fish_size:  # filter small noise

                x, y, w, h = cv.boundingRect(contour)
                cv.rectangle(result, (x, y), (x + w, y + h), (0, 255, 0), 2)
                side = get_side(width, x)

                cv.putText(result, f"Fish at ({x},{y})", (x, y - 10),
                           cv.FONT_HERSHEY_SIMPLEX, 0.7,
                           (0, 255, 0),
                           2)
                cv.putText(result, f"Fish on {side}",
                           (50, 120),
                           cv.FONT_HERSHEY_SIMPLEX, 1,
                           (0, 255, 0),
                           2)

        most_time_side = "left" if most_side_spent_on[0] > most_side_spent_on[1] else "right"

        cv.putText(result, f"Most time spent on: {most_time_side}",
                   (50, 160),
                   cv.FONT_HERSHEY_SIMPLEX, 1,
                   (0, 255, 0),
                   2)
        cv.putText(result, f"left: {round(most_side_spent_on[0])} right: {round(most_side_spent_on[1])}",
                   (50, 190),
                   cv.FONT_HERSHEY_SIMPLEX, 1,
                   (0, 255, 0),
                   2)
        cv.putText(result, "press 'w' to reset side tracker", (width-600, 120),
                   cv.FONT_HERSHEY_SIMPLEX, 1,
                   (0, 255, 0),
                   2)
        cv.putText(result, f"Left stock: {stock1_symbol} x {stock1_price} ",
                   (20, height - 50),
                   cv.FONT_HERSHEY_SIMPLEX, 1.4,
                   (0, 255, 255),
                   2)
        cv.putText(result, f"Right Stock: {stock2_symbol} x {stock2_price}.",
                   (width-800, height - 50), cv.FONT_HERSHEY_SIMPLEX,
                   1.4,
                   (255, 0, 255),
                   2)

        # display the resulting frame
        cv.imshow('Fish Stock Prediction', result)

        if cv.waitKey(1) == ord('q'):
            break

        elif cv.waitKey(1) == ord('w'):
            most_side_spent_on = [0, 0]

        elif most_side_spent_on[0] + most_side_spent_on[1] >= limit:
            cap.release()
            cv.destroyAllWindows()
            return 0 if most_side_spent_on[0] > most_side_spent_on[1] else 1

    # release if anything goes wrong
    cap.release()
    cv.destroyAllWindows()
