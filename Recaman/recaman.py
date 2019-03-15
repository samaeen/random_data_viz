import turtle

def recaman(n):
    arr = [0] * n
    arr[0] = 0
    for i in range(1, n):   
        curr = arr[i-1] - i
        for j in range(0, i):
            if ((arr[j] == curr) or curr < 0):
                curr = arr[i-1] + i
             
        arr[i] = curr
    print(arr)
    return arr
def draw(arr):
	pen=turtle.Turtle()
	pen.getscreen().bgcolor("#191919")
	pen.color("#a85715")

	for x in range(len(arr)):
		pen.forward(x*5)
		pen.left(90)
		pen.forward(arr[x]*10)
		pen.backward(arr[x]*10)
		pen.circle(arr[x]*10, 180)
		pen.right(90)

	
	turtle.done()


draw(recaman(20))