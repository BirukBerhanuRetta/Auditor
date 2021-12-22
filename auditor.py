#Biruk Berhanu Retta

import os

#getting the file
file_name= input("enter the name of the trial balance: ")
file_name= file_name+ ".csv"
if type(file_name) != str:
    raise AssertionError("filename has to be a string")
    
if not os.path.exists(file_name):
    raise AssertionError("file doesn't exist")

#opening and copying the file onto fobj
fobj= open(file_name, "r", encoding="utf8")



tb= []
#make this a function uve copied it too much
for line in fobj:
    y= line.split(",")
    tb.append(y)




def copying_function(name,start, end):
    #sections off the right parts
    sheet= tb[start:end]
    temp=[]
    
    #try to identify abnormal balances
    debit_sides=["cash", "AR", "stock", "cost_of_goods_sold", "admin"]
    credit_sides= ["creditors","loan", "capital", "income"]
    for ROW in sheet:
        
        if name in debit_sides:
            if ROW[2] =='':
                ROW[3]= '-'+ ROW[3]
        if name in credit_sides:
            if ROW[2] != '':
                ROW[2]= '-'+ ROW[2]
    
    
    
    #opens the correct sheet that has already been created
    name_of_excel= name + ".csv"
    f= open(name_of_excel, "w", encoding= 'utf8')
    
    #loop to make the array back to a string
    for row in sheet:
        
        #makes sure that all values are copied onto the draft section by removing empty colums
        if '' in row:
            row.remove('')
        line= ','.join(row)

        temp.append(line)
    copied_info =''.join(temp)
    whole_sheet_info_in_a_line= "Account Number,Description,Draft, Adjustment, Final,\n"+ copied_info
    f.write(whole_sheet_info_in_a_line)
    f.close()


def sheet_creator(sheets):
    """
    (list) -> (void)
    creates each and every sheet with the appropriate format
    """
    to_B_removed= []
    for sheet in sheets:
        print("we're now working with: " + sheet)
        start= input("where does " + sheet + " start: ")
        if start in ['n' , 'N', 'none', 'None', 'no']:
            to_B_removed.append(sheet)
            
            
        else:
            start= int(start)-1
            end= int(input("where does " + sheet+ " end: "))
            copying_function(sheet, start, end)
     
    for sheet in to_B_removed:
        sheets_to_be_created.remove(sheet)

sheets_to_be_created=["stock", "AR", "cash", "creditors", "loan", "income", "cgs", "admin"]
sheet_creator(sheets_to_be_created)

