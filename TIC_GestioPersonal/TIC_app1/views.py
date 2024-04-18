from django.shortcuts import render


def students(request):
    students_data = [
        {"nom": "Jordi", "cognom1": "Hondureño", "cognom2": "García", "correu": "jordi@example.com", "curs": "2n", "mòduls_matriculats": ["Matemàtiques", "Història"]},
        {"nom": "Maria", "cognom1": "González", "cognom2": "Pérez", "correu": "maria@example.com", "curs": "1r", "mòduls_matriculats": ["Biologia", "Física"]},
        {"nom": "Pablo", "cognom1": "Martínez", "cognom2": "López", "correu": "pablo@example.com", "curs": "3r", "mòduls_matriculats": ["Química", "Llengua"]},
        {"nom": "Sara", "cognom1": "Ruiz", "cognom2": "Sánchez", "correu": "sara@example.com", "curs": "2n", "mòduls_matriculats": ["Història de l'Art", "Educació Física"]},
        {"nom": "Marc", "cognom1": "Fernández", "cognom2": "García", "correu": "marc@example.com", "curs": "1r", "mòduls_matriculats": ["Música", "Informàtica"]}
    ]
    return render(request, 'student.html', {"data": students_data})

def teachers(request):
    teachers_data = [
        {"nom": "Oriol", "cognom1": "Roca", "cognom2": "Martínez", "correu": "oriol@example.com", "curs": "2n", "tutor": "Física", "mòduls_impartits": ["Matemàtiques", "Física"]},
        {"nom": "Laura", "cognom1": "Fernández", "cognom2": "López", "correu": "laura@example.com", "curs": "1r", "tutor": "Química", "mòduls_impartits": ["Química", "Biologia"]},
        {"nom": "Carlos", "cognom1": "Gómez", "cognom2": "Sánchez", "correu": "carlos@example.com", "curs": "3r", "tutor": "Biologia", "mòduls_impartits": ["Biologia", "Matemàtiques"]},
        {"nom": "Elena", "cognom1": "Martínez", "cognom2": "Fernández", "correu": "elena@example.com", "curs": "2n", "tutor": "Història", "mòduls_impartits": ["Història", "Filosofia"]},
        {"nom": "David", "cognom1": "González", "cognom2": "López", "correu": "david@example.com", "curs": "1r", "tutor": "Llengua", "mòduls_impartits": ["Llengua", "Català"]}
    ]
    return render(request, 'teacher.html', {"data": teachers_data})


def index(request):
    return render(request, 'index.html')
