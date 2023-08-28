import datetime

def clock() -> str:
    """ Returns the time in the format %H:%M:%S """
    return f"[bold white]\[[bold cyan]{datetime.datetime.today().strftime('%H:%M:%S')}[bold white]]"
