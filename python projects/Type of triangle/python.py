def kind_of_triangle(a,b,c):
    if((a>=(b+c))or(b>=(a+c))or(c>=(b+a))):
        print('Triangle is not possible')
    else:
        if(a==b and b==c):
            print('Triangle is Equilateral')
        elif(a==b and b!=c) or (a!=b and b==c) or (a!=b and a==c):