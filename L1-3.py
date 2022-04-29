#3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.
def equation(*arq):
  k = (arq[3]-arq[1])/(arq[2]-arq[0])
  b= -k*arq[0]+arq[1]
  if b<0:
    return f'y={k}x{b}'
  elif b>0:
    return f'y={k}x+{b}'
  elif b == 0:
    return f'y={k}x'
  else:
    return f'введены некорректные данные координат'

if __name__ == '__main__':
  print(equation(
    int(input('x1=')),
    int(input('y1=')),
    int(input('x2=')),
    int(input('y2='))
  ))