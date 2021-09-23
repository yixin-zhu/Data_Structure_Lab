#include "Matrix.cpp"

void ReadinRandomArray(vector<int> &a, vector<int> &b, vector<int> &c)
{
    int temp;
    while (cin >> temp)
    {
        a.push_back(temp);
        b.push_back(temp);
        c.push_back(temp);
    }
}

void testOrdinaryMulti(const Matrix &x, Matrix &y)
{
    LARGE_INTEGER begin, end, fre;
    ll dur;
    QueryPerformanceFrequency(&fre);
    QueryPerformanceCounter(&begin);
    Matrix temp = x * y;
    QueryPerformanceCounter(&end);
    dur = (end.QuadPart - begin.QuadPart) * 1000000000 / fre.QuadPart;
    cout << "Time use of ordinary multi is: ";
    cout << dur << " nanoseconds." << endl;
};

void testStressenMulti(const Matrix &x, Matrix &y)
{
    LARGE_INTEGER begin, end, fre;
    ll dur;
    QueryPerformanceFrequency(&fre);
    QueryPerformanceCounter(&begin);
    Matrix temp = stressenMulti(x,y);
    QueryPerformanceCounter(&end);
    dur = (end.QuadPart - begin.QuadPart) * 1000000000 / fre.QuadPart;
    cout << "Time use of stressen multi is: ";
    cout << dur << " nanoseconds." << endl;
};

int main()
{
    Matrix* x = new Matrix(2,2);
    x->n = x->m = 2;
    x->con[0][0]=5;
    x->con[0][1]=6;
    x->con[1][0]=7;
    x->con[1][1]=3;
    x->printMatrix();
    Matrix* y = new Matrix(2,2);
    y->con[0][0]=4;
    y->con[0][1]=6;
    y->con[1][0]=8;
    y->con[1][1]=3;
    /*Matrix z = (*x) * (*y);
    z.printMatrix()*/
    Matrix* r ;
    r = &(stressenMulti((*x),(*y)));
    cout<<r->con[0][0];
    //r.printMatrix();
    return 0;
}
