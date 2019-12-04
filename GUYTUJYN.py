class Triangle:
    # w , h1 , h2 - длины сторон
    def __init__(self, w=2, h1=1, h2=2):
        self.width = w
        self.height1 = h1
        self.height2 = h2

    def square(self):
        return self.width + self.height1 + self.height2
# задание а)
x=int(input("Введите длинну 1 стороны"))
y=int(input("Введите длинну 2 стороны"))
z=int(input("Введите длинну 3 стороны"))
rec1 = Triangle(x, y, z) #произвольный
rec2 = Triangle() # стандарт
rec3 = Triangle(3,3,3) #равнстороний
rec4 = Triangle(h1=4,h2=4)# равнобедренный
print(rec1.square())
print(rec2.square())
print(rec3.square())
print(rec4.square())
#Задание б)
naq = [rec2.square(), rec3.square(), rec4.square()]
t = max(naq)
print("Самый самый большой треуголбник)- "+ str(t))
