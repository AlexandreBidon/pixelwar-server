test = ["#ffffff"] * 10
test2 = []
for i in range(10):
    test2.append(test.copy())

test2[1][1] = "test"

print(test2)
