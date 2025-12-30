import logging, os
from utils import paths

logging.basicConfig(
     level=logging.INFO
    ,format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    ,filename=os.path.join(paths.GetPath.logs,"log.txt")
    ,filemode="a"
)

logger_user_data = logging.getLogger("log: user_data")
logger_credentials = logging.getLogger("log: credentials")