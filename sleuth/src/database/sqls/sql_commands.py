# NOTE: please do not edit this sql commands
# as it may lead to some future issues when
# trying to read from/write to the database
# ------------------------------------------
from sqlalchemy import text

TARGETED_IPS_TABLE_SQLITE = text("""
    CREATE TABLE targeted_ips (
        ip_uid VARCHAR PRIMARY KEY,
        ip VARCHAR,
        is_vpn BOOL,
        is_proxy BOOL,
        is_tor BOOL,
        is_relay BOOL,
        nmap_service_uids VARCHAR,
        ip_api_results_uid VARCHAR,
        created_at DATETIME
    );"""
)

NMAP_SERVICES_TABLE_SQLITE = text("""
    CREATE TABLE nmap_services (
        nmap_service_uid VARCHAR PRIMARY KEY,
        service VARCHAR(72),
        port VARCHAR(72),
        protocol VARCHAR(72),
        state VARCHAR(72),
        version VARCHAR(72),
        reason VARCHAR(72),
        reason_ttl VARCHAR(72),
        cpe VARCHAR(72),
        created_at DATETIME
    );"""
)

IP_API_TABLE_SQLITE = text("""
    CREATE TABLE ip_api_results (
        ip_api_results_uid TEXT PRIMARY KEY,
        status TEXT,
        continent TEXT,
        continentCode TEXT,
        country TEXT,
        countryCode TEXT,
        region TEXT,
        regionName TEXT,
        city TEXT,
        district TEXT,
        zip TEXT,
        lat REAL,
        lon REAL,
        timezone TEXT,
        offset TEXT,
        currency TEXT,
        isp TEXT,
        org TEXT,
        as_ TEXT,
        asname TEXT,
        reverse TEXT,
        mobile BOOL,
        proxy BOOL,
        hosting BOOL,
        query TEXT,
        created_at DATETIME
    );"""
)

# postgresql
TARGETED_IPS_TABLE_POSTGRESQL = text("""
    CREATE TABLE targeted_ips (
        ip_uid VARCHAR PRIMARY KEY,
        ip VARCHAR,
        is_vpn BOOL,
        is_proxy BOOL,
        is_tor BOOL,
        is_relay BOOL,
        nmap_service_uids VARCHAR,
        ip_api_results_uid VARCHAR,
        created_at TIMESTAMP
    );"""
)

NMAP_SERVICES_TABLE_POSTGRESQL = text("""
    CREATE TABLE nmap_services (
        nmap_service_uid VARCHAR PRIMARY KEY,
        service VARCHAR(72),
        port VARCHAR(72),
        protocol VARCHAR(72),
        state VARCHAR(72),
        version VARCHAR(72),
        reason VARCHAR(72),
        reason_ttl VARCHAR(72),
        cpe VARCHAR(72),
        created_at TIMESTAMP
    );"""
)

IP_API_TABLE_POSTGRESQL = text("""
    CREATE TABLE ip_api_results (
        ip_api_results_uid TEXT PRIMARY KEY,
        status TEXT,
        continent TEXT,
        continentCode TEXT,
        country TEXT,
        countryCode TEXT,
        region TEXT,
        regionName TEXT,
        city TEXT,
        district TEXT,
        zip TEXT,
        lat REAL,
        lon REAL,
        timezone TEXT,
        offset_text TEXT,
        currency TEXT,
        isp TEXT,
        org TEXT,
        as_ TEXT,
        asname TEXT,
        reverse TEXT,
        mobile BOOL,
        proxy BOOL,
        hosting BOOL,
        query TEXT,
        created_at TIMESTAMP
    );"""
)
