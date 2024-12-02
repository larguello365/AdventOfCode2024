from collections import Counter

def part1_solution(list1, list2):
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    length = len(sorted_list1)
    
    total = 0
    for i in range(length):
        total += abs(sorted_list1[i] - sorted_list2[i])
    
    return total

def part2_solution(list1, list2):
    list2_freq = Counter(list2)
    total = 0
    
    for num in list1:
        total += num * list2_freq[num]
    
    return total


if __name__ == "__main__":
    
    list1 = []
    list2 = []
    
    with open("day1.txt", "r") as input_file:
         for line in input_file:
             [num1, num2] = [int(num) for num in line.split()]
             list1.append(num1)
             list2.append(num2)
    
    part1_answer = part1_solution(list1, list2)
    part2_answer = part2_solution(list1, list2)
    
    print(f"Part 1 answer: {part1_answer}")
    print(f"Part 2 answer: {part2_answer}")
    
    