def fixed_asset():
    print("we're now working with: fixed asset " )
    start= int(input("where do " + "fixed assets" + " start: "))-1
    end= int(input("where do " + "fixed assets" + " end: "))
    
    FA= tb[start:end]
    assets=[]
    depreciations=[]
    added_months=[]
    
    #classify into asset and depreciation
    for element in FA:
        if element[2] == '':
            
            depreciations.append(element)
        else:
            assets.append(element)
    
    #iterating through each asset asking for opening balances
    for asset in assets:
        temp1= input("Enter the opening balance for " + asset[1] +": ")
        asset[2]= temp1
        
        add= input("Enter any additions: (0 if none)")
        month = input("How many months has it been used: ")
        added_months.append(month)
        if len(asset)<4:
            asset.append(add) 
        else:
            asset[3]= add
        
        dis= input("Enter any disposals:(0 if none) ")
        
        if len(asset)<5:
            asset.append(dis) 
        else:
            asset[4]= dis 
        
    for depreciation in depreciations:
        temp2= input("Enter the opening balance for " + depreciation[1] + ": ")
        depreciation[2] = temp2
        
        disp= input("Enter any disposals:(0 if none) ")
        
        if len(depreciation)<5:
            depreciation.append(disp) 
        else:
            depreciation[4]= disp 

    
    #calculating this years depreciation
    for i in range(len(assets)):
        typee= input("what type of asset is " + assets[i][1] +"\n Enter B for building, C for computer, O for other")
        net = float(assets[i][2]) - float(assets[i][4])
        
        if typee == "B":
            
            depreciations[i][3]= round(net*0.05,2)
            addition_depriciation= round(float(assets[i][3]) * (int(added_months[i])/12)*0.05, 2)
            depreciations[i][3]+= addition_depriciation
            depreciations[i][3] = str(depreciations[i][3])
        if typee == "C":
            depreciations[i][3]= (net- float(depreciations[i][2]))*0.25
            addition_depriciation= round(float(assets[i][3]) * (int(added_months[i])/12)*0.25, 2)
            depreciations[i][3]+= addition_depriciation
            depreciations[i][3]= str(round(depreciations[i][3],2)) 
        if typee == "O":
            depreciations[i][3]= (net- float(depreciations[i][2]))*0.2
            addition_depriciation= round(float(assets[i][3]) * (int(added_months[i])/12)*0.2, 2)
            depreciations[i][3]+= addition_depriciation
            depreciations[i][3]= str(round(depreciations[i][3],2))
    
    
    #horizontal sum
    #vertical sum too
            
    VsumAss= 0
    for asset in assets:
        hsum= round(float(asset[2])+ float(asset[3])+ float(asset[4]),2)
        n_hsum = str(hsum) + "\n"
        VsumAss+= hsum
        asset.append(n_hsum)
    tot_line_ass = "Total,,,,," + str(VsumAss)
    
    
    VsumDep= 0
    for depreciation in depreciations:
        added=round(float(depreciation[2])+ float(depreciation[3])+ float(depreciation[4]),2)
        nadded= str(added) + "\n"
        VsumDep+= added
        depreciation.append(nadded)
    tot_line_dep= "Total,,,,," + str(VsumDep)
    net_book= "Net Book value,,,,," + str(VsumAss- VsumDep)
    
    
    
    #writting it all down
    fa= open("FA.csv", "w")
    
    temp3=[]
    for row in assets:
        
        line= ','.join(row)

        temp3.append(line)
        
    copied_assets =''.join(temp3)
    
    temp4=[]
    for row1 in depreciations:
        
        line1= ','.join(row1)

        temp4.append(line1)
        
    copied_depreciations =''.join(temp4)
    
    whole_sheet_info_in_a_line= "Account Number,Description,Draft, Addition, disposal, Final,\n"+ copied_assets+ "\n"+tot_line_ass + "\n"+ copied_depreciations+ tot_line_dep+ net_book
    fa.write(whole_sheet_info_in_a_line)
    fa.close()
fixed_asset()

def sumer(sheets):
    
    #(list) ->(none)
    
    
    for sheet in sheets:
        fobj= open(sheet+ ".csv" , "r", encoding='utf8')
        
        data= []
        for line in fobj:
            y= line.split(",")
            data.append(y)
        
        summ=0
        for row in data[1:]:
            num= row[2].replace(" ",'')
            tempp= float(num)
            summ += tempp
            
        fobj.close()
        
        
        fobject= open(sheet+ ".csv" , "a", encoding='utf8')
        fobject.write("TOTAL,,"+ str(round(summ,2)))
        fobject.close()
        
