import json,  pyaudio
from vosk import Model, KaldiRecognizer

from os import makedirs, path, system
from gtts import gTTS

import pydub
import pydub.playback

from dotenv import load_dotenv
from os import environ

load_dotenv('.env')

import replicate


model = Model('small_model')

rec = KaldiRecognizer(model, 16000)
p = pyaudio.PyAudio()

stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True,frames_per_buffer=8000)
stream.start_stream()


def listen():
    while True:
        data = stream.read(num_frames=4000, exception_on_overflow=False)
        if (rec.AcceptWaveform(data)) and (len(data) > 0):
            answer  = json.loads(rec.Result())

            if answer['text']:
                yield answer['text']


def get_lama_answer(
    prompt,
    system_prompt,
    temperature=0.5,
    top_p=1,
    max_tokens=500,
):
    output = replicate.run(
        "replicate/llama-2-70b-chat:2796ee9483c3fd7aa2e171d38f4ca12251a30609463dcfd4cd76703f22e96cdf",
        input={
            "prompt": prompt,
            "system_prompt": system_prompt,
            "temperature": temperature,
            "top_p": top_p,
            "max_new_tokens": max_tokens,
        },
    )

    return "".join(output)


def generate_voice_message(text, language='ru', reply_to=None):
    """Got a text and generate voice file and return path to voice file"""
    if reply_to != None:
        message = reply_to

    voice_obj = gTTS(text=text, lang=language, slow=False)
    voice_obj.save("audio.mp3")
    sound = pydub.AudioSegment.from_mp3("audio.mp3")
    pydub.playback.play(sound)

    

    # system("audio.mp3")


print('работает')

for text in listen():

    print(f'LOG {text}')

    answer = get_lama_answer(prompt=text, system_prompt='Ты веселый собеседник, отвечай на русском языке')

    print(answer)

    generate_voice_message(text=answer)



    # if text == 'отправка платежей':
    #     generate_voice_message(text='отправка платежей выполнена')
    # elif text == 'проверка баланса':
    #     generate_voice_message(text='проверка баланса выполнена')
    # elif text == 'отправка переводов':
    #     generate_voice_message(text='отправка переводов выполнена')

    # else:
    #     generate_voice_message(text=f'еррор: ваш запрос: {text}')






    # if not path.exists("output\\voice_out"):
    #     makedirs("output\\voice_out")

    # voice_obj.save(f"output\\voice_out\\voice_out_{message.message_id}.mp3")

    # return f"output\\voice_out\\voice_out_{message.message_id}.mp3"

# отправка платежей;
    # проверка баланса;
    # отправка переводов. 

# model.get_model_by_name('small_model')
