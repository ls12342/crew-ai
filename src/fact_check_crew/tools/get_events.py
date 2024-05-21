
from datetime import datetime, timedelta
from langchain_community.vectorstores import LanceDB
from langchain.tools import tool

from gcsa.google_calendar import GoogleCalendar


class GetEvents:
    @tool("Get Data Tool")
    def data(email: str) -> str:
        """Search for events in the Google Calendar API"""
        # Get tomorrow's date
        tomorrow = datetime.now() + timedelta(days=1)
        # Get the day after tomorrow's date
        day_after_tomorrow = tomorrow + timedelta(days=1)

        # Get events for tomorrow
        calendar = GoogleCalendar()
        print("Calendar:", calendar)
        events = calendar.get_events(
            time_min=tomorrow, time_max=day_after_tomorrow)
        print("Events:", events)
        for event in calendar:
            print(event)
