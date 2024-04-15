import click
import pyfiglet

@click.command()
@click.option('-n', '--name', default='from cli1.py', help='Name of user to greet.')
@click.option('-c', '--count', default=1, help='Number of greetings.')
def greet(name, count):
    """Simple program that greets NAME for a total of COUNT times."""
    figlet = pyfiglet.Figlet()

    for _ in range(count):
        big_string = figlet.renderText(f'Hello, {name}!')
        click.echo( big_string )

if __name__ == '__main__':
    greet()