def profit_or_loss():
    
    
    
    #income
    fobj= open("income.csv", "r", encoding ='utf8')
    ic=[]
    for line in fobj:
        x= line.split(",")
        ic.append(x)
        
        income= ic[-1][-1]
        income= income.replace(" ",'')
        
    
     #cgs
    fobj= open("cgs.csv", "r", encoding ='utf8')
    cg=[]
    for line in fobj:
        y= line.split(",")
        cg.append(y)
            
        cgs= cg[-1][-1]
        cgs= cgs.replace(" ",'')
        
    
    #admin
    fobj= open("admin.csv", "r", encoding ='utf8')
    ad=[]
    for line in fobj:
        z= line.split(",")
        ad.append(z)
            
        admin= ad[-1][-1]
        admin= admin.replace(" ",'')
    
    
    
    
    add_back_str=[]
    add_back_no=[]
    i =0
    ad_bck= input("any add back?")
    while ad_bck == "Y":
        add_back= input("add or deduct name(string)?")
        add_bck_no= float(input("amount?"))
        add_back_str.append(add_back)
        add_back_no.append(add_bck_no)
        ad_bck= input("any add back?")
    
    gross_profit = str(round(float(income)- float(cgs),2))
    profit= round(float(gross_profit)- float(admin),2)
    
    for ad in add_back_no:
        profit= round(profit - ad,2)
        
        
    if profit>0:
        comp_type= input("sole prop(P)?, S.C or PLC (NP)? or tax-holiday(TH)?")
        if comp_type == "P" or "p":
            tax= round((profit*0.35)-18000,2)
            p= "(profit*0.35)-18000"
        elif comp_type == "NP" or "Np" or "np":
            tax= round(profit*0.3,2)
            p = "(profit*0.3)"
        elif comp_type == "TH" or "Th" or "th":
            tax= float(input("please enter provision of tax according to your calculation: "))
            p= "profit*0"
    else:
        p="no profit"
        tax=0
    
    #side note you are creating a lead for tax
    
    tobj= open("profit tax.csv", "w", encoding = 'utf8')
    ln1= "Description, amount\nProfit tax"+ p + "," + str(tax)+ "\n"
    tobj.write(ln1)
    tobj.close()
    
    net_profit= profit- tax
    for ad in add_back_no:
        profit_carried= round(net_profit + ad,2)
    
    #writing it in
    profit= str(profit)
    tax= str(tax)
    net_profit= str(net_profit)
    profit_carried=str(profit_carried)
    adds=""
    i=0
    while i<len(add_back_str):
        adds= adds+ "\n" + add_back_str[i]  + "," +str(add_back_no[i])
        i= i+1
    
    f= open("Profit(Loss).csv", "w", encoding= 'utf8')
    info= "Sales," + income +"\n" + "LESS: Cost of sales,(" + cgs + ")\n" + "Gross profit,"+ gross_profit + "\n " + "Adminstration cost," + admin +"\n"+"Profit(Loss)," + profit + "\n" + "Provision for taxation," + tax +"\n" + "Profit-less tax," +  net_profit + "\n" +adds +"\n,"+ profit_carried      

    f.write(info)
    f.close()

def retained_earning():
    paid_c = float(input("please enter the opening balance of paid up capital: "))
    acc_pl = float(input("please enter the opening balance of accumlated profit(loss): "))
    legal_r= float(input("please enter the opening balance of legal reserve: "))
    
    f= open("Profit(Loss).csv", "r", encoding= 'utf8')
    
    pl= []
    #make this a function uve copied it too much
    for line in f:
        y= line.split(",")
        pl.append(y)
    
    f.close()
    prolos= pl[-1][1]
    prolos=prolos.replace(" ",'')
    prolos= float(prolos)
    leg_res_exists= input("should I calculate legal reserve for you?(y/n)")
    
    if ((prolos> 0) and (leg_res_exists == "y")) :
        if (0.1*paid_c) > legal_r:
            legal_r_add = prolos*0.05
        
        else:
            legal_r_add = 0
    else:
        legal_r_add = 0
        
    add_c = float(input("please enter the capital increase(if any) : "))
    
    
    withdrawal= float(input("any withdrawals?(0 if none)"))
    profit_carried_forward= prolos - legal_r_add - withdrawal
    
    fin_paid_cap= paid_c+ add_c
    line1= "description, opening, adjustment, final\n"
    line2 = "Paid up capital," + str(paid_c) +"," + str(add_c) +"," + str(fin_paid_cap)+ "\n"
    
    fin_acc_pl= acc_pl + profit_carried_forward
    line3= "Accumlated profit(loss)," + str(acc_pl) + "," + str(profit_carried_forward) +"," + str(fin_acc_pl)+"\n"+ "Withdrawal,"
    
    fin_legal_res= legal_r+ legal_r_add
    line4 = "Legal reserve," + str(legal_r) +"," + str(legal_r_add) +"," + str(fin_legal_res)+ "\n"
    
    foj= open("Retained earning.csv" , "w", encoding= 'utf8')
    foj.write(line1+ line2+ line3 + line4)
