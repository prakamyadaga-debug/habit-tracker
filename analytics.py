from datetime import date, timedelta


def today():
    return date.today().isoformat()


def current_streak(completed_dates):
    dates = set(completed_dates)
    current = date.today()
    streak = 0

    while current.isoformat() in dates:
        streak += 1
        current -= timedelta(days=1)

    return streak


def longest_streak(completed_dates):
    if not completed_dates:
        return 0

    dates = sorted(
        date.fromisoformat(d)
        for d in set(completed_dates)
    )

    longest = 1
    streak = 1

    for i in range(1, len(dates)):
        if dates[i] == dates[i - 1] + timedelta(days=1):
            streak += 1
            longest = max(longest, streak)
        else:
            streak = 1

    return longest


def completion_percentage(habit):
    start = date.fromisoformat(habit["created"])
    days = (date.today() - start).days + 1

    completed = 0

    for d in habit["completed"]:
        completed_date = date.fromisoformat(d)

        if start <= completed_date <= date.today():
            completed += 1

    if days <= 0:
        return 0

    return round((completed / days) * 100)
