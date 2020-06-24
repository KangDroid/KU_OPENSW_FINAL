def retPie(iteration_ctr):
    final_value = 0
    for i in range(1,iteration_ctr+1):
        final_value = final_value + ((pow(-1, i+1) / (2 * i - 1)))
    return 4 * final_value

print("i \t m(i)")
for i in range(1, 902, 100):
    print("%d \t %.4f"%(i, retPie(i)))