from django.shortcuts import render, get_object_or_404
from .models import Semester, Marhala, Book, Note

def home(request):
    semesters = Semester.objects.all()
    return render(request, 'home.html', {'semesters': semesters})

def semester_detail(request, semester_id):
    semester = get_object_or_404(Semester, pk=semester_id)
    #marhalas = Marhala.objects.filter(semester=semester)

    marhalas = Marhala.objects.filter(semester=semester)

    return render(request, 'semester_detail.html', {'semester': semester, 'marhalas': marhalas,})

def marhala_detail(request, marhala_id):
    marhala = get_object_or_404(Marhala, pk=marhala_id)
    books = Book.objects.filter(marhala=marhala)
    notes = Note.objects.filter(marhala=marhala)
    return render(request, 'marhala_detail.html', {
        'marhala': marhala,
        'books': books,
        'notes': notes
    })
