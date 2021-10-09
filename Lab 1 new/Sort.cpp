#include <bits/stdc++.h>
using namespace std;
#include <windows.h>
typedef long long ll;
const int K = 60;

template <class T>
class Sort
{
public:
    void testInsertionSort(vector<T> &a);
    void testMergeSort(vector<T> &a);
    void testCombineSort(vector<T> &a);
    double timeDiff();

private:
    void insertionSort(vector<T> &a);
    void insertionSortPartly(vector<T> &a, int begin, int end);
    void mergeSort(vector<T> &a);
    void mergeSortPartly(vector<T> &a, T *temp, int begin, int end);
    void mergeTwoArrays(vector<T> &a, T *temp, int begin, int end);
    void combineSortPartly(vector<T> &a, T *temp, int begin, int end);
    void combineSort(vector<T> &a);
};

template <class T>
void Sort<T>::insertionSortPartly(vector<T> &a, int begin, int end)
{
    for (int j = begin + 1; j <= end; j++)
    {
        T temp = a[j];
        int i = j;
        while (i > begin && a[i - 1] >= temp)
        {
            a[i] = a[i - 1];
            i--;
        }
        a[i] = temp;
    }
}

template <class T>
void Sort<T>::insertionSort(vector<T> &a)
{
    if (a.empty())
        return;
    insertionSortPartly(a, 0, a.size() - 1);
}

template <class T>
void Sort<T>::mergeTwoArrays(vector<T> &a, T *temp, int begin, int end)
{
    int mid = ((end - begin) / 2) + begin;
    int begin1 = begin;
    int begin2 = mid + 1;
    int t = begin;
    while (begin1 <= mid && begin2 <= end)
    {
        if (a[begin1] < a[begin2])
            temp[t++] = a[begin1++];
        else
            temp[t++] = a[begin2++];
    }
    while (begin1 <= mid)
        temp[t++] = a[begin1++];
    while (begin2 <= end)
        temp[t++] = a[begin2++];
    for (int t = begin; t <= end; t++)
        a[t] = temp[t];
}

template <class T>
void Sort<T>::mergeSortPartly(vector<T> &a, T *temp, int begin, int end)
{
    int mid = ((end - begin) / 2) + begin;
    if (begin >= end)
        return;
    mergeSortPartly(a, temp, begin, mid);
    mergeSortPartly(a, temp, mid + 1, end);
    mergeTwoArrays(a, temp, begin, end);
}

template <class T>
void Sort<T>::mergeSort(vector<T> &a)
{
    int begin = 0;
    int end = a.size() - 1;
    if (begin >= end)
        return;
    int len = end - begin + 1;
    T *temp = new T[len];
    mergeSortPartly(a, temp, begin, end);
}

template <class T>
void Sort<T>::combineSortPartly(vector<T> &a, T *temp, int begin, int end)
{
    if (end - begin < K)
    {
        insertionSortPartly(a, begin, end);
    }
    else
    {
        int mid = ((end - begin) / 2) + begin;
        combineSortPartly(a, temp, begin, mid);
        combineSortPartly(a, temp, mid + 1, end);
        mergeTwoArrays(a, temp, begin, end);
    }
}

template <class T>
void Sort<T>::combineSort(vector<T> &a)
{
    int begin = 0;
    int end = a.size() - 1;
    if (begin >= end)
        return;
    int len = end - begin + 1;
    T *temp = new T[len];
    combineSortPartly(a, temp, begin, end);
}

template <class T>
void Sort<T>::testMergeSort(vector<T> &a)
{
    LARGE_INTEGER begin, end, fre;
    ll dur;
    QueryPerformanceFrequency(&fre);
    QueryPerformanceCounter(&begin);
    mergeSort(a);
    QueryPerformanceCounter(&end);
    dur = (end.QuadPart - begin.QuadPart) * 1000000000 / fre.QuadPart;
    cout << "Time use of Merge Sort is: ";
    cout << dur << " nanoseconds." << endl;
}

template <class T>
void Sort<T>::testInsertionSort(vector<T> &a)
{
    LARGE_INTEGER begin, end, fre;
    ll dur;
    QueryPerformanceFrequency(&fre);
    QueryPerformanceCounter(&begin);
    insertionSort(a);
    QueryPerformanceCounter(&end);
    dur = (end.QuadPart - begin.QuadPart) * 1000000000 / fre.QuadPart;
    cout << "Time use of Insertion Sort is: ";
    cout << dur << " nanoseconds." << endl;
}

template <class T>
void Sort<T>::testCombineSort(vector<T> &a)
{
    LARGE_INTEGER begin, end, fre;
    ll dur;
    QueryPerformanceFrequency(&fre);
    QueryPerformanceCounter(&begin);
    combineSort(a);
    QueryPerformanceCounter(&end);
    dur = (end.QuadPart - begin.QuadPart) * 1000000000 / fre.QuadPart;
    cout << "Time use of Combine Sort is: ";
    cout << dur << " nanoseconds." << endl;
}