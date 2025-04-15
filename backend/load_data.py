import pandas as pd

def load_event_attendance_data():
    df = pd.read_csv("Cleaned_Event_Attendance.csv")
    df['Event Date'] = pd.to_datetime(df['Event Date'])
    df['day_of_week'] = df['Event Date'].dt.day_name()
    df['month'] = df['Event Date'].dt.hour

    return df

def load_company_data(): # unfinished
    df = pd.read_csv("Cleaned_Company_Visits.csv")
    
    return df
