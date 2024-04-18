import click

@click.command()
@click.option('--inches', type=float, default = '12', required=True, help='The number of inches to convert.')

def inchesToFeet(inches):
    """
    Converts a given number of inches to feet and inches.
    """
    feet = int(inches // 12)
    remaining_inches = inches % 12
    click.echo(f"{inches} inches is equal to {feet} feet and {remaining_inches:.2f} inches.")

if __name__ == '__main__':
    inchesToFeet()