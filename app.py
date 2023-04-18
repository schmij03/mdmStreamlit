import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Laden des Datensatzes
df = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv')
df['Height'] = df[' Height(Inches)"']
df['Weight'] = df[' "Weight(Pounds)"']
df.drop([' Height(Inches)"', ' "Weight(Pounds)"'], axis=1, inplace=True)

# Erstellen der Streamlit-App
st.title('Datensatz über Körpergröße und Gewicht')
st.write('Dies ist Datensatz, der Körpergröße (in Inches) und Gewicht (in Pounds) von Personen enthält.')

# Anzeige der Daten als Tabelle
st.header('Übersicht der Daten')
st.write(df)

# Anzeige der Daten als Histogramm
st.header('Histogramm der Körpergröße')
fig, ax = plt.subplots()
ax.hist(df['Height'], bins=20)
st.pyplot(fig)

# Anzeige der Daten als Scatterplot
st.header('Scatterplot von Körpergröße in Inches und Gewicht in Pounds')
fig, ax = plt.subplots()
ax.scatter(df['Height'], df['Weight'])
ax.set_xlabel('Körpergröße')
ax.set_ylabel('Gewicht')
st.pyplot(fig)

# Eingabefeld zur Steuerung der Anzeige
st.sidebar.header('Einstellungen')
height_range = st.sidebar.slider('Wähle einen Bereich der Körpergröße aus:', min_value=60, max_value=80, value=(70, 75))
subset_df = df[(df['Height'] >= height_range[0]) & (df['Height'] <= height_range[1])]
st.write('Daten im ausgewählten Bereich der Körpergröße:')
st.write(subset_df)
