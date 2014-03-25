def prime_factorization(n):
    if is_prime(n):
        return[(n,1)]
    else:
        prime_number_of_divisors(n)


'''def dict_divisors(n):
    divisorss={}
    i=n
    while (i>0):
        if n%i == 0:
            divisorss[i]=divisorss[i]+1
        else:
            i=i-1'''



def prime_number_of_divisors(n):
    sum=0
    i=n-1
    divisorss={}
    while (i>1):
        #print(i)
        if n%i == 0:
            divisorss[i]=1
            print(divisorss)
            n=n//i
        else:
            i=i-1

    return divisorss


    '''divisorss = []
    power = []
    while (i>0):
        if n%i == 0:
            divisorss+=[i]
        else:
            i=i-1
    return is_prime(sum)'''


def is_prime(n):
    sum=0
    i=n
    if n ==1:
        return True
    while (i>0):
        if n%i == 0:
            sum+=i
        i=i-1
    if sum>1+n:
        return False
    return True


def main():
    #print(prime_factorization(5))
    print(prime_factorization(20))
    #print(prime_factorization(20))


if __name__ == '__main__':
    main()
