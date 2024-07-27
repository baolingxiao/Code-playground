''''
简单的任务自动化
你需要自动化每天的课程安排，打印出当天的课程表。
'''
import datetime

schedule = {
    'Monday': ['Math', 'English', 'Physics'],
    'Tuesday': ['Biology', 'Chemistry', 'History'],
    'Wednesday': ['Math', 'PE', 'Computer Science'],
    'Thursday': ['English', 'Art', 'Physics'],
    'Friday': ['Biology', 'Math', 'History']
}

today = datetime.datetime.now().strftime('%A')

if today in schedule:
    print(f"Today's classes ({today}):")
    for course in schedule[today]:
        print(course)
else:
    print("No classes today!")
