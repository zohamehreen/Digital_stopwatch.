# Digital Stopwatch using Python

## Description

The Digital Stopwatch is a simple Python project that measures elapsed time in hours, minutes, and seconds.

The stopwatch automatically continues counting after it is started. The user does not need to press Enter after every second.

The project uses basic Python concepts along with the `time` and `keyboard` modules.

## Technologies Used

* Python
* Variables
* `while` loop
* `if-elif-else`
* `input/output`
* `time` module
* `keyboard` module

## Why is the `keyboard` Module Used?

The `keyboard` module is used to detect keyboard keys while the program is running.

Normally, Python's `input()` function waits for the user to press Enter. For this stopwatch, we want the user to be able to press a key such as **S** directly while the stopwatch is running.

The following statement checks whether the S key is pressed:

```python
keyboard.is_pressed("s")
```

When the user presses **S**, the program detects the key and stops the stopwatch.

Similarly:

```python
keyboard.is_pressed("r")
```

is used to detect the **R** key for resetting the stopwatch.

And:

```python
keyboard.is_pressed("q")
```

is used to detect the **Q** key for exiting the program.

Therefore, the `keyboard` module is not unnecessary. It is specifically required for detecting keys such as **S, R, and Q without requiring the user to press Enter**.

## Installing the Keyboard Module

The `keyboard` module is an external Python package, so it needs to be installed once.

Open Command Prompt or Terminal and enter:

```text
pip install keyboard
```

After installation, the program can use:

```python
import keyboard
```

The `time` module is already included with Python, so it does not need to be installed.

## Controls

| Key   | Function        |
| ----- | --------------- |
| ENTER | Start stopwatch |
| S     | Stop stopwatch  |
| R     | Reset stopwatch |
| Q     | Exit program    |

## Working

1. The program starts with the time set to `00:00:00`.
2. Press **ENTER** to start the stopwatch.
3. The program waits for one second using `time.sleep(1)`.
4. The seconds counter increases automatically.
5. After 60 seconds, the seconds become zero and the minute increases.
6. After 60 minutes, the minutes become zero and the hour increases.
7. Press **S** to stop the stopwatch.
8. Press **R** to reset the time to `00:00:00`.
9. Press **Q** to exit the program.

## Example

```text
Press ENTER to start

Stopwatch started.
Time: 00:00:01
Time: 00:00:02
Time: 00:00:03
Time: 00:00:04
Time: 00:00:05

Press S

Stopwatch stopped.
```

The user does **not** need to press Enter after every second.

## Project Structure

```text
Digital-Stopwatch/
│
├── stopwatch.py
├── testbench.py
├── output.txt
└── README.md
```

## How to Run

### Step 1: Install Python

Make sure Python 3 is installed.

### Step 2: Install keyboard

Open Command Prompt or Terminal:

```text
pip install keyboard
```

### Step 3: Run the Stopwatch

```text
python stopwatch.py
```

### Step 4: Run the Testbench

```text
python testbench.py
```

## Testbench

The testbench checks:

* Initial time
* Seconds counting
* Conversion of seconds into minutes
* Conversion of minutes into hours
* Reset operation

Expected result:

```text
Test 1: Initial Time - PASS
Test 2: Counting Seconds - PASS
Test 3: Minute Conversion - PASS
Test 4: Hour Conversion - PASS
Test 5: Reset - PASS
```

## Advantages

* Simple and beginner-friendly
* Automatically counts time
* No need to press Enter every second
* Easy keyboard controls
* Uses basic Python programming concepts
* Easy to understand and modify
* Suitable for a BTech mini project

## Future Scope

The project can be extended by adding:

* Lap time
* Countdown timer
* Alarm
* Graphical user interface
* Digital clock display
* Start/stop buttons
* Multiple stopwatch functions

## Conclusion

The Digital Stopwatch demonstrates how Python can be used to create a simple time-measuring application. It uses basic programming concepts for counting time and the `keyboard` module to detect keys such as S, R, and Q while the stopwatch is running.
