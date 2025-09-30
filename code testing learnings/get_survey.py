from survey import AnonymousSurvey

question='What language do you like?'
my_survey=AnonymousSurvey(question)
my_survey.show_question()
print('Enter q to quit')

while True:
    language=input('list the names:')
    
    if language=='q':
        break
    my_survey.store_response(language)

print('Thanks to everyone who participated!')
my_survey.show_results()