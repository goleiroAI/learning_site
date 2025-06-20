from lessons.models import Lesson

Lesson.objects.all().delete()

lessons = [
Lesson(chapter="第1章", number="1-1", title="テレマーケティングと特定商取引法"),
    Lesson(chapter="第1章", number="1-2", title="個人情報保護の基本"),
    Lesson(chapter="第1章", number="1-3", title="コンプライアンス違反の実例"),
    Lesson(chapter="第1章", number="1-4", title="架電するときの注意"),
    Lesson(chapter="第1章", number="1-5", title="クレームを防ぐには"),

    Lesson(chapter="第2章", number="2-1", title="プレミアムウォーターとは"),
    Lesson(chapter="第2章", number="2-2", title="ボトルの仕組み"),
    Lesson(chapter="第2章", number="2-3", title="サーバーの種類と特徴"),
    Lesson(chapter="第2章", number="2-4", title="サービス概要"),
    Lesson(chapter="第2章", number="2-5", title="注意事項"),

    Lesson(chapter="第3章", number="3-1", title="スクリプトを読んでみよう"),
    Lesson(chapter="第3章", number="3-2", title="よくある質問"),

    Lesson(chapter="第4章", number="4-1", title="システムの基本操作"),
    Lesson(chapter="第4章", number="4-2", title="お申し込み登録の手順"),
    Lesson(chapter="第4章", number="4-3", title="エラー時の対応"),

    Lesson(chapter="第5章", number="5-1", title="システムでロープレをしよう"),
    Lesson(chapter="第5章", number="5-2", title="自分のログを聞いてみよう"),
    Lesson(chapter="第5章", number="5-3", title="実際の受注ログを聞いてみよう"),
    Lesson(chapter="第5章", number="5-4", title="過去の事例を参考にしよう"),
]

Lesson.objects.bulk_create(lessons)
