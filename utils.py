import glob


def get_all_reports_current_dir():
    return glob.glob("./report*.csv")
