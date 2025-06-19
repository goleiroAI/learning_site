from django.shortcuts import render, get_object_or_404
from .models import Lesson

def lesson_list(request):
    lessons = Lesson.objects.all().order_by('chapter', 'number')
    return render(request, 'lessons/lesson_list.html', {'lessons': lessons})

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'lessons/lesson_detail.html', {'lesson': lesson})
