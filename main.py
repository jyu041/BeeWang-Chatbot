from difflib import SequenceMatcher as SQM
import glob, json, string, random, time, os
import speech_recognition as sr 
import pyttsx3

PATH = './data' # Set the folder where you store your "training data"

engine = pyttsx3.init()
unknown_dialogues = {}
r = sr.Recognizer()  

if os.path.isdir(PATH) == False:
    os.mkdir(PATH)

def similar(a, b):
    return SQM(None, a, b).ratio()

def speak(audio):
    global engine
    engine.say(audio)  
    engine.runAndWait()

def load_files(file_path):
    global data
    files = glob.glob(f'{file_path}/*.json')
    data = {}
    try:
        for each_file in files:
            data.update(json.load(open(each_file,'r')))
    except:
        pass
    
def learn_file(data_to_learn, file_path):

    print('[info]: Saving dialogues just inputted...')
    speak('Saving dialogues just inputted')
    if len(unknown_dialogues) == 0:
        print('[error]: You did not enter any dialogue to learn')
        speak('You did not enter any dialogue to learn')

    files = glob.glob(f'{file_path}/*.json')
    new_file = lambda: ''.join([random.choice(string.ascii_lowercase) for i in range(20)]) + '.json'
    new_file_name = new_file()
    if new_file_name in files:
        learn_file(data_to_learn, file_path)
    else:
        with open(f'{file_path}/{new_file_name}','a+') as create_new_file:
            json.dump(data_to_learn, create_new_file, ensure_ascii=False, indent=4)
            print('[info]: Your new dialogues have been saved... reloading data...')
            speak('Your new dialogues have been saved, reloading data')

        unknown_dialogues.clear()
        print(unknown_dialogues)
        load_files(file_path)
       
def add_to_unknown(uk):
    global unknown_dialogues
    inform_msg = f'[BeeWang]:\n I do not understand what this means:\n    "{uk}"\n Please tell me what to reply to this message\n Type "/finished" to stop\n'
    print(inform_msg)
    gathered_new_info = []
    while True:
        usr_input = input('[Learning] >>> ')
        if usr_input.replace(' ','') == '/finished':
            if len(gathered_new_info) != 0:
                unknown_dialogues.update({uk:gathered_new_info})
                print('Stopped')
                break
            else:
                print('You did not teach me anything')
        gathered_new_info.append(usr_input)

def displaying(user_entry):
    high_match = {}
    for possible_data in data.keys():
        matching_ratio = similar(user_entry, possible_data)
        if matching_ratio >= 0.8:
            high_match.update({possible_data:matching_ratio})

    print(f'[You]    : {user_entry}')
    if user_entry == '/save_dialogue':
        learn_file(unknown_dialogues, PATH)

    elif len(high_match) == 0:
        add_to_unknown(user_entry)

    else:
        if isinstance(data[max(high_match, key=high_match.get)], (str, int, float)):
            print(f'[BeeWang]: {data[max(high_match, key=high_match.get)]}\n[You]    : ', end='')
            speak(data[max(high_match, key=high_match.get)])
        
        if isinstance(data[max(high_match, key=high_match.get)], (list, tuple)):
            list_choice = random.choice(data[max(high_match, key=high_match.get)])
            print(f'[BeeWang]: {list_choice}\n[You]    : ', end='')
            speak(list_choice)

if __name__ == '__main__': # Main routine below
    print('''    [info]: Thankyou for using BeeWang fake AI learning chatbot
    [info]: This chatbot learns by constant user inputs
    [info]: When it sees something it does not understand
    [info]: it poses a question for the outputs the user wants it to respond with
    [info]: next time it sees the same input, it would pick a random response\n[You]    : ''')
    load_files(PATH)
    while True:
        try:
            with sr.Microphone() as source2:
                # wait for a second to let the recognizer
                # adjust the energy threshold based on
                # the surrounding noise level
                r.adjust_for_ambient_noise(source2, duration=0.2) 
                
                #listens for the user's input
                audio2 = r.listen(source2)
                
                # Using google to recognize audio
                MyText = r.recognize_google(audio2) 
                MyText = MyText.lower() 

                #displaying(str(input('[Beewang] >>> ')))
                displaying(MyText)

        except sr.RequestError as e:
            print(f"Could not request results; {e}")

        except sr.UnknownValueError:
            print("unknown error occured")