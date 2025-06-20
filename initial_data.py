from lessons.models import Lesson

Lesson.objects.all().delete()

lessons = [
    Lesson(chapter="第1章：コンプライアンスと法令", number="1-1", title="テレマーケティングと特定商取引法"),
    Lesson(chapter="第1章：コンプライアンスと法令", number="1-2", title="個人情報保護の基本"),
    Lesson(chapter="第1章：コンプライアンスと法令", number="1-3", title="コンプライアンス違反の実例"),
    Lesson(chapter="第1章：コンプライアンスと法令", number="1-4", title="架電する上での注意"),
    Lesson(chapter="第1章：コンプライアンスと法令", number="1-5", title="クレームを防ぐためには"),

    Lesson(chapter="第2章：プレミアムウォーターの商品知識", number="2-1", title="プレミアムウォーターとは"),
    Lesson(chapter="第2章：プレミアムウォーターの商品知識", number="2-2", title="ボトルの仕組み"),
    Lesson(chapter="第2章：プレミアムウォーターの商品知識", number="2-3", title="サーバーの種類と特徴"),
    Lesson(chapter="第2章：プレミアムウォーターの商品知識", number="2-4", title="サービス概要"),
    Lesson(chapter="第2章：プレミアムウォーターの商品知識", number="2-5", title="注意事項"),

    Lesson(chapter="第3章：トークスクリプトをマスターしよう", number="3-1", title="スクリプトを読んでみよう"),
    Lesson(chapter="第3章：トークスクリプトをマスターしよう", number="3-2", title="ペアを作ってお互いに話してみよう"),
    Lesson(chapter="第3章：トークスクリプトをマスターしよう", number="3-3", title="お客さんの質問に答えてみよう"),
    Lesson(chapter="第3章：トークスクリプトをマスターしよう", number="3-4", title="OUT返しを見てみよう"),
    Lesson(chapter="第3章：トークスクリプトをマスターしよう", number="3-5", title="スクリプトとアウト返しをスムーズにしよう"),

    Lesson(chapter="第4章：39cloudを操作する", number="4-1", title="39cloudの使い方"),
    Lesson(chapter="第4章：39cloudを操作する", number="4-2", title="架電の発信の仕方とリストについて"),
    Lesson(chapter="第4章：39cloudを操作する", number="4-3", title="フラグについて"),
    Lesson(chapter="第4章：39cloudを操作する", number="4-4", title="架電の記録の残し方"),
    Lesson(chapter="第4章：39cloudを操作する", number="4-5", title="よくあるミスと防止策"),

    Lesson(chapter="第5章：実践ロープレとログ学習", number="5-1", title="システムでロープレをしてみよう"),
    Lesson(chapter="第5章：実践ロープレとログ学習", number="5-2", title="自分のログを聞いてみよう"),
    Lesson(chapter="第5章：実践ロープレとログ学習", number="5-3", title="受注のログを聞いてみよう"),
    Lesson(chapter="第5章：実践ロープレとログ学習", number="5-4", title="その他の事例のログを聞いてみよう"),
    Lesson(chapter="第5章：実践ロープレとログ学習", number="5-5", title="最終確認"),
]

Lesson.objects.bulk_create(lessons)
