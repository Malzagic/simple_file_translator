from pathlib import Path
from translate import Translator

p = Path(".")
# Absolute Path to script direcotry
absolute_path = p.absolute()
# You can change the language base on wikipedia page about ISO-639-1:2002 Language Standard
language_used = "pl"
translator= Translator(to_lang=f"{language_used}")

try: 
  with open(f"{absolute_path}/test.txt", mode="r") as my_file:
    txt = my_file.read()
    translation = translator.translate(txt)
    with open(f"{absolute_path}/translated.txt", mode="w") as my_file2:
      my_file2.write(translation)
except FileNotFoundError as err:
  print(err)
except IOError as err:
  print(err)