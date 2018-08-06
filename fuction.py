# -*- coding:utf-8 -*- 

import numpy as np

#等额本息
def average_capital_plus_interest(PV,mouth_rate,nper,Sum_interest=0,returned_capital=0):
    for i in range(1, nper + 1):
        PPMT = -np.ppmt(mouth_rate, i, nper, PV)
        IPMT = -np.ipmt(mouth_rate, i, nper, PV)
        EIR=mouth_rate*12 #有效年化率
        PMT = PPMT + IPMT
        Sum_interest+=IPMT
        returned_capital+= PPMT  # 求出已还本金
        left_capital=PV-returned_capital #求出剩余本金
        actual_mouth_rate = IPMT / (left_capital+PPMT) #求出月利率
        Sum_money=PV+Sum_interest
        yield '第'+str(i)+'期',round(PPMT,1),round(IPMT,1),round(PMT,1),round(left_capital,1),"%.2f%%" % (actual_mouth_rate * 100)
        if i == nper:
            yield "还款总额："+str(round(Sum_money,1)),"总利息："+str(round(Sum_interest,1)),"年利率："+str("%.2f%%" % (EIR * 100))



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
def average_capital(PV,mouth_rate,nper,Sum_interest=0,returned_capital=0):
    PPMT=PV/nper
    EIR=mouth_rate*12
    for i in range(1, nper + 1):
        returned_capital += PPMT  # 求出已还本金
        left_capital = PV - returned_capital  # 求出剩余本金
        IPMT = (left_capital+PPMT) * mouth_rate # 求出每期利息
        Sum_interest+=IPMT
        PMT=PPMT+IPMT
        Sum_money = PV + Sum_interest
        yield '第'+str(i)+'期',round(PPMT,1), round(IPMT,1), round(PMT,1),round(left_capital,1),"%.2f%%" % (mouth_rate * 100)
        if i == nper:
            yield "还款总额："+str(round(Sum_money,1)),"总利息："+str(round(Sum_interest,1)),"年利率："+str("%.2f%%" % (EIR * 100))




#等本等息
def equal_capital_equal_interest(PV,mouth_rate,nper,Sum_interest=0,returned_capital=0):
    PPMT = PV / nper
    IPMT = PV * mouth_rate
    PMT=PPMT+IPMT
    EIR = np.rate(nper, -PMT, PV, 0) * 12
    for i in range(1, nper + 1):
        returned_capital += PPMT  # 求出已还本金
        left_capital = PV - returned_capital  # 求出剩余本金
        Sum_interest += IPMT
        actual_mouth_rate = IPMT / (left_capital + PPMT)
        Sum_money = PV + Sum_interest
        yield '第'+str(i)+'期',round(PPMT,1), round(IPMT,1), round(PMT,1),round(left_capital,1),"%.2f%%" % (actual_mouth_rate * 100)
        if i == nper:
            yield "还款总额："+str(round(Sum_money,1)),"总利息："+str(round(Sum_interest,1)),"年利率："+str("%.2f%%" % (EIR * 100))


#按月还息到期还本
def interest_first_then_capital(PV,mouth_rate,nper):
    IPMT=PV*mouth_rate
    Sum_interest=IPMT*nper
    EIR = mouth_rate * 12
    for i in range(1, nper + 1):
        if i != nper:
            left_capital = PV
            PPMT = 0
        else:
            left_capital = 0
            PPMT = PV
        PMT=PPMT+IPMT
        Sum_money = PV + Sum_interest
        yield '第'+str(i)+'期',round(PPMT, 1), round(IPMT, 1), round(PMT, 1),round(left_capital,1),"%.2f%%" % (mouth_rate * 100)
        if i == nper:
            yield "还款总额："+str(round(Sum_money,1)),"总利息："+str(round(Sum_interest,1)),"年利率："+str("%.2f%%" % (EIR * 100))



#按季还息到期还本
def quarter_interest_first_then_capital(PV,mouth_rate,nper,Sum_interest=0,returned_capital=0):
    IPMT=PV*mouth_rate

    EIR = mouth_rate * 12
    for i in range(1, nper + 1):
        if i % 3 == 0 and i != nper:
            IPMT = PV * mouth_rate * 3
            PPMT = 0
        elif i % 3 != 0 and i != nper:
            IPMT = 0
            PPMT = 0
        elif i % 3 != 0 and i == nper:
            IPMT = (nper % 3) * PV * mouth_rate
            PPMT = PV
        elif i % 3 == 0 and i == nper:
            IPMT = PV * mouth_rate * 3
            PPMT = PV

        PMT = PPMT + IPMT
        returned_capital += PPMT  # 求出已还本金
        left_capital = PV - returned_capital  # 求出剩余本金
        Sum_interest += IPMT
        Sum_money = PV + Sum_interest
        yield '第'+str(i)+'期',round(PPMT, 1), round(IPMT, 1), round(PMT, 1),round(left_capital,1),"%.2f%%" % (mouth_rate * 100)
        if i == nper:
            yield "还款总额："+str(round(Sum_money,1)),"总利息："+str(round(Sum_interest,1)),"年利率："+str("%.2f%%" % (EIR * 100))

