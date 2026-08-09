# Digital Stopwatch Testbench

hours = 0
minutes = 0
seconds = 0

print("================================")
print("    DIGITAL STOPWATCH TESTBENCH")
print("================================")

# Test 1: Initial time
if hours == 0 and minutes == 0 and seconds == 0:
    print("Test 1: Initial Time - PASS")
else:
    print("Test 1: Initial Time - FAIL")


# Test 2: Count seconds
seconds = seconds + 1

if seconds == 1:
    print("Test 2: Counting Seconds - PASS")
else:
    print("Test 2: Counting Seconds - FAIL")


# Test 3: 60 seconds = 1 minute
seconds = 59
seconds = seconds + 1

if seconds == 60:
    seconds = 0
    minutes = minutes + 1

if minutes == 1 and seconds == 0:
    print("Test 3: Minute Conversion - PASS")
else:
    print("Test 3: Minute Conversion - FAIL")


# Test 4: 60 minutes = 1 hour
minutes = 59
seconds = 59

seconds = seconds + 1

if seconds == 60:
    seconds = 0
    minutes = minutes + 1

if minutes == 60:
    minutes = 0
    hours = hours + 1

if hours == 1 and minutes == 0:
    print("Test 4: Hour Conversion - PASS")
else:
    print("Test 4: Hour Conversion - FAIL")


# Test 5: Reset
hours = 0
minutes = 0
seconds = 0

if hours == 0 and minutes == 0 and seconds == 0:
    print("Test 5: Reset - PASS")
else:
    print("Test 5: Reset - FAIL")


print("================================")
print("All tests completed.")
print("================================")