from itertools import permutations


def sort_lst(lst):
    sorted_lst = sorted(list(enumerate(lst)), key=lambda x: x[1], reverse=True)
    num_dict = {}

    for sorted_tuple in sorted_lst:
        if sorted_tuple[1] in num_dict:
            num_dict[sorted_tuple[1]] += 1
        else:
            num_dict[sorted_tuple[1]] = 1

    cnt_values = []
    for value in num_dict.values():
        if value != 1:
            cnt_values.append(value)

    print(sorted_lst)
    perms_length_2 = list(permutations(sorted_lst))
    print(len(perms_length_2))
    print(perms_length_2)
    print(num_dict)
    print(cnt_values)


data = [1, 2, 3, 4, 4]
sort_lst(data)




# def is_adjacent(a, b):
#     if abs(a - b) <= 1:
#         return False
#     return True


# def sort_lst(lst):
#     sorted_lst = sorted(list(enumerate(lst)), key=lambda x: x[1], reverse=True)
#     return sorted_lst


# def processed_lst(lst):
#     subset = [lst[0]]
#     for i in range(len(lst)):
#         if all(is_adjacent(num[0], lst[i][0]) for num in subset):
#             subset.append(lst[i])
#     return subset


# def remaining_lst(ori_lst, dis_lst):
#     for num in dis_lst:
#         ori_lst[num[0]] = 0
#     return ori_lst


# def calculate_cost(rem_nums):
#     cost = 0
#     while sum(rem_nums) != 0:
#         sorted_nums = sort_lst(rem_nums)
#         processed_nums = processed_lst(sorted_nums)
#         rem_nums = remaining_lst(nums, processed_nums)
#         cost += max(item[1] for item in processed_nums)
#     return cost


# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     nums = list(map(int, input().split()))

#     remaining_nums = nums[:]
#     cost_lst = [calculate_cost(remaining_nums)]

#     print(f'#{tc} {min(cost_lst)}')

