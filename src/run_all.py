# src/run_all.py
from pathlib import Path
import sys

# Repo root = folder that contains src/, data/, results/, etc.
REPO_ROOT = Path(__file__).resolve().parents[1]

RAW_DIR = REPO_ROOT / "data" / "raw"
PROCESSED_DIR = REPO_ROOT / "data" / "processed"
FIG_DIR = REPO_ROOT / "results" / "figures"
TABLE_DIR = REPO_ROOT / "results" / "tables"


def check_data():
    """
    Checks that raw PATH files exist in data/raw/.
    We only enforce filenames once you confirm them with your teammate.
    """
    if not RAW_DIR.exists():
        raise FileNotFoundError(
            f"Missing folder: {RAW_DIR}\n"
            "Create data/raw/ and place the PATH files there.\n"
            "See data/README.md for instructions."
        )

    # TODO: When your teammate confirms exact filenames, list them here.
    REQUIRED_FILES = [
        # "example_wave5_file.ext",
        # "example_wave6_file.ext",
        # "example_wave7_file.ext",
    ]

    missing = [name for name in REQUIRED_FILES if not (RAW_DIR / name).exists()]
    if missing:
        raise FileNotFoundError(
            "Missing required raw files in data/raw/: " + ", ".join(missing) + "\n"
            "Fix: add the files OR update REQUIRED_FILES in src/run_all.py."
        )


def main():
    # Ensure output folders exist
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    print("1) Checking data...")
    check_data()

    # Import here so errors are cleaner
    from .preprocess import preprocess
    from .analysis import run_analysis
    from .figures import make_figures

    print("2) Preprocess...")
    preprocess()

    print("3) Analysis...")
    run_analysis()

    print("4) Figures...")
    make_figures()

    print("\n✅ Done. Outputs saved to:")
    print(f"   Figures: {FIG_DIR}")
    print(f"   Tables : {TABLE_DIR}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        sys.exit(1)
