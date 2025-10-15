#初期化
from decimal import Decimal
mode = Decimal('0')
bpm = Decimal('0')
length = Decimal('0')



#モード選択、範囲以外のものはもう一回
mode = int(input("モードを選択してください(1:秒数指定, 2:48分指定)："))
while 2 < mode or 1 > mode:
    mode = int(input("もう一度モードを選択してください(1:秒数指定, 2:48分指定)："))



#もし秒数指定モードの場合
if mode == 1:
    length = Decimal(input("秒数を入力してください:"))
#48分指定モードの場合
else:
    bpm = Decimal(input("bpmを入力してください："))
    length = Decimal(input("48分表記で何拍か入力してください:"))
    #連打秒数計算、出力
    length = length - Decimal('1')
    length = length * Decimal('5') / bpm
    print("\nー連打秒数ーーーーーーーーーーーーーーーーーーーー\n連打の秒数 %.3f 秒\nーーーーーーーーーーーーーーーーーーーーーーーーー\n"%length)
#連打秒数の辻褄を合わせるために計算上0.001秒(1ミリ秒)足す(最新の研究に基づく)
length = length + Decimal('0.001')



#120fps, 60fpsのフレーム数と　1個目の連打可能打数を計算
onetwozeroFPS = length * Decimal('120')
sixzeroFPS = length * Decimal('60')
frRen = onetwozeroFPS // Decimal('2') + Decimal('1')
#60fpsの小数部分を計算
x = int(sixzeroFPS)
y = sixzeroFPS - x



#もし60fpsの小数部分が0.5以上の場合連打可能秒数は1つに定まるのでそのまま出力
if y >= Decimal('0.5'):
    print("\nー結果ーーーーーーーーーーーーーーーーーーーーーー\nseconds: %.3f  s\n 120fps: %.3f f\n  60fps: %.3f f\n連打可能打数: %d 打\nーーーーーーーーーーーーーーーーーーーーーーーーー\n"%(length, onetwozeroFPS, sixzeroFPS, frRen))
#もし60fpsの小数部分が0.5未満の場合連打可能秒数は2つになるので、1個目の連打可能打数を計算し出力
else:
    scRen = onetwozeroFPS // 2
    print("\nー結果ーーーーーーーーーーーーーーーーーーーーーー\nseconds: %.3f  s\n120fps: %.3f f\n 60fps: %.3f f\n連打可能打数: %d or %d 打\nーーーーーーーーーーーーーーーーーーーーーーーーー\n"%(length, onetwozeroFPS, sixzeroFPS, frRen, scRen))

end = input("何かを入力して終了")