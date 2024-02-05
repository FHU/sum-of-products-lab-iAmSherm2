#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
def sum_of_products(list1, list2):
    if len(list1) != len(list2):
        raise ValueError
    result = sum(x * y for x, y in zip(list1, list2))
    return result


if __name__ == '__main__':
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    output = sum_of_products(list1, list2)
    print(output)