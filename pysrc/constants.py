from pathlib import Path

cachepath = lambda x: (Path(__file__).parent.parent / "cache" / x).resolve()
datapath = lambda x: (Path(__file__).parent.parent / "data" / x).resolve()
chartpath = lambda x: (Path(__file__).parent.parent / "charts" / x).resolve()

N_ITEMS = 91599
N_USERS = 52643