import pandas as pd
import sys
from sklearn.metrics import f1_score

def main(test_labels_path, submission_path):
    try:
        y_true = pd.read_csv(test_labels_path)['Outcome']
        y_pred = pd.read_csv(submission_path)['Outcome']
        
        # Calculate Weighted F1
        score = f1_score(y_true, y_pred, average='weighted')
        print(f"SCORE:{score}") 
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])