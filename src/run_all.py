from pathlib import Path
import sys

RAW_DIR = Path("data/raw")
PROCESSED_DIR = Path("data/processed")
FIG_DIR = Path("results/figures")
TABLE_DIR = Path("results/tables")

def check_data():
    if not RAW_DIR.exists():
        raise FileNotFoundError("Missing data/raw/. See data/README.md for download instructions.")

    # TODO: Fill these in once your teammate confirms exact filenames
    required = [
        # "YOUR_FILE_1",
        # "YOUR_FILE_2",
    ]
    missing = [f for f in required if not (RAW_DIR / f).exists()]
    if missing:
        raise FileNotFoundError(
            "Missing required raw files in data/raw/: " + ", ".join(missing) +
            "\nUpdate required[] in src/run_all.py after confirming filenames."
        )

def main():
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    print("1) Checking data...")
    check_data()

    print("2) Preprocess (TODO)")
    # from src.preprocess import preprocess
    # preprocess()

    print("3) Analysis (TODO)")
    # from src.analysis import run_analysis
    # run_analysis()

    print("4) Figures (TODO)")
    # from src.figures import make_figures
    # make_figures()

    print("Done. Check results/figures and results/tables.")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)
