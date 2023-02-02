# last 3000 days
#kelowna_temp = pd.read_csv('data/weatherstats_kelowna_daily.csv', parse_dates=['date'])[['date', 'avg_temperature']]
from main import main
import altair as alt

def visual():
    dataframe = main()
    chart = alt.Chart(dataframe).mark_line(interpolate='monotone').encode(
        alt.X('datetime', title=None,  axis=alt.Axis(labelAngle=-45)),
        alt.Y('temp2m', title='Temperature (°C)'),
        tooltip = ('temp2m')
        ).properties(height=300, width=900, title = "City Daily Temperatures(°C)")

    return chart + chart.mark_point()