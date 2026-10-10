from resemblyzer import VoiceEncoder,preprocess_wav
import numpy as np 
import streamlit as st 
import io
import librosa 

@st.cache_resource

def load_voice_encoder():
    return VoiceEncoder()

def get_voice_embedding(audio_bytes):
    try:
        encoder=load_voice_encoder()
        audio,sr=librosa.load(io.BytesIO(audio_bytes),sr=16000)
        wav=preprocess_wav(audio)
        embedding=encoder.embed_utterance(wav)
        return embedding.tolist()
    except Exception as e:
        st.error("voice recog error")
        return None

def identify_speaker(new_embedding,candidates_dict,threshold=0.65):
    if new_embedding is None or not candidates_dict:
        return None,0.0

    best_stid=None
    best_score=-1.0

    for sid,stored_embedding in candidates_dict.items():
        if stored_embedding:
            simlarity=float(np.dot(new_embedding, stored_embedding))
            if simlarity > best_score:
                best_score=simlarity
                best_stid=sid
    if best_score >= threshold:
        return best_stid, best_score
    else:
        return None,0.0

def process_bulk_audio(audio_bytes,candidates_dict,thresold=0.45):
    try:
        encoder=load_voice_encoder()

        audio,sr=librosa.load(io.BytesIO(audio_bytes),sr=16000)
        segments=librosa.effects.split(audio,top_db=30)

        identified_result={}

        for start,end in segments:
            if(end-start) < sr*0.5:
                continue
            segment_audio=audio[start:end]
            wav=preprocess_wav(segment_audio)
            embedding=encoder.embed_utterance(wav)

            sid,score =identify_speaker(embedding,candidates_dict,thresold)

            if sid:
                if sid not in identified_result or score > identified_result[sid]:
                    identified_result[sid]=score
        return identified_result
    except Exception as e:
        st.error(f"Bulk voice process error:{e}")
        return {}

