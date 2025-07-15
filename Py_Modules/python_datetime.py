"""
PYTHON DATETIME MODULE - CONCEPT FILE FOR REVISION
=================================================

CORE CONCEPTS:
- datetime module handles dates, times, and time intervals
- Main classes: date, time, datetime, timedelta, timezone, UTC
- Supports arithmetic, formatting, parsing, and timezone conversion
- Objects are immutable (operations return new objects)

ESSENTIAL CLASSES:
- date: year, month, day only
- time: hour, minute, second, microsecond only  
- datetime: combines date and time
- timedelta: represents duration/difference
- timezone: handles timezone information
- UTC: constant for UTC timezone
"""

from datetime import date, time, datetime, timedelta, timezone, UTC

# ============================================================================
# 1. CREATING OBJECTS
# ============================================================================

# Current date/time
today = date.today()                    # 2025-07-09
now = datetime.now()                    # 2025-07-09 19:36:25.123456
now_utc = datetime.now(UTC)             # 2025-07-09 14:06:25.123456+00:00

# Specific date/time
birthday = date(1995, 3, 15)            # 1995-03-15
meeting = time(14, 30, 0)               # 14:30:00
deadline = datetime(2025, 12, 31, 23, 59, 59)  # 2025-12-31 23:59:59

print(f"Today: {today}")
print(f"Now: {now}")
print(f"UTC: {now_utc}")
print(f"Birthday: {birthday}")
print(f"Metting: {meeting}")
print(f"Deadline: {deadline}")
print()
# ============================================================================
# 2. ATTRIBUTES & PROPERTIES
# ============================================================================

dt = datetime(2025, 7, 9, 14, 30, 45)

print(f"Year: {dt.year}")              # 2025
print(f"Month: {dt.month}")            # 7
print(f"Day: {dt.day}")                # 9
print(f"Hour: {dt.hour}")              # 14
print(f"Minute: {dt.minute}")          # 30
print(f"Second: {dt.second}")          # 45
print(f"Weekday: {dt.weekday()}")      # 2 (Wednesday, Monday=0)
print()
# ============================================================================
# 3. ARITHMETIC OPERATIONS
# ============================================================================

# Adding/subtracting time
tomorrow = today + timedelta(days=1)
last_week = today - timedelta(weeks=1)
in_2_hours = now + timedelta(hours=2)

print(f"Tomorrow: {tomorrow}")
print(f"Last week: {last_week}")
print(f"In 2 hours: {in_2_hours}")
print()
# Calculate differences
start = datetime(2025, 1, 1)
end = datetime(2025, 7, 9)
diff = end - start

print(f"Days difference: {diff.days}")           # 189
print(f"Total seconds: {diff.total_seconds()}")  # 16329600.0
print(f"Total hours: {diff.total_seconds() / 3600}")  # 4536.0
print()
# ============================================================================
# 4. STRING FORMATTING (strftime)
# ============================================================================
# The strftime() method converts a datetime object into a formatted string. 
# Think of it as taking a date/time and turning it into text that's readable and formatted the way you want.
now = datetime.now()

# Common formats
iso_format = now.strftime("%Y-%m-%d %H:%M:%S")     # 2025-07-09 19:36:25
us_format = now.strftime("%m/%d/%Y %I:%M %p")      # 07/09/2025 07:36 PM
long_format = now.strftime("%A, %B %d, %Y")       # Wednesday, July 09, 2025

print(f"ISO: {iso_format}")
print(f"US: {us_format}")
print(f"Long: {long_format}")
print()
# Essential format codes
"""
%Y - 4-digit year    %m - month (01-12)    %d - day (01-31)
%H - hour (00-23)    %I - hour (01-12)     %M - minute (00-59)
%S - second (00-59)  %p - AM/PM            %A - weekday name
%B - month name      %b - short month      %a - short weekday
"""

# ============================================================================
# 5. STRING PARSING (strptime)
# ============================================================================
'''
-> String parsing refers to the reverse process - converting a string back into a datetime object.
This is actually done by strptime(), not strftime().
-> String parsing in datetime context means taking a date/time string and breaking it down to understand its components,
then converting it into a datetime object

The Two-Way Process:

strftime(): datetime object → formatted string (formatting)
strptime(): formatted string → datetime object (parsing)
'''
# Parse different formats
date_str1 = "2025-07-09"
parsed1 = datetime.strptime(date_str1, "%Y-%m-%d")

date_str2 = "July 09, 2025 2:30 PM"
parsed2 = datetime.strptime(date_str2, "%B %d, %Y %I:%M %p")

print(f"Parsed 1: {parsed1}")
print(f"Parsed 2: {parsed2}")