sumer(sheets_to_be_created)
profit_or_loss()
retained_earning()
def lead():
    print("Please post adjustments and save the files and make sure they're closed")
    
    
    #cash
    coh_start= int(input("where does cash on hand start? "))-1
    coh_end = int(input("where does cash on hand end? "))
    
    cab_start= int(input("where does cash at bank start? "))-1
    cab_end = int(input("where does cash at bank end? "))
    
    if os.path.exists("cash.csv"):
        fobject = open("cash.csv", "r", encoding= 'utf8')
    cash= []
    #make this a function uve copied it too much
    for line in fobject:
        y= line.split(",")
        cash.append(y)
    fobject.close()
    
    coh= cash[coh_start:coh_end]
    tot_coh= 0
    for c in coh:
        tot_coh+= float(c[-1])
    
        
    cab= cash[cab_start:cab_end]
    tot_cab= 0
    for c in cab:
        tot_cab+= float(c[-1])
    
    tot_cash= tot_coh + tot_cab
    
    csh_lead= "Description, amount\nCash on hand," + str(round(tot_coh,2))+ "\n"+ "Cash at bank," + str(round(tot_cab,2)) + "\n" + "Total," + str(round(tot_cash,2))
    
    fo= open("cash_lead.csv", "w", encoding= 'utf8')
    fo.write(csh_lead)
    fo.close()
    
    
    #Accounts recievable
    if os.path.exists("AR.csv"):
        fobject = open("AR.csv", "r", encoding= 'utf8')
    ar= []
    #make this a function uve copied it too much
    for line in fobject:
        y= line.split(",")
        ar.append(y)
    fobject.close()
    
    new_class=["trade debtors","staff debtors","sundry debtors","advance profit tax","others"]
    tots_ar=[]
    
        
    print(new_class)
    cont= input("any other classification? (y/n)")
    
    while cont == "y" or cont == "Y" :
        temp = input("state your classification: ")
        new_class.append(temp)
        cont= input("any other classification? (y/n)")
        
    for clas in new_class:
        c_start= int(input("where does " + clas+ " start(enter 1 if this classification doesnt apply): "))-1
        if c_start!= 0:
        
            c_end= int(input("where does " + clas + " end: "))
            c= ar[c_start: c_end]
            c_tot=0
            for e in c:
                c_tot += float(e[-1])
            tots_ar.append(c_tot)
    
    ar_lead= "Description, amount\n"
    for i in range(len(new_class)):
        ar_lead= ar_lead+ new_class[i]+ ","+ str(tots_ar[i])+"\n"
    
    #for calculating the total
        total_ar= 0
    for tot in tots_ar:
        total_ar+= tot
    ar_lead= ar_lead + "Total," + str(total_ar)
    
    fo= open("AR_lead.csv", "w", encoding= 'utf8')
    fo.write(ar_lead)
    fo.close()

    #creditors
    if os.path.exists("creditors.csv"):
        fobject = open("creditors.csv", "r", encoding= 'utf8')
    cr= []
    #make this a function uve copied it too much
    for line in fobject:
        y= line.split(",")
        cr.append(y)
    fobject.close()
    
    new_class=["shareholders account","interest payable","sundry creditors","income tax payable","pension contribution", "VAT payable", "wht payable"]
    tots_cr=[]
    
        
    print(new_class)
    cont= input("any other classification? (y/n)")
    
    while cont == "y" or cont == "Y":
        temp = input("state your classification: ")
        new_class.append(temp)
        cont= input("any other classification? (y/n)")
        
    for clas in new_class:
        c_start= int(input("where does " + clas+ " start: "))-1
        if c_start!= 0:
        
            c_end= int(input("where does " + clas + " end: "))
            c= cr[c_start: c_end]
            c_tot=0
            for e in c:
                c_tot += float(e[-1])
            tots_cr.append(c_tot)
    
    cr_lead= "Description, amount\n"
    for i in range(len(new_class)):
        cr_lead= cr_lead+ new_class[i]+ ","+ str(tots_cr[i])+"\n"
    
    #for calculating the total
        total_cr= 0
    for tot in tots_cr:
        total_cr+= tot
    cr_lead= cr_lead + "Total," + str(total_cr)
    
    fo= open("Creditors_lead.csv", "w", encoding= 'utf8')
    fo.write(cr_lead)
    
    #stock
    ###check file opening is alright and catch exceptions or sth
    if os.path.exists("stock.csv"):
        fobject = open("stock.csv", "r", encoding= 'utf8')
        stock= []
        
    #make this a function uve copied it too much
        for line in fobject:
            y= line.split(",")
            stock.append(y)
        fobject.close()
        
        new_class=["stock"]
        tots_stock=[]
        
            
        print(new_class)
        cont= input("any other classification? (y/n)")
        
        while cont == "y" or cont == "Y":
            temp = input("state your classification: ")
            new_class.append(temp)
            cont= input("any other classification? (y/n)")
            
        for clas in new_class:
            c_start= int(input("where does " + clas+ " start: "))-1
            if c_start!= 0:
                
                c_end= int(input("where does " + clas + " end: "))
                c= stock[c_start: c_end]
                c_tot=0
                for e in c:
                    c_tot += float(e[-1])
                tots_stock.append(c_tot)
        
        stock_lead= "Description, amount\n"
        for i in range(len(new_class)):
            stock_lead= stock_lead+ new_class[i]+ ","+ str(tots_stock[i])+"\n"
        
        #for calculating the total
            total_stock= 0
        for tot in tots_stock:
            total_stock+= tot
        stock_lead= stock_lead + "Total," + str(total_stock)
        
        fo= open("stock_lead.csv", "w", encoding= 'utf8')
        fo.write(stock_lead)
        fo.close()
    
