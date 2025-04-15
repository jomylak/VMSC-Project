import pandas as pd

def load_event_attendance_data():
    df = pd.read_csv("cleaned_attendance.csv")
    df['Event Date'] = pd.to_datetime(df['Event Date'])
    df['day_of_week'] = df['Event Date'].dt.day_name()
    df['month'] = df['Event Date'].dt.hour

    return df

def load_company_data(): #Still need to add more
    df = pd.read_csv("cleaned_company_visit.csv")
    
    return df
