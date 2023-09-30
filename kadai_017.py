#名前(name)と年齢(age)の属性を持つHumanクラスを作成してください。
#Humanクラスには、以下の条件で標準出力(print)するcheck_adultメソッドを追加してください。
#ageが20以上の場合に大人であること
#そうでない場合に大人でないこと
#Humanクラスのインスタンスを複数生成してリストに追加し、リストの要素数分だけcheck_adultメソッドを呼び出してください。

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    # メソッドを定義する
    def set_name(self, name):
        self.name = name
    def set_age(self,age):
        self.age = age
        
    def check_adult(self):
        if self.age >= 20:
            print("大人です")
        else:
            print("大人ではありません")

# インスタンス化する
human_names = ["侍太郎", "侍一郎", "侍二郎", "侍三郎", "侍四郎"]
human_ages  = [36, 15, 29, 11, 12]

for i in range(0,5):
    human = Human(human_names[i],human_ages[i])
    human.check_adult()
