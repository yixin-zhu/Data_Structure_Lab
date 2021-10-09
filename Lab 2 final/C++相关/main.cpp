#include "Matrix.cpp"

void readInData(Matrix &x, Matrix &y, int n)
{
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            cin>>x.con[i][j];
    for(int i=0;i<n;i++)
        for(int j=0;j<n;j++)
            cin>>y.con[i][j];
}

void testOrdinaryMulti(const Matrix &x, Matrix &y)
{
    clock_t begin, end;
    double cost;
    begin = clock();
    printf("Ordinary begin，begin = %ld ", begin);
    Matrix temp = x*y;
    temp.printMatrix();
    end = clock();
    printf("Ordinary end，end = %ld\n", end);
    cost = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Time cost：%lf\n", cost );
    cout << endl;
};

void testStrassenMulti(const Matrix &x, Matrix &y)
{
    clock_t begin, end;
    double cost;
    begin = clock();
    printf("Strassen begin，begin = %ld ", begin);
    Matrix temp = strassenMulti(x,y);
    temp.printMatrix();
    end = clock();
    printf("Strassen end，end = %ld\n", end);
    cost = (double)(end - begin) / CLOCKS_PER_SEC;
    printf("Time cost：%lf\n", cost );
    cout << endl;
};

int main()
{   
    freopen("data.in", "r", stdin);
    freopen("data.out", "w", stdout);
    int n;
    cin >> n;
    Matrix x = Matrix(n,n);
    Matrix y = Matrix(n,n);
    readInData(x,y,n);
    x.printMatrix();
    y.printMatrix();
    testOrdinaryMulti(x,y);
    testStrassenMulti(x,y);
    return 0;
}
