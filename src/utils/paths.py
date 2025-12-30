from pathlib import Path

class GetPath:
    """
    Centralized access to all important project directories.

    Defines absolute paths to common directories and their subfolders. 
    It allows consistent and maintainable access to files throughout 
    the project, regardless of the scripts execution location.

    Attributes:
        base (Path): root directory of the project.
        src (Path): source code directory (src).
        functions (Path): directory containing function modules (src/functions).
        notebooks (Path): directory for notes and notebooks (src/notebooks).
        data (Path): base data directory (data).
        raw (Path): directory for raw data files from databases (data/raw).
        raw_history (Path): directory for historical raw data (data/raw_history).
        processed (Path): directory for processed data files (data/processed).
        processed_history (Path): directory for historical processed data files (data/processed_history).
    """
    base = Path(__file__).resolve().parents[2]

    src = base / 'src'
    functions = src / 'functions'
    notebooks = src / 'notebooks'
    logs = src / 'log'

    data = base / 'data'
    
    #raw = data / 'raw'
    #raw_history = data / 'raw_history'
    #processed = data / 'processed'
    #processed_history = data / 'processed_history'