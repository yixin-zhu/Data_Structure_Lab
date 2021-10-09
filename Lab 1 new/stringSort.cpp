#include "Sort.cpp"

template <class T>
void ReadinRandomArray(vector<T> &a,vector<T> &b, vector<T> &c)
{
    T temp;
    while(cin >> temp)
    {  
        a.push_back(temp);
        b.push_back(temp);
        c.push_back(temp);
    }
}

template <class T>
void printArray(vector<T> &a)
{
    if(a.empty()) return ;
    for(int i=0;i<a.size();i++){
        cout<<a[i]<<" ";
    }
}

int main()
{
    Sort<string> mySort;
    vector<string> a,b,c;
    ReadinRandomArray(a,b,c);
    mySort.testInsertionSort(a);
    mySort.testMergeSort(b);
    mySort.testCombineSort(c);
    printArray(a);
    cout<<endl;
    printArray(b);
    cout<<endl;
    printArray(c);
    cout<<endl;
    return 0;
}