# Streamlit

## Basic setup
## For Mac & Windows user:

1. Clone the repository or download the repository
 
        git clone https://github.com/yvanzhu/Sign_language_human_evaluation.git
        
2. Install the Python3 (Better the newest version)
3. Open the Terminal and change directory to
        
        cd ./Sign_language_human_evaluation/Phoenix_evaluation

4. Install the Python Requirements

        pip3 install -r requirements.txt

5. Run app.py

        streamlit run app.py

Open the browser at http://localhost:8501/

Hints:
1. If you think it is a bad reference either in source side or target side, click the top button of the interface and leave the comment below. The scores will be automatically saved to 0 and also the comment.
2. Score slider counts from 0 to 6 in integer. 
3. Leave comments if you think it is necessary to explain.
4. There is a big drawback of this interface: YOU CAN NOT SHUT DOWN THE TERMINAL UNTIL EVALUATION FINISHED. 
If you need multiple times to finish all the evaluation. Every time you need pause, just click "EXIT & SAVE" and the keep the web interface and terminal on. If you need continuing with evaluation, click the icon of top right corner and then click "Rerun", you will back to the page. 
5. At the end, you will find a file named "FEEDBACK_PHOENIX.txt" which is the summary of the evaluation.
