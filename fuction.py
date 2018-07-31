import numpy as np

#等额本息
def average_capital_plus_interest(PV,mouth_rate,nper,Sum_interest=0):
    for i in range(1, nper + 1):
        PPMT = np.ppmt(mouth_rate, i, nper, PV)
        IPMT = np.ipmt(mouth_rate, i, nper, PV)
        EIR=mouth_rate*12 #有效年化利率
        PMT = PPMT + IPMT
        Sum_interest+=IPMT
        yield i,round(-PPMT,1),round(-IPMT,1),round(-PMT,1)
        if i == nper:
            yield "总利息："+str(round(-Sum_interest,1)),"实际利率："+str("%.2f%%" % (EIR * 100))



#等额本息by 实际利息
def average_capital_plus_interest_by_actualInterest(PV,mouth_rate,nper):
    year_actual_Interest=mouth_rate*PV*nper
    FV=PV+year_actual_Interest
    PMT=FV/nper
    EIR=np.rate(nper,-PMT,PV,0)*12
    actual_mouth_rate=EIR/12
    for i in range(1, nper + 1):
        PPMT = np.ppmt(actual_mouth_rate, i, nper, PV)
        IPMT = np.ipmt(actual_mouth_rate, i, nper, PV)
        yield i,-PPMT,-IPMT,PMT
        if i == nper:
            yield year_actual_Interest,round(EIR,4)


#等额本金
def average_capital(PV,mouth_rate,nper,Sum_interest=0):
    PPMT=PV/nper
    EIR=mouth_rate*12
    for i in range(1, nper + 1):
        left_capital = PV - PPMT * (i - 1) # 求出每期剩余本金
        IPMT = left_capital * mouth_rate # 求出每期利息
        Sum_interest+=IPMT
        PMT=PPMT+IPMT
        yield i,round(left_capital,1),round(PPMT,1), round(IPMT,1), round(PMT,1),round(mouth_rate,4)
        if i == nper:
            yield Sum_interest, "%.2f%%" % (EIR * 100)




#等本等息
def equal_capital_equal_interest(PV,mouth_rate,nper,Sum_interest=0):
    PPMT = PV / nper
    IPMT = PV * mouth_rate
    PMT=PPMT+IPMT
    EIR = np.rate(nper, -PMT, PV, 0) * 12
    for i in range(1, nper + 1):
        left_capital = PV - PPMT * (i - 1) #求出剩余本金
        Sum_interest += IPMT
        actual_mouth_RATE = IPMT / left_capital
        yield i,round(left_capital,1),round(PPMT,1), round(IPMT,1), round(PMT,1),round(actual_mouth_RATE,4)
        if i == nper:
            yield Sum_interest, round(EIR,4)


#先息后本
def interest_first_then_capital(PV,mouth_rate,nper):
    IPMT=PV*mouth_rate
    Sum_interest=IPMT*nper
    EIR = mouth_rate * 12
    for i in range(1, nper + 1):
        if i != nper:   # 求出每期剩余本金
            left_capital = PV
            PPMT = 0
        else:
            left_capital = 0
            PPMT = PV
        PMT=PPMT+IPMT
        yield i, round(left_capital, 1), round(PPMT, 1), round(IPMT, 1), round(PMT, 1), round(mouth_rate, 4)
        if i == nper:
            yield Sum_interest, round(EIR, 4)

