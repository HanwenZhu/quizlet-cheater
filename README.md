# Quizlet Match Cheater
Use this to ~~beat your friends in Quizlet match games~~ lEaRn HoW tO dO pRoGrAmMiNg.

It can reach a speed of 0.5s for Quizlet matches (it could be 0.0s, but the fastest score the server accepts is 0.5s).

## Warning
This software is made and should **only** be used **for educational purposes**. Users should be responsible for using this software.

## Usage
1. Download the repository:
```sh
git clone https://github.com/HanwenZhu/quizlet-cheater.git
cd quizlet-cheater
```
2. Install dependencies:
```sh
pip install -U -r requirements.txt
```
And see [https://selenium-python.readthedocs.io/installation.html](https://selenium-python.readthedocs.io/installation.html) to install browser drivers, for your corresponding browser version.

3. Go to the desired Quizlet set and copy the _set number_. It is the first string of numbers in the URL of your set. It should be about (but not always) 9 (?) characters long.
4. Run the code:
```sh
python3 main.py
```
5. Paste the _set number_. Enter your Quizlet username and password.
6. Sit back.

## Remarks
- After many trials, I found that the fastest score the server accepts is 0.5 seconds.
- I initially wanted to keep the code not opensourced. But after 22 seconds of thought, I thought a bunch of other people will also want to use this.
- In the JavaScript source code of Quizlet matches, you can see that if Quizlet discovers that you're cheating, it will designate you as a `time_changing_scatter_cheater`.
- Feel free to use or change this code, as long as you comply with the license.
