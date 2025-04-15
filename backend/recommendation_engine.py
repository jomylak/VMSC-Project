def recommend_schedule(df): # Temporary recommendation (Finds the averages of the attendances for each day (monday, tuesday, etc))
    best_day = df.groupby('day_of_week')['Attendance'].mean().idxmax()
    best_month = df.groupby('month')['Attendance'].mean().idxmax() # Also finds for each month
    best_type = df.groupby('Event Type')['Attendance'].mean().idxmax() # Finds the best event type depending on attendance

    return {
        "best_day": best_day,
        "best_month": best_month,
        "best_type": best_type
    }

def find_popular_companies(df_event, df_company): #To Do
