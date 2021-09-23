#include <bits/stdc++.h>
using namespace std;
#include <windows.h>
typedef long long ll;
const int MAXN = 512;

class Matrix
{
public:
    Matrix(int mm = 0, int nn = 0) : m(mm), n(nn){};
    void printMatrix() const;
    Matrix operator+(const Matrix &ma) const;
    Matrix operator-(const Matrix &ma) const;
    Matrix operator*(const Matrix &ma) const; //ordinary multi
    // Matrix stressenMulti(const Matrix &ma) const;
    void copyFrom(const Matrix &ma, int b1, int e1, int b2, int e2);
    void copyTo(const Matrix &ma, int b1, int e1, int b2, int e2);
    int m, n;
    int con[MAXN][MAXN];
};



void Matrix::copyFrom(const Matrix &ma, int b1, int e1, int b2, int e2)
{
    int mid = e1 - b1;
    n = m = mid;
    for (int i = 0; i < mid; ++i)
    {
        for (int j = 0; j < mid; ++j)
        {
            con[i][j] = ma.con[b1 + i][b2 + j];
        }
    }
}

void Matrix::copyTo(const Matrix &ma, int b1, int e1, int b2, int e2)
{
    int mid = e1 - b1;
    n = m = mid;
    for (int i = 0; i < mid; ++i)
    {
        for (int j = 0; j < mid; ++j)
        {
            con[b1 + i][b2 + j] = ma.con[i][j];
        }
    }
}

void Matrix::printMatrix() const
{   
    cout << "The Matrix is"<<endl;
    for (int i = 0; i < m; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            printf("%5d",con[i][j]);
        }
        cout << endl;
    }
}

Matrix Matrix::operator+(const Matrix &ma) const
{
    Matrix ans;
    if ((n != ma.n) || (m != ma.m))
    {
        cout << "Matrix + invalid!" << endl;
        return ans;
    }
    ans.m = m;
    ans.n = n;
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            ans.con[i][j] = con[i][j] + ma.con[i][j];
    return ans;
}

Matrix Matrix::operator-(const Matrix &ma) const
{
    Matrix ans;
    if ((n != ma.n) || (m != ma.m))
    {
        cout << "Matrix - invalid!" << endl;
        return ans;
    }
    ans.m = m;
    ans.n = n;
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < n; ++j)
            ans.con[i][j] = con[i][j] - ma.con[i][j];
    return ans;
}

Matrix Matrix::operator*(const Matrix &ma) const
{
    Matrix ans;
    if (n != ma.m)
    {
        cout << "Matrix * invalid!" << endl;
        return ans;
    }
    ans.m = m;
    ans.n = ma.n;
    for (int i = 0; i < m; ++i)
        for (int j = 0; j < ma.n; ++j)
            for (int k = 0; k < n; ++k)
                ans.con[i][j] += (con[i][k] * ma.con[k][j]);
    return ans;
}

Matrix stressenMulti(const Matrix &x, const Matrix &y)
{
    Matrix ans;
    if (x.n != y.m)
    {
        cout << "Matrix * invalid!" << endl;
        return ans;
    }
    int all = 1;
    int p = max(x.n, x.m);
    int q = max(y.n, y.m);
    int w = max(p, q);
    while (all < w)
    {
        all = all * 2;
    }
    if (all == 1)
    {
        ans.con[0][0] = x.con[0][0] * (y.con[0][0]);
    }
    int mid = all / 2;
    Matrix a, b, c, d, e, f, g, h;
    a.copyFrom(x, 0, mid, 0, mid);
    b.copyFrom(x, 0, mid, mid, all);
    c.copyFrom(x, mid, all, 0, mid);
    d.copyFrom(x, mid, all, mid, all);
    e.copyFrom(y, 0, mid, 0, mid);
    f.copyFrom(y, 0, mid, mid, all);
    g.copyFrom(y, mid, all, 0, mid);
    h.copyFrom(y, mid, all, mid, all);
    Matrix P1 = stressenMulti(a, (f - h));
    Matrix P2 = stressenMulti((a + b), h);
    Matrix P3 = stressenMulti((c + d), e);
    Matrix P4 = stressenMulti(d, (g - e));
    Matrix P5 = stressenMulti((a + d), (e + h));
    Matrix P6 = stressenMulti((b - d), (g + h));
    Matrix P7 = stressenMulti((a - c), (e + f));
    Matrix r = P5 + P4 - P2 + P6;
    Matrix s = P1 + P2;
    Matrix t = P3 + P4;
    Matrix u = P5 + P1 - P3 - P7;
    ans.copyTo(r, 0, mid, 0, mid);
    ans.copyTo(s, 0, mid, mid, all);
    ans.copyTo(t, mid, all, 0, mid);
    ans.copyTo(u, mid, all, mid, all);
    return ans;
}