# ISO format (recommended)
iso_str = "2025-07-09T14:30:45"
iso_parsed = datetime.fromisoformat(iso_str)
print(f"ISO parsed: {iso_parsed}")
print()
# ============================================================================
# 6. TIMEZONE HANDLING
# ============================================================================

# Create timezone objects
utc_tz = UTC
ist_tz = timezone(timedelta(hours=5, minutes=30))  # IST = UTC+5:30
est_tz = timezone(timedelta(hours=-5))             # EST = UTC-5

# Timezone-aware datetime
utc_time = datetime.now(UTC)
ist_time = datetime.now(ist_tz)

print(f"UTC time: {utc_time}")
print(f"IST time: {ist_time}")

# Convert between timezones
local_time = utc_time.astimezone()      # Convert to local timezone
ist_converted = utc_time.astimezone(ist_tz)  # Convert to IST

print(f"Local: {local_time}")
print(f"IST converted: {ist_converted}")
print()
# ============================================================================
# 7. PRACTICAL EXAMPLES
# ============================================================================

# Age calculator
def calculate_age(birth_date):
    today = date.today()
    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

age = calculate_age(date(1990, 5, 15))
print(f"Age: {age} years")

# Days until event
def days_until(target_date):
    return (target_date - date.today()).days

christmas = date(2025, 12, 25)
days_left = days_until(christmas)
print(f"Days until Christmas: {days_left}")

# Business day checker
def is_business_day(check_date):
    return check_date.weekday() < 5  # Monday=0, Friday=4

print(f"Today is business day: {is_business_day(today)}")

# Time logger
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"[{timestamp}] {message}"

print(log_message("Application started"))
print()
# ============================================================================
# 8. COMMON OPERATIONS
# ============================================================================

# First and last day of month
first_day = today.replace(day=1)
next_month = (first_day + timedelta(days=32)).replace(day=1)
last_day = next_month - timedelta(days=1)

print(f"First day of month: {first_day}")
print(f"Last day of month: {last_day}")

# Weekend check
is_weekend = today.weekday() >= 5  # Saturday=5, Sunday=6
print(f"Is weekend: {is_weekend}")

# Duration formatting
def format_duration(seconds):
    days = int(seconds // 86400)
    hours = int((seconds % 86400) // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{days}d {hours}h {minutes}m"

duration_seconds = 90061  # 1 day, 1 hour, 1 minute, 1 second
print(f"Duration: {format_duration(duration_seconds)}")
print()
# ============================================================================
# 9. ERROR HANDLING
# ============================================================================

# Safe parsing
def safe_parse_date(date_string, format_string):
    try:
        return datetime.strptime(date_string, format_string)
    except ValueError as e:
        print(f"Parse error: {e}")
        return None

result = safe_parse_date("invalid-date", "%Y-%m-%d")
print(f"Safe parse result: {result}")
print()
# ============================================================================
# 10. BEST PRACTICES & GOTCHAS
# ============================================================================

"""
BEST PRACTICES:
✅ Use datetime.now(UTC) for UTC time (NOT datetime.utcnow() - deprecated)
✅ Use timezone-aware objects for global applications
✅ Store dates in UTC, display in local time
✅ Use ISO format (YYYY-MM-DD) for consistency
✅ Handle parsing errors with try-except
✅ Use appropriate class: date for dates, datetime for date+time

COMMON GOTCHAS:
❌ Mixing naive and timezone-aware datetimes
❌ Using deprecated datetime.utcnow()
❌ Assuming date formats (MM/DD vs DD/MM)
❌ Not handling leap years (datetime handles this automatically)
❌ Ignoring daylight saving time changes
❌ Month arithmetic edge cases (Jan 31 + 1 month = ?)
"""

# ============================================================================
# 11. QUICK REFERENCE
# ============================================================================

"""
CREATION:
date.today(), datetime.now(), datetime.now(UTC)
date(2025, 7, 9), datetime(2025, 7, 9, 14, 30, 0)

ARITHMETIC:
dt + timedelta(days=1), dt1 - dt2, timedelta(hours=2, minutes=30)

FORMATTING:
dt.strftime("%Y-%m-%d"), datetime.strptime(s, "%Y-%m-%d")

ATTRIBUTES:
dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second
dt.weekday(), dt.isoformat(), dt.timestamp()

TIMEZONE:
datetime.now(UTC), dt.astimezone(tz), timezone(timedelta(hours=5))
"""

print("\n" + "="*60)
print("DATETIME MODULE CONCEPT FILE COMPLETE")
print("Run this file to see all examples in action!")
print("="*60)
