'''This function will take as input two users, a borrower and an lender, 
as well as the loan amount and how many terms it will paid over'''

''' Assumptions taken:
1. will use timer to count 30 days
2. There is a user object with these methods:
        user.deposit(amount) puts amount in user's account
        user.withdraw(amount) returns an amount of money from user 
             and deducts it
3. loan object has variables amount, terms, complete
'''
'''import time'''
def transfer(borrower, lender, loan):
    '''transfer money from lender to borrower'''
    if lender.hasSufficentFunds:
        borrower.deposit( lender.withdraw(loan.amount))
    else:
        '''throw/raise an error if lender doesn't have sufficent funds and exit'''
        loan.complete(False)
    
    '''divide the money by the number of terms'''
    payment = loan.amount / loan.terms #will be the monthly payment 
    
    '''each term, every 30 days, send lender a payment'''
    while terms > 0:
        if borrower.hasSufficentFunds:
            lender.deposit( borrower.withdraw(payment))
            terms -= 1
            if terms == 0: #if loan has been paid off
                '''mark loan complete and exit'''
                loan.complete(True)
                '''exit '''
        else:
            ''' mark payment as failed and borrower as deliquent 
            then exit '''
            loan.complete(False)
            '''exit'''
            
        '''repeat this monthly until terms = 0'''
        #time.sleep(30 days) 