import speech_recognition as sr
import operator

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... (Say '5 plus 5' or '10 minus 3')")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
        except sr.RequestError:
            print("Could not request results. Check internet.")
        except Exception as e:
            print(f"Error: {e}")
    return None

def calculate(text):
    if not text: return
    
    ops = {
        'plus': operator.add,
        'added to': operator.add,
        'minus': operator.sub,
        'times': operator.mul,
        'multiplied by': operator.mul,
        'divided by': operator.truediv
    }
    
    words = text.split()
    try:
        num1 = None
        op_func = None
        num2 = None
        
        for word in words:
            if word.isdigit():
                if num1 is None: num1 = float(word)
                else: num2 = float(word)
            elif word in ops:
                op_func = ops[word]
        
        if num1 is not None and num2 is not None and op_func:
            result = op_func(num1, num2)
            print(f"Result: {result}")
        else:
            print("Could not find a valid calculation pattern.")
            
    except Exception as e:
        print(f"Calculation error: {e}")

def main():
    print("--- Voice Calculator ---")
    print("Note: Requires internet for recognition.")
    while True:
        input("Press Enter to speak (or 'q' to quit)...")
        text = get_voice_input()
        calculate(text)
        
        cont = input("Continue? (y/n): ")
        if cont.lower() != 'y':
            break

if __name__ == "__main__":
    main()
