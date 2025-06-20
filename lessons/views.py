from django.shortcuts import render
from .models import Lesson
from collections import defaultdict
from django.http import HttpResponseForbidden

ACCESS_KEY = "abc123"  # このキーだけ許可

def lesson_list(request):
    key = request.GET.get("access", "")
    if key != ACCESS_KEY:
        return HttpResponseForbidden("このページは限定公開です。")

    lessons = Lesson.objects.all().order_by('chapter', 'number')
    grouped_lessons = defaultdict(list)
    for lesson in lessons:
        grouped_lessons[lesson.chapter].append(lesson)
    return render(request, 'lessons/lesson_list.html', {'grouped_lessons': grouped_lessons, 'lessons': lessons})
from django.shortcuts import get_object_or_404

def lesson_detail(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'lessons/lesson_detail.html', {'lesson': lesson})
