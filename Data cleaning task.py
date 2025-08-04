import pandas as pd
df=pd.read_csv("KaggleV2-May-2016.csv")
print(df.head())
df['PatientId'] = "'" + df['PatientId'].astype(int).astype(str)
df['AppointmentID'] = "'" + df['AppointmentID'].astype(int).astype(str)
# Check for missing values
print(df.isnull().sum())
# Remove duplicate rows if any
df.drop_duplicates(inplace=True)
# Convert ScheduledDay and AppointmentDay  dd-mm-yyyy
df['ScheduledDay'] = pd.to_datetime(df['ScheduledDay']).dt.strftime('%d-%m-%Y')
df['AppointmentDay'] = pd.to_datetime(df['AppointmentDay']).dt.strftime('%d-%m-%Y')
print(df[['ScheduledDay','AppointmentDay']].head())
print(df.loc[0, 'ScheduledDay'])
# Rename columns to lowercase with underscores
df.columns = [col.strip().lower().replace('-', '_').replace(' ', '_') for col in df.columns]
# Convert age to integer (if it's not already)
df['age'] = df['age'].astype(int)
print(df.dtypes)
df.to_csv("cleaned_medical_no_shows.csv", index=False)







