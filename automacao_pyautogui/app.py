import pyautogui
from time import sleep

pyautogui.click(1295, 542, duration=2)
pyautogui.write('jhonatan')

pyautogui.click(1296, 568, duration=2)
pyautogui.write('123456')

pyautogui.click(1190, 595, duration=2)


try:
    with open('produtos.txt', 'r') as arquivo:
        for linha in arquivo:
            produto = linha.split(',')[0]
            quantidade = linha.split(',')[1]
            preco = linha.split(',')[2]
            
        pyautogui.click(1047, 530, duration=2)
        pyautogui.write(produto)

        pyautogui.click(1042, 554, duration=2)
        pyautogui.write(quantidade)

        pyautogui.click(1034, 580, duration=2)
        pyautogui.write(preco)

        pyautogui.click(907, 734, duration=1)
        sleep(1)
except FileNotFoundError:
    print("File 'produtos.txt' not found.")
except Exception as e:
    print(f"An error occurred: {e}")

    
