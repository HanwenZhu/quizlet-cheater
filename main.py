import getpass
import json
import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def strip_html_whitespace(string):
    if isinstance(string, str):
        return '\n'.join(line.strip() for line in string.split('\n'))
    else:
        return string


def login(driver, username, password):
    driver.set_window_size(500, 800)

    driver.get('https://quizlet.com')
    driver.implicitly_wait(10)
    sign_in = driver.find_element(
        By.CSS_SELECTOR,
        'span.SiteHeader-signInBtn'
    )
    sign_in.click()
    username_input = driver.find_element(
        By.CSS_SELECTOR,
        'body > div.UIModal.UIModal-container.is-white.is-open > div > div.UIM'
        'odalBody > form > div > div > label:nth-child(1) > div > input'
    )
    username_input.send_keys(username)
    password_input = driver.find_element(
        By.CSS_SELECTOR,
        'body > div.UIModal.UIModal-container.is-white.is-open > div > div.UIM'
        'odalBody > form > div > div > label:nth-child(2) > div.UIInput-conten'
        't > input'
    )
    password_input.send_keys(password)
    log_in = driver.find_element(
        By.CSS_SELECTOR,
        'body > div.UIModal.UIModal-container.is-white.is-open > div > div.UIM'
        'odalBody > form > button'
    )
    log_in.click()

    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, '#DashboardPageTarget')


def play(driver, set_number, desired_time='0.5'):
    # Totally could have ignored definitions and try out every
    # combination.  But we're civilized.
    if os.path.isfile(f'{set_number!s}-dict.json'):
        with open(f'{set_number!s}-dict.json', 'r') as file:
            definitions = json.load(file)
    else:
        driver.get(f'https://quizlet.com/{set_number!s}')
        terms = driver.execute_script(
            'return Object.values(window.Quizlet.setPageData.termIdToTermsMap)'
        )
        definitions = {
            strip_html_whitespace(term['word']):
                strip_html_whitespace(term['definition'] or term['_imageUrl'])
            for term in terms
        }
        with open(f'{set_number!s}-dict.json', 'w') as file:
            json.dump(definitions, file)

    driver.get(f'https://quizlet.com/{set_number!s}/match')
    driver.implicitly_wait(10)
    start = driver.find_element(
        By.CSS_SELECTOR,
        'body > div.UIModal.UIModal-container.is-white.is-open > div > div > d'
        'iv > div.MatchModeInstructionsModal-button > button'
    )
    start.click()
    driver.execute_script('''document.getElementsByClassName('''
                          ''''MatchModeControls-currentTime')[0]'''
                          '''.addEventListener('DOMSubtreeModified', '''
                          '''function() {\n'''
                          f'''\tif (this.innerHTML === '{desired_time!s}')\n'''
                          '''\t\tfor (var i = 0; i < 100; i++)\n'''
                          '''\t\t\tclearInterval(i);\n'''
                          '''})''')
    blocks = driver.find_elements(By.CSS_SELECTOR,
                                  'div.MatchModeQuestionGridTile')
    texts = []
    for block in blocks:
        if 'is-imageOnly' not in block.get_attribute('class').split(' '):
            texts.append(block.find_element(
                By.CSS_SELECTOR, 'div.MatchModeQuestionGridTile-text > div'
            ).text)
        else:
            texts.append(block.find_element(
                By.CSS_SELECTOR, 'div.MatchModeQuestionGridTile-image'
            ).value_of_css_property('background-image')[5:-2])
    for i, text in enumerate(texts):
        if text in definitions:
            blocks[i].click()
            for j, t in enumerate(texts):
                if t == definitions[text]:
                    blocks[j].click()
                    break
            else:
                print(f'No definition for {text!r} found')


if __name__ == '__main__':
    if len(sys.argv) > 2:
        print('Usage: python3 main.py [<setnumber>]\n\n'
              'Read `README.md` for more.')
        sys.exit(2)
    elif len(sys.argv) == 0:
        set_number = input('Quizlet set number: ')
    else:
        set_number = sys.argv[1]

    username = input('Username: ')
    password = getpass.getpass('Password: ')

    with webdriver.Chrome() as driver:
        login(driver, username, password)
        play(driver, sys.argv[1])

        time.sleep(10000)
