//print logcat
adb -d shell logcat ActivityManager:I art:I *:S | findstr "[packagename]"
