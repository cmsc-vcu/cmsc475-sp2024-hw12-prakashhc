import click
import requests

API_KEY = '0bbb7d4a9d6e494a94400640241604'
BASE_URL = 'http://api.weatherapi.com/v1/current.json'

@click.command()
@click.option('-z', '--zip', default='23059', help='Zip code to get the weather for')
def weather(zip):
    """Get the current weather for a given zip code."""
    params = {
        'key': API_KEY,
        'q': zip,
        'aqi': 'no'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        location = data['location']
        current = data['current']

        click.echo(f"Current weather for {location['name']}, {location['region']}, {location['country']}:")
        click.echo(f"- Temperature: {current['temp_f']}°F ({current['temp_c']}°C)")
        click.echo(f"- Conditions: {current['condition']['text']}")
        click.echo(f"- Wind: {current['wind_mph']} mph ({current['wind_kph']} kph) from {current['wind_dir']}")
        click.echo(f"- Humidity: {current['humidity']}%")
    except requests.exceptions.RequestException as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    weather()