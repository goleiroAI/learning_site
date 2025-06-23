from lessons.models import Lesson

Lesson.objects.bulk_create([
    Lesson(chapter="第1章：コンプライアンスと法令", number="1-1", title="テレマーケティングと特定商取引法", content="仮の本文"),
    Lesson(chapter="第1章：コンプライアンスと法令", number="1-2", title="個人情報保護の基本", content="仮の本文"),
    Lesson(chapter="第1章：コンプライアンスと法令", number="1-3", title="コンプライアンス違反の実例", content="仮の本文"),
    Lesson(chapter="第1章：コンプライアンスと法令", number="1-4", title="架電する上での注意", content="仮の本文"),
    Lesson(chapter="第1章：コンプライアンスと法令", number="1-5", title="クレームを防ぐためには", content="仮の本文"),

    Lesson(chapter="第2章：プレミアムウォーターの商品知識", number="2-1", title="プレミアムウォーターとは", content="仮の本文"),
    Lesson(chapter="第2章：プレミアムウォーターの商品知識", number="2-2", title="ボトルの仕組み", content="仮の本文"),
    Lesson(chapter="第2章：プレミアムウォーターの商品知識", number="2-3", title="サーバーの種類と特徴", content="仮の本文"),
    Lesson(chapter="第2章：プレミアムウォーターの商品知識", number="2-4", title="サービス概要", content="仮の本文"),
    Lesson(chapter="第2章：プレミアムウォーターの商品知識", number="2-5", title="注意事項", content="仮の本文"),

    Lesson(chapter="第3章：トークスクリプトをマスターしよう", number="3-1", title="スクリプトを読んでみよう", content="仮の本文"),
    Lesson(chapter="第3章：トークスクリプトをマスターしよう", number="3-2", title="ペアを作ってお互いに話してみよう", content="仮の本文"),
    Lesson(chapter="第3章：トークスクリプトをマスターしよう", number="3-3", title="お客さんの質問に答えてみよう", content="仮の本文"),
    Lesson(chapter="第3章：トークスクリプトをマスターしよう", number="3-4", title="OUT返しを見てみよう", content="仮の本文"),
    Lesson(chapter="第3章：トークスクリプトをマスターしよう", number="3-5", title="スクリプトとアウト返しをスムーズにしよう", content="仮の本文"),

    Lesson(chapter="第4章：39cloudを操作する", number="4-1", title="39cloudの使い方", content="仮の本文"),
    Lesson(chapter="第4章：39cloudを操作する", number="4-2", title="架電の発信の仕方とリストについて", content="仮の本文"),
    Lesson(chapter="第4章：39cloudを操作する", number="4-3", title="フラグについて", content="仮の本文"),
    Lesson(chapter="第4章：39cloudを操作する", number="4-4", title="架電の記録の残し方", content="仮の本文"),
    Lesson(chapter="第4章：39cloudを操作する", number="4-5", title="よくあるミスと防止策", content="仮の本文"),

    Lesson(chapter="第5章：実践ロープレとログ学習", number="5-1", title="システムでロープレをしてみよう", content="仮の本文"),
    Lesson(chapter="第5章：実践ロープレとログ学習", number="5-2", title="自分のログを聞いてみよう", content="仮の本文"),
    Lesson(chapter="第5章：実践ロープレとログ学習", number="5-3", title="受注のログを聞いてみよう", content="仮の本文"),
    Lesson(chapter="第5章：実践ロープレとログ学習", number="5-4", title="その他の事例のログを聞いてみよう", content="仮の本文"),
    Lesson(chapter="第5章：実践ロープレとログ学習", number="5-5", title="最終確認", content="仮の本文"),
])
