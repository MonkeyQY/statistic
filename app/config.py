import os

from dotenv import load_dotenv

load_dotenv()

# params servers
host = os.getenv("HOST", "localhost")
port = int(os.getenv("PORT", 5000))

# endpoints
get_statistic_path = os.getenv("GET_STATISTIC_PATH", "/statistic/get")

save_statistic_path = os.getenv("SAVE_STATISTIC_PATH", "/statistic/save")

delete_statistic_path = os.getenv("DELETE_STATISTIC_PATH", "/statistic/delete")

# API prefix
prefix_api = os.getenv("PREFIX_API", "/api/v1")

# API DOCS URL
docs_url = os.getenv("DOCS_URL", "/docs")

debug = os.getenv("DEBUG", False)

# database
DATABASE = {
    "drivername": "postgresql+psycopg2",
    "host": os.environ.get("DB_HOST", "db"),
    "port": os.environ.get("DB_PORT", "5432"),
    "username": os.environ.get("DB_USER", "postgres"),
    "password": os.environ.get("DB_PASS", "postgres"),
    "database": os.environ.get("DB_NAME", "Statistic"),
}

reload = os.getenv("RELOAD", "False") == "True"

use_log_file = os.getenv("USE_LOG_FILE", "False") == "True"
