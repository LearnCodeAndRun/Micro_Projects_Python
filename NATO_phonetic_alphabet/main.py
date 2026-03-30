def display(name,student,dic):
    try:
      for (index,row) in student_data_frame.iterrows():
        if row['student']==name:
          print(f"Score: {row['score']}")
      nato_list=[dic[letter.upper()] for letter in name]
      print(nato_list)
    except KeyError:
       print("The given value does not exist")
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}
import pandas
student_data_frame = pandas.DataFrame(student_dict)
content=pandas.read_csv('./NATO_phonetic_alphabet/nato_phonetic_alphabet.csv')
dic={row.letter:row.code for (index, row) in content.iterrows()}
try:
    name=input("Enter a name: ").title()
    if name.isalpha():
      display(name,student_data_frame,dic)
    else:
      raise ValueError("Input contains non - alphabet characters")
except ValueError as e:
   print(f"Error: {e}")