def calculate_unc(x, y, m, b):
    N = len(x)
    s = 0
    s_sq = 0
    for i in range(N):
        s += x[i]
        s_sq += x[i]**2
    delta = N*s_sq - s**2
    var = 0
    for i in range(N):
        var += (y[i] - (m*x[i]+b))**2
    var /= (N-2)
    sm = round_unc((N*var/delta)**(1/2))
    sb = round_unc((var*s_sq/delta)**(1/2))
    
    return sm, sb

def round_unc(unc):
    pow = 0
    if(unc > 10):
        i = -1
    elif (unc < 1):
        i = 1
    else:
        return int(unc)
    while((unc > 10) or (unc < 1)):
        unc *= (10)**i
        pow += i
    return int(unc) / 10**pow
