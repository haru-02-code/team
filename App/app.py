from flask import Flask, render_template #
from dotenv import load_dotenv #.envファイルを読み込むため
from supabase import create_client #Supabaseを接続するため
import os #環境変数を扱うため .envの中身をos.getenv()で呼び出すため

app = Flask(__name__) # Flaskアプリケーションのインスタンスを作成

load_dotenv()# .envファイルを読み込む

supabase = create_client(#Supabaseに接続するための設定を作る keyとurlを.envから呼び出す
    supabase_url=os.getenv("SUPABASE_URL"),
    supabase_key=os.getenv("SUPABASE_KEY")
)
@app.route("/") #ブラウザで/にアクセスしたときにindex関数が呼び出されるようにする
def index():
    response = supabase.table("main-to-do").select("*").execute() #Supabaseのtodosテーブルから全てのデータを取得するクエリを実行
    todos = response.data #取得したデータをtodosに代入

    events = []
    for todo in todos: #todosの中身を一つずつtodoに入れてループする
        events.append({
            "title": todo["todonaiyou"], #todoのtodonaiyouカラムをタイトルにする
            "start": todo["start_at"], #todoのstart_atカラムを開始日時にする
            "end": todo["end_at"], #todoのend_atカラムを終了日時にする
            "color": todo["color"], #todoのcolorカラムを表示色にする
            "textColor": "white", #文字色は白にする
            "extendedProps": {
                "person": todo["tantou"] #todoのtantouカラムを担当者名にする
            }
        })

    print(events)

    return render_template("calendar.html", events=events)# calendar.htmlをレンダリング(表示,生成）して、eventsのデータを渡す


if __name__ == "__main__":#このファイルが直接実行されたときに以下のコードを実行する
    app.run(debug=True)#flaskを起動




#カラム一覧：

#カラム名	    型              入れるもの

#todonaiyou	   text	           ToDoのタイトル
#todosetumei   text	           詳細説明
#start_at	   timestamptz	   開始日時
#end_at	       timestamptz	   終了日時
#tantou	       text	           担当者名
#color	       text	           表示色
#status	       text	           状態

