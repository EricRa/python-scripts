from pathlib import Path


def get_dl_folder():
    """
    Attempts to get the path to the user's system Downloads folder and
    return that path as a string.

    This should work cross-platform.

    This will only work if the system Downloads folder is in the default
    location (home/Downloads, ~/Downloads, etc).

    Script can be easily modified to get the path to other folders by
    replacing "Downloads" in the Path call with any other home location.

    Usage example:

    from get_dl_folder import get_dl_folder as gdf
    path = gdf()
    print(path)

    """

    try:
        folder = Path.home() / "Downloads"
        if folder.exists():
            return str(folder)
        else:
            print("The Downloads folder was not found at the default location")
    except Exception as e:
        print(f"There was an error: {e}")
        print("The Downloads folder could not be found")
