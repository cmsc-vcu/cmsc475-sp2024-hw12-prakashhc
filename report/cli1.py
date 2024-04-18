import click
import requests

APIKEY = '7ac9cd98e15b83fd44ee2ada'

@click.command()
@click.option('--from', 'from_currency', type=str, default='USD', help='The source currency code.')
@click.option('--to', 'to_currency', type=str, default='INR', required=True, help='The target currency code.')
@click.option('--amount', type=float, default=1.0, help='The amount to convert.')
@click.help_option('--help', '-h', help='Usage: convertCurrency --from [CURRENCY SYMBOL] --to [CURRENCY SYMBOL] --amount [AMOUNT]')

def convertCurrency(from_currency, to_currency, amount):
    """
    Convert a currency amount from one currency to another.
    """
    url = f'https://api.exchangerate-api.com/v4/latest/{from_currency}'
    response = requests.get(url, params={'apikey': APIKEY})
    
    if response.status_code == 200:
        data = response.json()
        conversion_rate = data['rates'][to_currency]
        converted_amount = amount * conversion_rate
        click.echo(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        click.echo(f"Error: {response.status_code} - {response.text}")

if __name__ == '__main__':
    convertCurrency()