import requests

from bs4 import BeautifulSoup

import PySimpleGUI as sg

#The Url for the Ticker you are looking for is formated in the function
def get_url(ipo):
    template = "https://www.wallstreetzen.com/stocks/us/nasdaq/{}"
    URL = template.format(ipo)
    return URL
#The Value of the Stocks Last Close is Scraped
def last_Close(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find('div', 'MuiGrid-root jss148 MuiGrid-container')
    #The Class with the Content The Last Close Price is found and returned with its value
    Last_Close = results.find('div', 'MuiTypography-root MuiTypography-h4').text.strip()
    return Last_Close

def main():
    #display window is created to take input of what Stock you are looking at.
    sg.theme('DarkAmber')
    layout = [[sg.Text("Enter The Stock Ticker You want to Track")], [sg.InputText()],[sg.Button('Enter')]]
    window = sg.Window('Indeed', layout)
    while True:
        event, ipo = window.read()
        if event == sg.WIN_CLOSED or event == 'Enter':
            sg.WIN_CLOSED
            break
    #The entered Ticker is turned into a Url and its price is Scraped
    URL = get_url(ipo[0])
    Stock = last_Close(URL)
    #The Last Close Value is Displayed in a new window
    sg.theme('DarkAmber')
    layout = [[sg.Text(" The Last Close of the Stock Was:")],[sg.Text(Stock)]]
    window = sg.Window('Indeed', layout)
    window.read()

if __name__ == "__main__":
    main()








