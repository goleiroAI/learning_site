from django.shortcuts import render, get_object_or_404
from .models import Lesson
from collections import defaultdict
from django.http import HttpResponseForbidden

ACCESS_KEY = "abc123"

def lesson_list(request):
    key = request.GET.get("access", "")
    if key != ACCESS_KEY:
        return HttpResponseForbidden("このページは限定公開です。")

    lessons = Lesson.objects.all().order_by('chapter', 'number')
    grouped_lessons = defaultdict(list)
    for lesson in lessons:
        chapter_cleaned = (lesson.chapter or "").strip().replace("：", ":")
        grouped_lessons[chapter_cleaned].append(lesson)

    # ✅ 各章に画像を対応させる辞書
    chapter_images = {
        "第1章:コンプライアンスと法令": "images/ch1.jpg",
        "第2章:プレミアムウォーターの商品知識": "images/ch2.jpg",
        "第3章:トークスクリプトをマスターしよう": "images/ch3.jpg",
        "第4章:39cloudを操作する": "images/ch4.jpg",
        "第5章:実践ロープレとログ学習": "images/ch5.jpg",
}

    return render(request, 'lessons/lesson_list.html', {
        'lessons': lessons,
        'g_lessons': dict(grouped_lessons),
        'chapter_images': chapter_images,  
        'access_key': key,
    })

def lesson_detail(request, pk):
    key = request.GET.get("access", "")
    if key != ACCESS_KEY:
        return HttpResponseForbidden("このページは限定公開です。")

    lesson = get_object_or_404(Lesson, pk=pk)
    return render(request, 'lessons/lesson_detail.html', {
        'lesson': lesson,
        'access_key': key,
    })
