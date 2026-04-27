import pandas as pd
import sys
from sklearn.metrics import f1_score

def main(test_labels_path, submission_path):
    # We use a try-except to catch the EXACT error and print it to the GitHub log
    try:
        df_true = pd.read_csv(test_labels_path)
        df_pred = pd.read_csv(submission_path)

        # Check if column exists
        if 'Outcome' not in df_true.columns or 'Outcome' not in df_pred.columns:
            print(f"ERROR: Missing 'Outcome' header. Secret columns: {list(df_true.columns)}, Sub columns: {list(df_pred.columns)}")
            sys.exit(1)

        y_true = df_true['Outcome']
        y_pred = df_pred['Outcome']
        
        print(f"DEBUG: Secret rows: {len(y_true)}, Submission rows: {len(y_pred)}")

        score = f1_score(y_true, y_pred, average='weighted')
        print(f"SCORE:{score}") 
    except Exception as e:
        print(f"PYTHON CRASH: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])