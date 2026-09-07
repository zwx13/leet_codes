#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

void swap(int* a, int* b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

// xxx: high != 0; low != 0
size_t do_partition(int* partition, int* indexes, size_t low, size_t high)
{
    int pivot = partition[high];
    size_t i = low - 1;
    for(size_t j = low; j <= high - 1; ++j){
        if(partition[j] <= pivot){
            ++i;
            swap(&partition[j], &partition[i]);
            swap(&indexes[j], &indexes[i]);
        }
    }
    swap(&partition[high], &partition[i + 1]);
    swap(&indexes[high], &indexes[i + 1]);
    return i + 1;
}

void qsort2(int* input, int* indexes, size_t low, size_t high)
{
    size_t pivot;
    size_t low_pivot;
    if(low < high){
        pivot = do_partition(input, indexes, low, high);
        if(pivot != 0)
            qsort2(input, indexes, low, pivot - 1);
        qsort2(input, indexes, pivot + 1, high);
    }
}

void qsort1(int* input, int* indexes, size_t size){
    qsort2(input, indexes, 0, size - 1);
}

int* twoSum(int* nums, int numsSize, int target, int* returnSize) {
    int* solution = malloc(2 * sizeof(int));
    int* indexes = malloc(sizeof(int) * numsSize);
    for(size_t i = 0; i < numsSize; ++i){
        indexes[i] = (int)i;
    }
    int sum;
    qsort1(nums, indexes, numsSize);
    size_t index_1, index_2;
    index_1 = 0;
    index_2 = 1;
    while(true){
        sum = nums[index_1] + nums[index_2];
        if(sum == target){
            break;
        }
        if(sum < target && index_2 < numsSize - 1){
            index_2 += 1;
        }else{
            index_1 += 1;
            index_2 = index_1 + 1;
        }
    }
    solution[0] = indexes[index_1];
    solution[1] = indexes[index_2];
    *returnSize = 2;
    return solution;
}

// int main()
// {
//     int retu;
//     int array[] = {-1,-2,-3,-4,-5};
//     printf("size: %ld\n", sizeof(array) / sizeof(array[0]));
//     int* resp = twoSum(array, sizeof(array) / sizeof(array[0]), -8, &retu);
//     printf("%d , %d\n", resp[0], resp[1]);
// }