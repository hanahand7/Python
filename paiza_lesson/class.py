# coding: utf-8
# クラスを作成する
# ポイント1:頭文字は大文字。
class Example():

# ポイント2:def関数でメソッドを作成。引数はselfが必須。 
# ポイント3:コンストラクタは、インスタンスを生成したときに一度だけ呼び出されるメソッドです。
#          基本的には対象のクラスのインスタンスを初期化するために利用します。
#          コンストラクタを定義するには、「init」という特殊な名前でメソッドを定義する必要があります
    def __init__(self, a,b,c):
        self.num1 = a
        self.num2 = b
        self.num3 = c
 
    def print_tot(self):
        tot = self.num1+self.num2+self.num3
        print(tot)

# ポイント3:変数myinstanceにインスタンスを作成
myinstance = Example(1,2,3)
# ポイント4:classで定義されたメソッドを呼び出しすることができる
myinstance.print_tot()