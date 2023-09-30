#名前(name)と年齢(age)の属性を持つHumanクラスを作成してください。
#Humanクラスには、以下の条件で標準出力(print)するcheck_adultメソッドを追加してください。
#ageが20以上の場合に大人であること
#そうでない場合に大人でないこと
#Humanクラスのインスタンスを複数生成してリストに追加し、リストの要素数分だけcheck_adultメソッドを呼び出してください。

class Human:
    # 初期化とメソッドを定義する
    def __init__(self,name,age):
        self._name = name
        self._age = age

    def check_adult(self):
        if self._age >= 20:
            print("大人です")
        else:
            print("大人ではありません")

# インスタンス化する
humans_ages = []
humans_ages.append(Human("太郎",10))
humans_ages.append(Human("次郎",20))
humans_ages.append(Human("三郎",30))
for human in humans_ages:
    human.check_adult()
