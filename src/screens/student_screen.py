import streamlit as st
from src.components.header import header_dashboard
from src.components.footer import footer_dashboard
from src.ui.base_layout import style_base_layout,style_background_dashboard
from PIL import Image
import numpy as np
from src.pipeline.face_pipeline import predict_attendance,get_face_embedding,train_classifier
from src.pipeline.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students,create_student,get_student_subjects,get_student_attendance,unenroll_student_subject
from src.components.dialog_enroll import enroll_dialog
from src.components.subject_card import subject_card


def student_dashboard():
    student_data=st.session_state.student_data
    student_id=student_data['student_id']
    c1,c2=st.columns(2,vertical_alignment="center",gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"""welcome,{student_data['name']}""")
        if st.button('Logout',type="secondary",key='loginbckbtn',shortcut="control+backspace"):
            st.session_state['is_logged_in']=False
            del st.session_state.student_data
            st.rerun()

    st.space()

    col1,col2=st.columns(2)

    with col1:
        st.header("Your Enroll Subjects")
    with col2:
        if st.button("Enroll in subject",type='primary',width='stretch'):
            enroll_dialog()
    
    st.divider()

    with st.spinner("Loading your enrolled subjects.."):
        subjects=get_student_subjects(student_id)
        logs=get_student_attendance(student_id)

    stats_map={}
    for log in logs:
        sid=log['student_id']

        if sid not in stats_map:
            stats_map[sid]={"total":0,'attended':0}

        stats_map[sid]['total']+=1

        if log.get('is_present'):
            stats_map[sid]['attended']+=1

    cols =st.columns(2)
    for i,sub_nodes in enumerate(subjects):
        sub=sub_nodes['subjects']
        sid=sub['subject_id']

        stats=stats_map.get(sid,{"total":0,"attended":0})
        def unenroll_button():
               if st.button("Unenroll form this course",type="tertiary",width="stretch",icon=':material/delete_forever:', key=f"unenroll_{sid}"):
                   unenroll_student_subject(student_id,sid)

        with cols[i%2]:
            subject_card(
                name=sub['name'],
                code=sub['subject_code'],
                section=sub['section'],
                stats=[
                    ('📅 ','Total',stats['total']),
                    ('✅ ','Attended',stats['attended']),
                ],
                footer_callback=unenroll_button
            )

    footer_dashboard()

def student_screen():

    style_background_dashboard()
    style_base_layout()

    show_registration = False

    if "student_data" in st.session_state:
        student_dashboard()
        return

    c1,c2=st.columns(2,vertical_alignment='center',gap='xxlarge')
    with c1:
        header_dashboard()
    with c2 :
       if st.button("Go back to home", type="secondary", key="logbckbtn", width='content'):
         st.session_state["login_type"] = None
         st.rerun()
    
    st.header("Login using Face ID",text_alignment="center")

    st.space(2)
    
    photo_source=st.camera_input("Position your face in center")

    if photo_source:
        img=np.array(Image.open(photo_source))

        with st.spinner("Ai is scanning..."):
            detected,all_ids,num_faces=predict_attendance(img)

            if num_faces==0:
                st.warning('Face not found!')

            elif num_faces>1:
                st.warning('Multiple faces found')
            else: 
                if detected:
                    student_id=list(detected.keys())[0]
                    all_students=get_all_students()
                    student=next((s for s in all_students if s['student_id']==student_id),None)

                    if student:
                        st.session_state.is_logged_in=True
                        st.session_state.user_role="student"
                        st.session_state.student_data=student
                        st.toast(f"Welcome back {student['name']}")
                        import time
                        time.sleep(1)
                        st.rerun()
                else:
                 st.info("Face not recognized! you might be a new student")
                 show_registration=True

    if show_registration:
        with st.container(border=True):
            st.header('Register new profile')
            new_name=st.text_input("Enter your name",placeholder="E.g.abhay pratap")

            st.subheader("Optional:Voice Enrollment")
            st.info("Eroll your voice only for attendance")

            audio_data=None

            try:
                audio_data=st.audio_input("Record a short pharse like I am present , My Name is Abhay")
            except Exception:
                st.error("Audio data  failed")

            if st.button("Create account",type="primary"):
                if  new_name:
                    with st.spinner("Creating your Profile.."):
                        img=np.array(Image.open(photo_source))
                        encodings=get_face_embedding(img)
                        if encodings:
                            face_emb=encodings[0].tolist()

                            voice_emb=None
                            if audio_data:
                                voice_emb=get_voice_embedding(audio_data.read())
                            else:
                                voice_emb=None

                            response_data=create_student(new_name,face_embedding=face_emb,voice_embedding=voice_emb)

                            if response_data:
                                train_classifier()
                                st.session_state.is_logged_in=True
                                st.session_state.user_role='student'
                                st.session_state.student_data=response_data[0]
                                st.toast(f"Profile Created! Hi {new_name}")
                                import time
                                time.sleep(1)
                                st.rerun()
                            else:
                                st.error('Couldnt capture your facial feature for registration')

                else:
                    st.warning("Please enter your name!")      
                      

    footer_dashboard()     
