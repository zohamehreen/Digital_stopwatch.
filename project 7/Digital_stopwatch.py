import time
import keyboard

hours = 0
minutes = 0
seconds = 0

print("================================")
print("       DIGITAL STOPWATCH")
print("================================")
print("Press ENTER to start")
print("Press S to stop")
print("Press R to reset")
print("Press Q to exit")
print("================================")

while True:

    # Start stopwatch
    if keyboard.is_pressed("enter"):
        time.sleep(0.3)

        print("\nStopwatch started.")

        while True:

            time.sleep(1)
            seconds = seconds + 1

            # Convert seconds into minutes
            if seconds == 60:
                seconds = 0
                minutes = minutes + 1

            # Convert minutes into hours
            if minutes == 60:
                minutes = 0
                hours = hours + 1

            print("Time: {:02d}:{:02d}:{:02d}".format(
                hours, minutes, seconds
            ))

            # Stop stopwatch
            if keyboard.is_pressed("s"):
                print("Stopwatch stopped.")
                time.sleep(0.5)
                break

            # Reset stopwatch
            if keyboard.is_pressed("r"):
                hours = 0
                minutes = 0
                seconds = 0

                print("Stopwatch reset.")
                time.sleep(0.5)
                break

            # Exit program
            if keyboard.is_pressed("q"):
                print("Exiting stopwatch.")
                exit()

    # Exit before starting
    if keyboard.is_pressed("q"):
        print("Exiting stopwatch.")
        break