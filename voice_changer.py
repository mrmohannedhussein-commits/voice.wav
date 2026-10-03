"""
Voice Changer - تغيير الصوت بشكل طبيعي (بدون ذكاء اصطناعي)

التثبيت (في Google Colab):
    !pip install pyworld librosa soundfile

التشغيل:
    !python voice_changer.py voice.wav woman
الخيارات: woman, child, man
"""

import sys
import numpy as np
import pyworld as pw
import librosa
import soundfile as sf

# pitch = حدة الصوت ، formant = لون الصوت
# جرّب تغيّر الأرقام لين يطلع الصوت حلو
PRESETS = {
    "woman": {"pitch": 1.6, "formant": 1.15},  # من رجل لامرأة
    "child": {"pitch": 2.0, "formant": 1.30},  # من رجل لطفل
    "man":   {"pitch": 0.6, "formant": 0.85},  # من امرأة لرجل
}


def change_voice(input_path, output_path, pitch_ratio, formant_ratio):
