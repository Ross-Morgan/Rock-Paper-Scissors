import os

ASSET_DIR = f"{os.path.dirname(__file__)}/Assets"


def _asset(name) -> str:
    return f"{ASSET_DIR}/{name}"


class Assets:
    """Asset Paths"""
    background = _asset("battleship-grey.jpg")
    info_icon = _asset("information.png")
    rock = _asset("rock.png")
    paper = _asset("paper.png")
    scissors = _asset("scissors.png")

