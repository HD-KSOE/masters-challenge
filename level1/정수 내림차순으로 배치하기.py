def solution(n):
    answer = 0
    
    number_str = str(n)
    number_array = []

    for char in number_str:
        number_array.append(int(char))

    number_array.sort(reverse=True)
    
    for i in range(len(number_array)):
        number_array[i] = str(number_array[i])
    
    answer = ''.join(number_array)
    answer = int(answer)

    return answer
