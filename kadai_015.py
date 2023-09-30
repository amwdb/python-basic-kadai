#名前(name)と年齢(age)の属性を持つHumanクラスを作成してください。
#nameとageを標準出力(print)するメソッド(printinfo)を追加してください。

#Humanクラスのインスタンスは、変数に代入してプログラム内で使用してください。

class Human:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    # メソッドを定義する
    def set_name(self, name):
        self.name = name
    def set_age(self,age):
        self.age = age
        
    def printinfo(self):
        print(self.name)
        print(self.age)

# インスタンス化する
human = Human("侍太郎", 36)

# メソッドにアクセスして実行する
human.printinfo()
