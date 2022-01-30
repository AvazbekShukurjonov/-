cost=int(input('chek\n'))
money=int(input('berilgan pul\n'))

if money >= cost and money%100==0 and cost%100==0:
    thousend=0
    five_houdreds = 0
    hundreds= 0

    qaytim=money-cost
    thousend = qaytim // 1000


    print('qaytim teng',qaytim)