def balance_sheet():
    #fa
    fobject = open("FA.csv", "r", encoding= 'utf8')
    FA_for_bs= []
    #make this a function uve copied it too much
    for line in fobject:
        y= line.split(",")
        FA_for_bs.append(y)
    fobject.close()
    
    fa_tots= FA_for_bs[-1][-1]
    
    #cash
    if os.path.exists("cash_lead.csv"):
        fobject = open("cash_lead.csv", "r", encoding= 'utf8')
        cash_for_bs= []
        #make this a function uve copied it too much
        for line in fobject:
            y= line.split(",")
            cash_for_bs.append(y)
        fobject.close()
        
        cash_tots= cash_for_bs[-1][-1]
    else:
        cash_tots="0"
    #ar
    if os.path.exists("AR_lead.csv"):
        fobject = open("AR_lead.csv", "r", encoding= 'utf8')
        AR_for_bs= []
        #make this a function uve copied it too much
        for line in fobject:
            y= line.split(",")
            AR_for_bs.append(y)
        fobject.close()
        
        AR_tots= AR_for_bs[-1][-1]
    else:
        AR_tots="0"
    
    
    # stock
    if os.path.exists("stock_lead.csv"):
        fobject = open("stock_lead.csv", "r", encoding= 'utf8')
        stock_for_bs= []
        #make this a function uve copied it too much
        for line in fobject:
            y= line.split(",")
            stock_for_bs.append(y)
        fobject.close()
        
        stock_tots= stock_for_bs[-1][-1]
    else:
        stock_tots='0'
    #total_assets= float(fa_tots)+ float(cash_tots) + float(AR_tots)+ float(stock_tots)
    
    #retained earning
    
    fobject = open("retained earning.csv", "r", encoding= 'utf8')
    re_for_bs= []
    #make this a function uve copied it too much
    for line in fobject:
        y= line.split(",")
        re_for_bs.append(y)
    fobject.close()
    
    
    paid_up_capital= re_for_bs[1][-1]
    accum_pl= re_for_bs[2][-1]
    legal_r= re_for_bs[3][-1]
    ###accumlated pl + net profit
    ### check if legal reserve needs to be added  do this before the others
    ###0.05*net profit for sc and plc
    ## lr =0 for others
    #accumlated profit = starter+ netprofit- lr
    
    
    
    
    #loan
    if os.path.exists("loan.csv"):
        
        fobject = open("loan.csv", "r", encoding= 'utf8')
        
        loan_for_bs= []
        #make this a function uve copied it too much
        for line in fobject:
            y= line.split(",")
            loan_for_bs.append(y)
        fobject.close()
        
        loan_tots= loan_for_bs[-1][-1]
    else:
        loan_tots= "0"
        
        
    #payable
    if os.path.exists("creditors.csv"):
        fobject = open("creditors.csv", "r", encoding= 'utf8')
        ap_for_bs= []
        #make this a function uve copied it too much
        for line in fobject:
            y= line.split(",")
            ap_for_bs.append(y)
        fobject.close()
        
        ap_tots= ap_for_bs[-1][-1]
    
    else:
        ap_tots="0"
    
    #cont'd from 272
    
    advance_tax= input("acceptable withholding")
    tobj= open("profit tax.csv", "r", encoding = 'utf8')
    
    # tobj.read()
    
    protax=[]
    for line in tobj:
        y= line.split(",")
        protax.append(y)
    tobj.close()
    calc_pro_tax= protax[-1][-1]
    ln2= "Advance profit tax,"+ advance_tax+ "\n"
    
    net_tax= float(calc_pro_tax)- float(advance_tax)
    ln3= "Net tax," + str(net_tax)
    
    temp=[]
    for row in protax:
        line= ','.join(row)

        temp.append(line)
    str_protax =''.join(temp)
    
    tnewobj=open("profit tax.csv", "w", encoding = 'utf8')
    tnewobj.write(str_protax+ "\n"+ ln2+ln3)
    tnewobj.close()
    if net_tax>0:
        fnettax = open("creditors.csv", "a", encoding= 'utf8')
        
        
        nwline= "Profit tax payable," +str(net_tax)
        
        fnettax.write(nwline)
        
    if net_tax<0:
        AR_for_bs[4][1]= str(net_tax)
        
        
        for row in AR_for_bs:

        
            line= ','.join(row)

            temp.append(line)
    new_ar =''.join(temp) 
    
    arobj= open("AR_lead", "w", encoding= 'utf8')
    arobj.write(new_ar)
    arobj.close()
    
    #continue with your balance sheet
    
    tax_tot= str(net_tax)
    
    ln123="\n"+"non-current asset\n"+ "Fixed Asset,," + fa_tots+ "\n"
    ln45= "Current Asssets\n"+ "Cash and bank,"+ cash_tots+"\n"
    ln67= "Accounts recievable," + AR_tots + "\n" + "Stock," + stock_tots+ "\n"
    current_assets= round(float(cash_tots)+ float(AR_tots)+ float(stock_tots),2)
    ln8= " ,,"+ str(current_assets)+ "\n"
    total_assets= round(current_assets+ float(fa_tots),2)
    ln9= "TOTAL assets,,"+ str(total_assets) +"\n"
    ln10="EQUITY AND LIABILITY\n"+ "Equity\n"+ "registerd capital,"+ paid_up_capital+ "\n"
    ln13= "Accumlated profit(loss)," + accum_pl+ "\n"+ "Legal reserve," + legal_r+ "\n"
    total_equity= round(float(paid_up_capital)+ float(accum_pl)+ float(legal_r),2)
    ln15= "total equity,,"+ str(total_equity)+ "\n"+ "Non-current liability\n"
    ln17= "loan,,"+ loan_tots+ "\n"+ "Current liabilities\n"
    ln19= "Trade and other payables,"+ ap_tots+ "\n" + "Profit tax payable,"+ tax_tot +"\n"
    current_liabilities= round(float(ap_tots)+ float(tax_tot),2)
    tot_equity_liability= round(current_liabilities+ float(total_equity),2)
    ln20= " ,,"+ str(current_liabilities)+ "\n"+  "TOTAL equity and liability,,"+ str(tot_equity_liability)
    
    bsobj= open("balance sheet.csv", "w", encoding= 'utf8')
    bsobj.write(ln123+ ln45+ ln67+ ln8+ ln9+ ln10+ ln13+ ln15+ ln17+ ln19+ ln20)
    
    
    
lead()

balance_sheet()
#note to self:enter arow of zeros for every sheet