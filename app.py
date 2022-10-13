import streamlit as st 
import pandas as pd

test_german_ref= './refs/phoenix_test_sentences_lowercase.txt'
test_gloss_ref = './refs/phoenix_test_glosses_lowercase.txt'

test_gloss_BEST = './outputs/BEST_SYSTEM.txt'
test_gloss_baseline_1 ='./outputs/BASELINE_1.txt'
test_gloss_baseline_2 = './outputs/BASELINE_2.txt'

human_evaluation_path = './FEEDBACK_PHOENIX.txt'


if 'num' not in st.session_state:
    st.session_state.num = 0
if 'data' not in st.session_state:
    st.session_state.data = []

class ScoreSys:
    def __init__(self, page_id):
        #st.subheader(f"Comment of No.{page_id}")
        self.score1 = st.slider('Score for SYSTEM_1', 0, 6, 0)
        self.score2 = st.slider('Score for SYSTEM_2', 0, 6, 0)
        self.score3 = st.slider('Score for SYSTEM_3', 0, 6, 0)
        self.comments = st.text_input("Comment here if avaliable")
 
def main():
    
    st.title('PHOENIX human evaluation system')
    placeholder = st.empty()
    placeholder2 = st.empty()

    while True:    
        num = st.session_state.num

        if placeholder2.button('EXIT & SAVE COMMENTS', key=num):
            placeholder2.empty()
            df = pd.DataFrame(st.session_state.data)
            st.dataframe(df)
            df.to_csv(human_evaluation_path, index=None, header = True, sep = '\t',columns=['Score1','Score2','Score3','Comment','BAD_REF'])
            break
        else:        
            with placeholder.form(key=str(num)):
                Bad_refs = st.checkbox('Click if it is a bad reference')
                df_ger_ref = pd.read_table(test_german_ref,header = None, names = ['DGS GERMAN SENTENCE REFERENCE'])
                st.markdown(f'<u>**_PHOENIX GERMAN SENTENCE REFERENCE {num}_**</u>',unsafe_allow_html=True)
                st.markdown(f'<p style="font-family:Arial; color:White; font-size: 15px;">{df_ger_ref.iloc[int(num),0]}</p>', unsafe_allow_html=True)
            
                df_glo_ref = pd.read_table(test_gloss_ref,header = None, names = ['DGS GLOSS REFERENCE'])
                st.markdown(f'<u>**_PHOENIX GLOSS REFERENCE {num}_**</u>',unsafe_allow_html=True)
                st.markdown(f'<p style="font-family:Arial; color:White; font-size: 15px;">{df_glo_ref.iloc[int(num),0]}</p>', unsafe_allow_html=True)

                df_glo_sys_1 = pd.read_table(test_gloss_baseline_1,header = None, names = ['PREDICTION_SYSTEM_ONE'])
                st.markdown(f'<u>**_PREDICTION_SYSTEM_ONE_{num}_**</u>',unsafe_allow_html=True)
                st.markdown(f'<p style="font-family:Arial; color:White; font-size: 15px;">{df_glo_sys_1.iloc[int(num),0].lower()}</p>', unsafe_allow_html=True)
                
                df_glo_sys_2 = pd.read_table(test_gloss_baseline_2,header = None, names = ['PREDICTION_SYSTEM_TWO'])
                st.markdown(f'<u>**_PREDICTION_SYSTEM_TWO_{num}_**</u>',unsafe_allow_html=True)
                st.markdown(f'<p style="font-family:Arial; color:White; font-size: 15px;">{df_glo_sys_2.iloc[int(num),0].lower()}</p>', unsafe_allow_html=True)
                
                df_glo_sys_3 = pd.read_table(test_gloss_BEST,header = None, names = ['PREDICTION_SYSTEM_THREE'])
                st.markdown(f'<u>**_PREDICTION_SYSTEM_THREE_{num}_**</u>',unsafe_allow_html=True)
                st.markdown(f'<p style="font-family:Arial; color:White; font-size: 15px;">{df_glo_sys_3.iloc[int(num),0].lower()}</p>', unsafe_allow_html=True)
                systems = ScoreSys(page_id=num)        
                
                if st.form_submit_button('NEXT'): 
                    if Bad_refs != 1:               
                        st.session_state.data.append({
                        'Score1': systems.score1,
                        'Score2': systems.score2,
                        'Score3': systems.score3,
                        'Comment': systems.comments,
                        'BAD_REF': 0})
                    else:
                        st.session_state.data.append({
                        'Score1': 0,
                        'Score2': 0,
                        'Score3': 0,
                        'Comment': systems.comments,
                         'BAD_REF': 1})
                    st.session_state.num += 1
                    placeholder.empty()
                    placeholder2.empty()
                else:
                    st.stop()

main()


