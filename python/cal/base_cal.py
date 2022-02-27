#递归
def func(n):
    if n < 1:
        return 1
    else:
        return n * func(n - 1)

#快速排序
def quick_sort(lst):
    # 判断列表lst的长度大于2
    # 如果列表lst的长度小于2，那么无须排序，只需返回排序结果
    if len(lst) < 2:
        return lst
    # 执行快速排序
    else:
        # 获取第一个列表元素
        pivot = lst[0]
        # 遍历列表lst，将小于第一个列表元素的元素放在列表small_lst中
        small_lst = [I for I in lst[1:] if I < pivot]
        # 遍历列表lst，将大于或等于第一个列表元素的元素放在列表large_lst中
        large_lst = [J for J in lst[1:] if J >= pivot]
        # 递归函数quick_sort，传入列表small_lst
        qs = quick_sort(small_lst)
        # 递归函数quick_sort，传入列表large_lst
        ql = quick_sort(large_lst)
        # 每次递归都返回一个列表，已经排好序的列表
        return qs + [pivot] + ql

#冒泡排序
def sortData(list):
    # 根据列表的长度，确定需要循环的次数 list长度+1，list是从0开始的
    for j in range(len(list) + 1):
        # 两两比较大小，挑出最大或者最小的值
        for i in range(len(list) - (j + 1)):
            if list[i] < list[i + 1]:
                tmp = list[i + 1]
                list[i + 1] = list[i]
                list[i] = tmp
    return list

#选择排序
def select_sort(list):
    #需要循环的次数
    for i in range(len(list)): #第一轮选出最大或最下的值
        index= i #暂定最大或最小值的
        for j in range(i+1,len(list)):
            #顺序，从小到大
            if list[index]>list[j]:#第二趟排序让min去和无序数列的数作比较找出真正最小值
                #替换最小线的index，最后用于交换位置
                index = j
                #list[i], list[index] = list[index], list[i]
        tmp = list[i]
        list[i] = list[index]
        list[index] = tmp
    return list


if __name__ == '__main__':
    list = [49, 38, 65, 88, 12, 75]
    #print(quick_sort(list))
    #print(sortData(list))
    print(select_sort(list))

