from app.helpers import pretty_date
from datetime import datetime, timedelta

def test_diff_less_than_zero():
   assert pretty_date(datetime.utcnow()+timedelta(seconds=1)) == "just about now"

def test_now():
   assert pretty_date(datetime.utcnow()) == "just now"
   assert pretty_date() == "just now"

def test_int_time():
   assert pretty_date(42) == "49 years ago"

def test_yesterday():
   assert (pretty_date(datetime.utcnow()-timedelta(days=1))) == "Yesterday"

def test_seconds_ago():
   assert (pretty_date(datetime.utcnow()-timedelta(seconds=12))) == "12 seconds ago"
   assert (pretty_date(datetime.utcnow()-timedelta(seconds=49))) == "49 seconds ago"
   assert (pretty_date(datetime.utcnow()-timedelta(seconds=30))) == "30 seconds ago"

def test_underminute_ago():
   assert (pretty_date(datetime.utcnow()-timedelta(seconds=61))) == "a minute ago"
   assert (pretty_date(datetime.utcnow()-timedelta(minutes=1.5))) == "a minute ago"

def test_minutes_ago():
   assert (pretty_date(datetime.utcnow()-timedelta(minutes=2.5))) == "2 minutes ago"
   assert (pretty_date(datetime.utcnow()-timedelta(minutes=32))) == "32 minutes ago"

def test_hour_ago():
   assert (pretty_date(datetime.utcnow()-timedelta(minutes=61))) == "an hour ago"
   assert (pretty_date(datetime.utcnow()-timedelta(minutes=119))) == "an hour ago"
   assert (pretty_date(datetime.utcnow()-timedelta(hours=1))) == "an hour ago"

def test_hours_ago():
   assert (pretty_date(datetime.utcnow()-timedelta(minutes=120))) == "2 hours ago"
   assert (pretty_date(datetime.utcnow()-timedelta(hours=16))) == "16 hours ago"
   assert (pretty_date(datetime.utcnow()-timedelta(hours=3))) == "3 hours ago"


def test_days_ago():
   assert (pretty_date(datetime.utcnow()-timedelta(hours=48))) == "2 days ago"
   assert (pretty_date(datetime.utcnow()-timedelta(days=3))) == "3 days ago"


def test_weeks_ago():
   assert (pretty_date(datetime.utcnow()-timedelta(days=7))) == "1 weeks ago"
   assert (pretty_date(datetime.utcnow()-timedelta(days=14))) == "2 weeks ago"


def test_months_ago():
   assert (pretty_date(datetime.utcnow()-timedelta(weeks=12))) == "2 months ago"
   assert (pretty_date(datetime.utcnow()-timedelta(weeks=27))) == "6 months ago"

def test_years_ago():
   assert (pretty_date(datetime.utcnow()-timedelta(days=365))) == "1 years ago"
   assert (pretty_date(datetime.utcnow()-timedelta(weeks=157))) == "3 years ago"

