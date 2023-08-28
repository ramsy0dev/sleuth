# ------------- info messages ---------------
# NOTE: Please do not change any of the following
# info messages unless their was a typo or some
# of them where hard to understand by the users

CHECKING_IP_REGEX = lambda ip: f"[bold green] \[ + ] [bold white]Checking regex for [bold red]IP:[bold green]`{ip}`[bold white]..."
CHECKING_IS_IP_RESPONSIVE = lambda ip: f"[bold green] \[ + ] [bold white]Checking if [bold red]IP:[bold green]`{ip}`[bold white] is alive..."

CONFIG_SAVED = lambda sleuth_config_path: f"[bold green] \[ + ] [bold white]Config saved successfully at [bold cyan]`{sleuth_config_path}` [bold red](please do not edit it unless you know what you are doing!!!)"

CONNECTING_TO_DATABASE = lambda database_type, database_url: f"[bold green] \[ + ] [bold white]Connecting to [bold red]database_type:[bold green]`{database_type}`[bold white] with [bold red]database_url:[bold green]`{database_url}`[bold white]..."
CONNECTED_TO_DATABASE = lambda database_type: f"[bold green] \[ + ] [bold white]Connected to [bold red]database_type:[bold green]`{database_type}`[bold white]"
SETTING_UP_DATABASE_TABLES = f"[bold green] \[ + ] [bold white]Setting up [bold green]database[bold white] [bold red]tables[bold white]... [bold yellow](do not exist!!)[bold white]"
TABLES_CREATED = lambda tables_name: f"[bold green]      \__[ + ] [bold white]Created [bold red]tables [bold cyan]`{', '.join(tables_name)}`[bold white] in the [bold green]database[bold white]"
DATABASE_SETUP_IS_DONE = f"[bold green] \[ + ] [bold green]Database [bold white]setup is [bold gren]done!!"
FETCHING_DATA_FROM_THE_DATABASE = lambda ip: f"[bold green] \[ + ] [bold white]Fetching data about [bold red]IP:[bold green]`{ip}`[bold white] from the [bold green]database[bold white]..."

RUNNING_NMAP_SCAN = "[bold green] \[ + ] [bold white]Running a [bold green]nmap [bold white]scan..."
SAVING_NMAP_SCAN_RESULTS = "[bold green] \[ + ] [bold white]Saving [bold green]nmap [bold white]scan results into the[bold green] database[bold white]..."
NMAP_RESULTS = "[bold green] \[ + ] [bold greeb]nmap [bold white]results:"

RUNNING_VPNAPI = lambda ip: f"[bold green] \[ + ] [bold white]Checking if [bold red]IP:[bold green]`{ip}`[bold white] is associated with a [bold yellow]vpn, tor, proxy, relay[bold white]..."
SKIPPING_VPN_API_SERVICE = "[bold yellow] \[ ! ] [bold yellow]Skipping[bold white] service [bold green]vpnapi.io[bold white], because not API [bold red]key[bold white] was found"

RUNNING_IP_API = lambda ip: f"[bold green] \[ + ] [bold white]Gather info about [bold red]IP:[bold green]`{ip}`[bold white] using [bold green]ip-api.com[bold white]..."
SAVING_IP_API_RESULTS = "[bold green] \[ + ] [bold white]Saving [bold green]ip-api.com[bold white] results in the [bold green]database[bold white]..."
IP_API_RESULTS = "[bold green] \[ + ] [bold green]ipapi.com [bold white]results:"

SAVING_TARGETED_IP_INFO = lambda ip: f"[bold green] \[ + ] [bold white]Saving [bold red]IP:[bold green]`{ip}`[bold white] gathered info into the [bold green]database[bold white]..."
TARGET_IP_INFO = lambda ip: f"[bold green] \[ + ] [bold white]Target [bold red]IP:[bold green]`{ip}`[bold white]'s results:"

RUN_THE_SEARCH_COMMAND = lambda ip: f"[bold green] \[ + ] [bold white]Please run the following: `sleuth search {ip}`, to fetch data about the target ip that is saved in the [bold green]database[bold white]"
