

print('AskPython Quiz')
answer=input('Сіз викторинаға қатысуға дайынсыз ба? (yes/no) :')
score=0
total_questions=3

if answer.lower()=='yes':
    answer=input('1-сұрақ: сіздің сүйікті бағдарламалау тіліңіз қандай?')
    if answer.lower()=='python':
        score += 1
        print('correct')
    else:
        print('Қате жауап :(')


    answer=input('2-сұрақ: Сіз кез-келген Github авторына жазыласыз ба? ')
    if answer.lower()=='yes':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('3-сұрақ: сіздің сүйікті оқу веб-сайтыңыз қалай аталады Python?')
    if answer.lower()=='github':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

print('Осы кішкентай викторинаны ойнағаныңыз үшін рахмет, сіз тырыстыңыз',score,"сұрақтар дұрыс!")
mark=(score/total_questions)*100
print('Алынған бағалар:',mark)
print('Сау бол!')