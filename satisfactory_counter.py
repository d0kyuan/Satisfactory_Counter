import math


class 採礦機MK1:
    output = 60


class 採礦機MK2:
    output = 120


class 鑄造機_鐵:
    output = 30


class 鑄造機_銅:
    output = 30


class 鐵礦:
    is_Synthesizable = False
    output = 30


class 鐵錠:
    is_Synthesizable = True
    output = 30
    input = {
        鐵礦: 30
    }


class 鐵棒:
    is_Synthesizable = True
    output = 15
    input = {
        鐵錠: 15
    }


class 鐵板:
    is_Synthesizable = True
    output = 15
    input = {
        鐵錠: 15
    }


class 螺絲:
    is_Synthesizable = True
    output = 90
    input = {
        鐵棒: 15
    }


class 強化鐵板:
    is_Synthesizable = True
    output = 5
    input = {
        鐵板: 20,
        螺絲: 120
    }


class 模組框架:
    is_Synthesizable = True
    output = 4
    input = {
        強化鐵板: 12,
        鐵棒: 24
    }


class 石頭:
    is_Synthesizable = False
    output = 30


class 混泥土:
    is_Synthesizable = True
    output = 15
    input = {
        石頭: 45
    }


class 碳:
    is_Synthesizable = False
    output = 30


class 鋼錠:
    is_Synthesizable = True
    output = 30
    input = {
        碳: 45,
        鐵礦: 45
    }


class SteelBeam:
    is_Synthesizable = True
    output = 10
    input = {
        鋼錠: 30
    }


class Encased_Industrial_Beam:
    is_Synthesizable = True
    output = 4
    input = {
        混泥土: 20,
        SteelBeam: 16
    }


class 鋼管:
    is_Synthesizable = True
    output = 15
    input = {
        鋼錠: 15
    }


class 重型模組框架:
    is_Synthesizable = True
    output = 15
    input = {
        螺絲: 180,
        模組框架: 10,
        Encased_Industrial_Beam: 10,
        鋼管: 30
    }


class 銅錠:
    is_Synthesizable = False
    output = 30


class 銅線:
    is_Synthesizable = True
    output = 45
    input = {
        銅錠: 15
    }


class 定子:
    is_Synthesizable = True
    output = 6
    input = {
        鋼管: 18,
        銅線: 60
    }


class 轉子:
    is_Synthesizable = True
    output = 6
    input = {
        鐵棒: 18,
        螺絲: 132
    }


class 馬達:
    is_Synthesizable = True
    output = 5
    input = {
        轉子: 10,
        定子: 10
    }


need_obj = {}
step = {

}


def counter():
    choose = eval(input('選擇計算的物品1.強化鐵板 2.模組框架 3.重型模組框架 4.馬達'))
    number = eval(input('您需要的產量 /分鐘 '))
    if choose == 1:
        # print(強化鐵板.input)
        get_input_need(強化鐵板, number)
    elif choose == 2:
        get_input_need(模組框架, number)
    elif choose == 3:
        get_input_need(重型模組框架, number)
    elif choose == 4:
        get_input_need(馬達, number)
    print("您需要的基本資源:")
    for o, n in need_obj.items():
        print("{}:{}個/分鐘".format(o, n['counter']))
    print()
    print("===========================")
    print()
    print("您需要的所有資源:")
    for o, n in step.items():
        print("{}:{}個/分鐘 {}台".format(o,
                                     n['counter'], int(math.ceil(n['counter'] / n['o'].output))))


def get_input_need(o, n):
    dd = 1
    if o.output < n:
        dd = int(math.ceil(n / o.output))
    for obj, need in o.input.items():
        if obj.__name__ in step:
            step[obj.__name__]['counter'] = step[obj.__name__]['counter'] + need * dd
            step[obj.__name__]['o'] = obj
        else:
            step.update({obj.__name__: {"counter": need * dd, "o": obj}})
        if obj.is_Synthesizable:
            get_input_need(obj, need * dd)

        else:
            if obj.__name__ in need_obj:
                need_obj[obj.__name__]['counter'] = need_obj[obj.__name__]['counter'] + need * dd
            else:
                need_obj.update({obj.__name__: {"counter": need * dd}})


counter()
