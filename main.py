def display(name,student,dic):
    for (index,row) in student_data_frame.iterrows():
      if row['student']==name:
        print(f"Score: {row['score']}")
    nato_list=[dic[letter.upper()] for letter in name]
    print(nato_list)
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}
import pandas
student_data_frame = pandas.DataFrame(student_dict)
content=pandas.read_csv('nato_phonetic_alphabet.csv')
dic={row.letter:row.code for (index, row) in content.iterrows()}
name=input("Enter a name: ").title()
display(name,student_data_frame,dic)