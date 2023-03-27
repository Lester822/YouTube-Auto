import time
import pyautogui
import pyperclip

def chat_gpt(inquiry):
    time.sleep(10)
    pyautogui.keyDown('ctrl')
    pyautogui.press('r')
    pyautogui.keyUp('ctrl')
    time.sleep(3)
    def getGPT():
        # GET INFORMATION
        pyautogui.click(1000, 500)
        pyautogui.keyDown('ctrl')
        pyautogui.press('a')
        pyautogui.press('c')
        pyautogui.keyUp('ctrl')
        response = pyperclip.paste()
        return response

    # CLICK ON BOX
    pyautogui.click(1000, 955)

    # PUT INTO CHAT GPT
    inquiry = inquiry.replace('\n', '')
    pyautogui.write(inquiry)
    pyautogui.press('enter')

    time.sleep(20)

    # PROCESS INFORMATION

    valid = False
    while not valid:
        try:
            response = getGPT()  # GETS INFORMATION
            splitList = response.split('\n')
            reduced = []
            for line in splitList:
                if line.strip() != '':
                    reduced.append(line.strip())
            print(inquiry)
            start = reduced.index(inquiry) + 1
            print(reduced)
            end = reduced.index('Regenerate response')
            output = reduced[start:end]
            output_string = '\n'.join(output)
            print(splitList)
            if 'Stop generating' not in reduced:
                valid = True
        except:
            time.sleep(5)
    return output_string