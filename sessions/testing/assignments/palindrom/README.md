# Palindrom script + testing

Your mission is to write a script that checks if a word is a palindrom (very simple in python - don't try to implement yourself as that is not what's the assignment about).

A few rules to begin with (Step1):
1. Please ignore case sensitivity fo now (the word abBa is actually a palindrom but ignore and let your script say it is not)
2. A word should be minimum 2 words for it to be a palindrom (e.g. single letters like "d" or "F" are not palindroms)

A few examples runs for you to better understand the requirements:

```shell
python check_palindrom.py abba → Yes!
python check_palindrom.py abBa → No!
python check_palindrom.py BOB → Yes!
python check_palindrom.py eyal → No!
python check_palindrom.py b → No!
```

### Addtional steps

After you have completed the above implementation of the code and the script can run from cmd like the above examples show, follow each of the below steps and implement as requested:

*NOTE*: It is important you implement each step by it's own, please don't rush yourself to do all the steps at once. Trust me, this will better help you learn the concepts of testing.

*Step2* - Add tests to your initial implementation! Run them with “pytest” make sure they pass. Make sure you cover the 2 rules mentioned at Step1
*Step3* - Implement that the letters “I”,"i",“A”, "a" are also palindroms (Remember, you can still ignore case sensitivity)
*Step4* - Add more tests for Step3. Run them with “pytest” make sure they all pass.
*Step5* - Make the palindrom check ignore case sensativity. This means that for words like "abBa" or "BOb" your check should return “Yes!”.
*Step6* - Add more tests for Step5. Run them with “pytest” make sure they all pass.
