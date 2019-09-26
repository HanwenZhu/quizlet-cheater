# Quizlet Match Cheater
Use this to ~~beat your friends in Quizlet Match games~~ lEaRn HoW tO dO pRoGrAmMiNg.

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
- I initially wanted to keep the code not opensourced. But after 22 seconds of thought, I think a bunch of other people will want to use this.
- If you read the source javascript code of Quizlet Matches, if it discovers that you cheat, it will label you as a `time_changing_scatter_cheater`.
