# ------------- errors messages ---------------
# NOTE: Please do not change any of the following
# error messages unless their was a typo or some
# of them where hard to understand by the users
import sleuth.constants as constants

FAILD_TO_CONNECT_TO_THE_DATABASE = lambda database_url, database_type, error: f"[bold red] [ - ] [bold white]Faild to connect to the database [bold red]database_type:[bold green]`{database_type}`[bold white] with [bold red]database_url:[bold green]`{database_url}`[bold white]. Please check your config file located at [bold green]`{constants.SLEUTH_CONFIG_PATH}`[bold white]or [bold red]internet connection[bold white]\n[bold red]      \__[ - ] [bold white] Exception thrown by [bold red]SQLAlchemy[bold white]:\n\t\t{error}"

NO_CONFIG_WAS_FOUND = f"[bold red] [ - ] [bold white]Faild to locate config for [bold red]S[bold cyan]leuth[bold white]. Please run [bold green]`sleuth setup` [bold white]to setup [bold red]S[bold cyan]leuth[bold white]"
CONFIG_FILE_IS_CORRUPTED = f"[bold red] [ - ] [bold white]Config file for [bold red]S[bold cyan]leuth[bold white] is [bold red]corrupted[bold white]. Please file a report/issue at [bold green]{constants.GITHUB}"
UNKNOW_DATABASE_TYPE = lambda database_type: f"[bold red] [ - ] [bold white]Unknow database type [bold red]database_type:[bold yellow]`{database_type}`[bold white]. Please check your config file at [bold cyan]`{constants.SLEUTH_CONFIG_PATH}`[bold white]"
NO_DATABASE_WAS_SETUP_TO_USE_SEARCH_COMMAND = "[bold red] [ - ] [bold white]Can't use [bold green]search[bold white] command. No [bold green]database[bold white] was setup"
TARGET_IP_DOESNT_EXISTS_IN_THE_DATABASE = lambda ip: f"[bold red] [ - ] [bold white]Target [bold red]IP:[bold green]`{ip}`[bold white] [bold red]doesn't exists[bold white] in the [bold green]database[bold white]"

IP_REGEX_ERROR = lambda ip: f"[bold red]      \__[ - ] [bold white]Faild to verify regex for [bold red]IP:[bold green]`{ip}`. [bold white]Please check the [bold red]IP[bold white] format"
IP_IS_NOT_ALIVE = lambda ip: f"[bold red]     \__[ - ] [bold white]Faild to reach [bold red]IP:[bold green]`{ip}`. [bold white]Host is [bold red]dead"

NMAP_SCAN_FAILD = lambda ip, error: f"[bold red]     \__[ - ] [bold white]Nmap scan faild for [bold red]IP:[bold green]`{ip}`[bold white]. [bold red]Error: [bold white]{error}"
