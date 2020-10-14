# quizlet-converter

quizlet-converter is a simple python script that converts exported quizlet files to a searchable database.
Created by Andrei Alin Popa

## How to use

### Obtaining the Quizlet database

1. Find your desired Quizlet set
2. While on flashcards, click on the three dot icon, then "export"
3. Under "Between term and definition", select "CUSTOM" and type "@@" (without the quotes) into the box
4. Under "Between rows", select "Semicolon"
5. Click "Copy text" and paste it into a text editor. Save as .txt

### Using the quizlet-converter python script

1. Run main.py using python3
2. Type in path to previously created .txt file
3. Once python is done reading the file, after "search:" type in your term
4. If only one similar match is found, it will display that one. Otherwise, it will number several options. Type in the corresponding number.
5. If no match is found, main.py will return "No match found"
6. To exit the software, close the entity of Python