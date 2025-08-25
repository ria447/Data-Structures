def sift_down(array, i):
    min_index = i
    left = 2 * i + 1
    right = 2 * i + 2
    size = len(array)
    
    if left < size and array[left] < array[min_index]:
        min_index = left

    if right < size and array[right] < array[min_index]:
        min_index = right 

    if i != min_index:
        array[i], array[min_index] =  array[min_index], array[i]
        sift_down(array, min_index)


def sift_up(array,i):
    while i > 0:
        parent = (i-1) // 2
        
        if array[parent][0] > array[i][0] or ( array[parent][0] == array[i][0] and array[parent][1] > array[i][1] ):
            array[parent], array[i] = array[i], array[parent]
            i = parent
        else:
            break

def insert(array, item):
    array.append(item)
    sift_up(array, len(array)-1)

    

def extract_min(array):
    min_item = array[0]
    last_item = array.pop()

    if array:
        array[0] = last_item 
        sift_down(array, 0)

    return min_item

def build_heap(array):
    size = len(array)

    for i in range((size // 2) - 1, -1, -1):
        sift_down(array, i)


def run_jobs(n, jobs_time):
    heap = []
    for i in range(n):
        heap.append((0, i))
    build_heap(heap)
    
    results = []
    
    for ith_job_time in jobs_time:
        start_time, thread_index = extract_min(heap)

        results.append((thread_index, start_time))

        new_start_time = start_time + ith_job_time
        
        insert(heap, (new_start_time, thread_index))

    return results


if __name__ == '__main__':
    n, m = input().split()
    n = int(n)
    m = int(m)
    array = input().split()
    jobs_time = map(int, array)
    output = run_jobs(n, jobs_time )
    for i in output:
        print(i[0], ' ', i[1])