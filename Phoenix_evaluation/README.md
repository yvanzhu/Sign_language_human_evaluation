# Streamlit evaluation interface

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

## The interface
<img src="https://github.com/yvanzhu/Sign_language_human_evaluation/blob/main/Phoenix_evaluation/Interface.png" width="400" height="600" alt="Image text"/><br/>

1. If you think it is a bad reference either in source side or target side, click the top button of the interface and leave the comment below. The scores will be automatically saved to 0.

2. Score slider counts from 0 to 6 in integer. 

3. Leave comments if you think it is necessary to explain.

4. A big drawback of this interface: <font color=red>**_YOU CAN NOT SHUT DOWN THE TERMINAL UNTIL EVALUATION FINISHED_**</font>. 

  If you need multiple times to finish all the evaluation, every time you need pause, just click "EXIT & SAVE COMMENTS" and then keep the web interface and Terminal on. When you go back to evaluation, click the icon of top right corner and then click "Rerun", you will back to the page and continue evaluation. 

5. At the end, you will find the file "FEEDBACK_PHOENIX.txt" under the directory.
