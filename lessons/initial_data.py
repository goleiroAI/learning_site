from lessons.models import Lesson

lessons = [
    Lesson(chapter="第1章", number="1-1", title="テレマーケティングと特定商取引法"),
    Lesson(chapter="第1章", number="1-2", title="個人情報保護の基本"),
    Lesson(chapter="第1章", number="1-3", title="コンプライアンス違反の実例"),
    Lesson(chapter="第2章", number="2-1", title="プレミアムウォーターとは"),
    Lesson(chapter="第2章", number="2-2", title="ボトルの仕組み"),
]

Lesson.objects.bulk_create(lessons)
