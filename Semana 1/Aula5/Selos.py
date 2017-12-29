# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
#
# (No fair for USians to just say use a "Forever" stamp and be done with it!)
#

def stamps2(t):
    s1= 5
    s2= 2
    s3= 1
    qs1 = t//s1
    print qs1
    qs2 = t%s1//s2
    qs3 = t%s1%s2//s3
    return qs1,qs2, qs3

def stamps3(n):
    x = n // 5 #Quantos selos de 5p cabem no valor(n) inserido?
    y = (n - x * 5) // 2 #Quantos selos de 2p, subtraindo-se o valor já utilizado para selos de 5p?
    z = (n - y * 2 - x * 5) #O resto necessariamente se converterá em selos de 1p.
    return x,y,z

def trupa(num,vlr,soma):
    time = 1
    tot = soma
    while True:
        if (vlr*time) + soma <= num:            
            time = time + 1
        else:
            break
    
    time = time - 1
    tot = tot + (vlr*time)
    return time,tot

def stamps(num):
    # Your code here
    time = 1
    tot = 0
    concat = "("

    time,tot = trupa(num,5, 0);   
    #print time,tot
    concat = concat + str(time) + ','
    q1 = time

    time,tot = trupa(num,2, tot);
    #print time,tot
    concat = concat + str(time) + ','
    q2 = time

    time,tot = trupa(num,1, tot);
    #print time,tot
    concat = concat + str(time) + ')'
    q3 = time

    return q1,q2,q3
        
    

#print stamps(40)

print stamps2(8)
#>>> (1, 1, 1)  # one 5p stamp, one 2p stamp and one 1p stamp
print stamps2(5)
#>>> (1, 0, 0)  # one 5p stamp, no 2p stamps and no 1p stamps
print stamps2(29)
#>>> (5, 2, 0)  # five 5p stamps, two 2p stamps and no 1p stamps
print stamps2(0)
#>>> (0, 0, 0) # no 5p stamps, no 2p stamps and no 1p stamps