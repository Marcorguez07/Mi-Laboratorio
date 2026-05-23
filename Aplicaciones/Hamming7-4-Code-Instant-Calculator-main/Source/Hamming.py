#Hamming 7-4 transformer, Made by Marco Rodríguez, Marcokistan 2025, CS project

command = ("")

print("----------------------------------------------------\nHamming(7,4) Code Correction - Instant Calculator\nBy Marco Rodríguez, 1.1v\n----------------------------------------------------")

def askagain():
    global command
    command = ("")
    while command == (""):
        try:
            command = input("State what mode would you like to use: Hamming_Check or Hamming_Convert: ")
        except:
            pass
    if command == ("Hamming_Check"):
        command = ("")
        while command == (""):
            try:
                command = input("State what parity this hamming code follows (Even or Odd): ")
            except:
                pass
        if command == ("Even"):
            checkinghammingpar()
        elif command == ("Odd"):
            checkinghammingimpar()
        else:
            print(f"{command} is not a parity type: Even or Odd, try again")
            askagain()   
    elif command == ("Hamming_Convert"):
        command = ("")
        while command == (""):
            try:
                command = input("State the parity (Even or Odd): ")
            except:
                pass
        if command == ("Even"):
            paridadpar()
        elif command == ("Odd"):
            paridadimpar()
        else:
            print(f"{command} is not a parity type: Even or Odd, try again")
            askagain()
        
    else:
        askagain()

def checkinghammingimpar():
    insertedvar = ("")
    binary0 = ("000")
    binary1 = ("001")
    binary2 = ("010")
    binary3 = ("011")
    binary4 = ("100")
    binary5 = ("101")
    binary6 = ("110")
    binary7 = ("111")
    int1 = 0
    int2 = 0
    int3 = 0
    int4 = 0
    int5 = 0
    int6 = 0
    int7 = 0
    var1 = ("")
    var2 = ("")
    var3 = ("")
    var4 = ("")
    var5 = ("")
    var6 = ("")
    var7 = ("")
    downcheck = 0
    midcheck = 0
    upcheck = 0
    downcheckinstr = ("")
    midcheckinstr = ("")
    upcheckinstr = ("")
    totalcheckinstr = ("")
    insertedvar = input("Introduce a seven digits binary number in Hamming7-4 Error Code Correction format: ")
    localcounter = len(insertedvar)
    if localcounter > 7 or localcounter < 7 or insertedvar.isdigit() == False or insertedvar[0] not in ('0', '1') or insertedvar[1] not in ('0', '1') or insertedvar[2] not in ('0', '1') or insertedvar[3] not in ('0', '1') or insertedvar[4] not in ('0', '1') or insertedvar[5] not in ('0', '1') or insertedvar[6] not in ('0', '1'):
        del int1, int2, int3, int4, int5, int6, int7
        checkinghammingimpar()
        return
    else:
        pass
    int1 = int(insertedvar[6])
    int2 = int(insertedvar[5])
    int3 = int(insertedvar[4])
    int4 = int(insertedvar[3])
    int5 = int(insertedvar[2])
    int6 = int(insertedvar[1])
    int7 = int(insertedvar[0])

    # checks
    downcheck = 1 - (int1 ^ int3 ^ int5 ^ int7)
    midcheck = 1 - (int2 ^ int3 ^ int6 ^ int7)
    upcheck = 1 - (int4 ^ int5 ^ int6 ^ int7)
    #concatenation so we can add each number and instantly convert it to int later
    downcheckinstr = str(downcheck)
    midcheckinstr = str(midcheck)
    upcheckinstr = str(upcheck)
    totalcheckinstr = upcheckinstr + midcheckinstr + downcheckinstr

    #real check now
    
    if totalcheckinstr == binary1:
        if int1 == 1:
            int1 = 0
        else:
            int1 = 1

    if totalcheckinstr == binary2:
        if int2 == 1:
            int2 = 0
        else:
            int2 = 1

    if totalcheckinstr == binary3:
        if int3 == 1:
            int3 = 0
        else:
            int3 = 1

    if totalcheckinstr == binary4:
        if int4 == 1:
            int4 = 0
        else:
            int4 = 1

    if totalcheckinstr == binary5:
        if int5 == 1:
            int5 = 0
        else:
            int5 = 1

    if totalcheckinstr == binary6:
        if int6 == 1:
            int6 = 0
        else:
            int6 = 1

    if totalcheckinstr == binary0:
        print("No errors in this Hamming7-4 code!")
        askagain()
    else:
        var1 = str(int1)
        var2 = str(int2)
        var3 = str(int3)
        var4 = str(int4)
        var5 = str(int5)
        var6 = str(int6)
        var7 = str(int7)
        newhamming = (f"Corrected Hamming(7,4): {var7}{var6}{var5}{var4}{var3}{var2}{var1}\n\n")
        infobits = (f"4 Digit Information bits: {var7}{var6}{var5}{var3}\n\n")
        print(f"{newhamming}\n{infobits}")
        del int1, int2, int3, int4, int5, int6, int7
        del var1 , var2, var3, var4, var5, var6, var7
        del binary0, binary1, binary2, binary3, binary4, binary5, binary6, binary7
        del downcheck, midcheck, upcheck, downcheckinstr, midcheckinstr, upcheckinstr, totalcheckinstr, insertedvar, localcounter
        askagain()
    

def checkinghammingpar():
    insertedvar = ("")
    binary0 = ("000")
    binary1 = ("001")
    binary2 = ("010")
    binary3 = ("011")
    binary4 = ("100")
    binary5 = ("101")
    binary6 = ("110")
    binary7 = ("111")
    int1 = 0
    int2 = 0
    int3 = 0
    int4 = 0
    int5 = 0
    int6 = 0
    int7 = 0
    int7 = 0
    var1 = ("")
    var2 = ("")
    var3 = ("")
    var4 = ("")
    var5 = ("")
    var6 = ("")
    var7 = ("")
    downcheck = 0
    midcheck = 0
    upcheck = 0
    downcheckinstr = ("")
    midcheckinstr = ("")
    upcheckinstr = ("")
    totalcheckinstr = ("")
    insertedvar = input("Introduce a seven digits binary number in Hamming7-4 Error Code Correction format: ")
    localcounter = len(insertedvar)
    if localcounter > 7 or localcounter < 7 or insertedvar.isdigit() == False or insertedvar[0] not in ('0', '1') or insertedvar[1] not in ('0', '1') or insertedvar[2] not in ('0', '1') or insertedvar[3] not in ('0', '1') or insertedvar[4] not in ('0', '1') or insertedvar[5] not in ('0', '1') or insertedvar[6] not in ('0', '1'):
        del int1, int2, int3, int4, int5, int6, int7
        checkinghammingpar()
        return
    else:
        pass
    int1 = int(insertedvar[6])
    int2 = int(insertedvar[5])
    int3 = int(insertedvar[4])
    int4 = int(insertedvar[3])
    int5 = int(insertedvar[2])
    int6 = int(insertedvar[1])
    int7 = int(insertedvar[0])

    # checks
    downcheck = int1 ^ int3 ^ int5 ^ int7
    midcheck = int2 ^ int3 ^ int6 ^ int7
    upcheck = int4 ^ int5 ^ int6 ^ int7
    #concatenation so we can add each number and instantly convert it to int later
    downcheckinstr = str(downcheck)
    midcheckinstr = str(midcheck)
    upcheckinstr = str(upcheck)
    totalcheckinstr = upcheckinstr + midcheckinstr + downcheckinstr

    #real check now
    
    if totalcheckinstr == binary1:
        if int1 == 1:
            int1 = 0
        else:
            int1 = 1

    if totalcheckinstr == binary2:
        if int2 == 1:
            int2 = 0
        else:
            int2 = 1

    if totalcheckinstr == binary3:
        if int3 == 1:
            int3 = 0
        else:
            int3 = 1

    if totalcheckinstr == binary4:
        if int4 == 1:
            int4 = 0
        else:
            int4 = 1

    if totalcheckinstr == binary5:
        if int5 == 1:
            int5 = 0
        else:
            int5 = 1

    if totalcheckinstr == binary6:
        if int6 == 1:
            int6 = 0
        else:
            int6 = 1

    if totalcheckinstr == binary0:
        print("No errors in this Hamming7-4 code!")
        askagain()
    else:
        var1 = str(int1)
        var2 = str(int2)
        var3 = str(int3)
        var4 = str(int4)
        var5 = str(int5)
        var6 = str(int6)
        var7 = str(int7)
        newhamming = (f"Corrected Hamming(7,4): {var7}{var6}{var5}{var4}{var3}{var2}{var1}\n\n")
        infobits = (f"4 Digit Information bits: {var7}{var6}{var5}{var3}\n\n")
        print(f"{newhamming}\n{infobits}")
        del int1, int2, int3, int4, int5, int6, int7
        del var1 , var2, var3, var4, var5, var6, var7
        del binary0, binary1, binary2, binary3, binary4, binary5, binary6, binary7
        del downcheck, midcheck, upcheck, downcheckinstr, midcheckinstr, upcheckinstr, totalcheckinstr, insertedvar, localcounter
        askagain()

def paridadpar():
    bit1uno = False
    bit2uno = False
    bit3uno = False
    bit4uno = False
    bit5uno = False
    bit6uno = False
    bit7uno = False
    var1 = ("")
    var2 = ("")
    var3 = ("")
    var4 = ("")
    var5 = ("")
    var6 = ("")
    var7 = ("")
    int1 = 0
    int2 = 0
    int3 = 0
    int4 = 0
    int5 = 0
    int6 = 0
    int7 = 0
    sumatorioprimerbitparidad = 0
    sumatoriosegundobitparidad = 0
    sumatoriotercerobitparidad = 0
    insertedvar = input("Introduce a four digits binary number: ")
    localcounter = len(insertedvar)
    if localcounter > 4 or localcounter < 4 or insertedvar.isdigit() == False or insertedvar[0] not in ('0', '1') or insertedvar[1] not in ('0', '1') or insertedvar[2] not in ('0', '1') or insertedvar[3] not in ('0', '1'):
        del bit1uno, bit2uno, bit3uno, bit4uno, bit5uno, bit6uno, bit7uno
        del insertedvar, localcounter, var1, var2, var3, var4, var5, var6, var7
        del int1, int2, int3, int4, int5, int6, int7
        paridadpar()
        return
    else:
        pass
    # bit one manages 1,3,5,7
    # bit two manages 2,3,6,7
    # bit three manages 4,5,6,7
    
    var7 = insertedvar[0]
    var6 = insertedvar[1]
    var5 = insertedvar[2]
    var3 = insertedvar[3]
    int7 = int(var7)
    int6 = int(var6)
    int5 = int(var5)
    int3 = int(var3)
    # first bit check
    sumatorioprimerbitparidad = int1 + int3 + int5 + int7
    if sumatorioprimerbitparidad % 2 != 0:
        int1 = 1
    else:
        int1 = 0
    # second bit check
    sumatoriosegundobitparidad = int2 + int3 + int6 + int7
    if sumatoriosegundobitparidad % 2 != 0:
        int2 = 1
    else:
        int2 = 0
    # third bit check
    sumatoriotercerobitparidad = int4 + int5 + int6 + int7
    if sumatoriotercerobitparidad % 2 != 0:
        int4 = 1
    else:
        int4 = 0

    var1 = str(int1)
    var2 = str(int2)
    var4 = str(int4)
    
    newhamming = (f"Hamming(7,4): {var7}{var6}{var5}{var4}{var3}{var2}{var1}\n\n")
    print(newhamming)
    del bit1uno, bit2uno, bit3uno, bit4uno, bit5uno, bit6uno, bit7uno
    del insertedvar, localcounter, var1, var2, var3, var4, var5, var6, var7
    del int1, int2, int3, int4, int5, int6, int7
    askagain()
    
def paridadimpar():
    global insertedvar
    bit1uno = False
    bit2uno = False
    bit3uno = False
    bit4uno = False
    bit5uno = False
    bit6uno = False
    bit7uno = False
    var1 = ("")
    var2 = ("")
    var3 = ("")
    var4 = ("")
    var5 = ("")
    var6 = ("")
    var7 = ("")
    int1 = 0
    int2 = 0
    int3 = 0
    int4 = 0
    int5 = 0
    int6 = 0
    int7 = 0
    sumatorioprimerbitparidad = 0
    sumatoriosegundobitparidad = 0
    sumatoriotercerobitparidad = 0
    insertedvar = input("Introduce a four digits binary number: ")
    localcounter = len(insertedvar)
    if localcounter > 4 or localcounter < 4 or insertedvar.isdigit() == False or insertedvar[0] not in ('0', '1') or insertedvar[1] not in ('0', '1') or insertedvar[2] not in ('0', '1') or insertedvar[3] not in ('0', '1'):
        del bit1uno, bit2uno, bit3uno, bit4uno, bit5uno, bit6uno, bit7uno
        del insertedvar, localcounter, var1, var2, var3, var4, var5, var6, var7
        del int1, int2, int3, int4, int5, int6, int7
        paridadimpar()
        return
    else:
        pass
    # bit one manages 1,3,5,7
    # bit two manages 2,3,6,7
    # bit three manages 4,5,6,7
    
    var7 = insertedvar[0]
    var6 = insertedvar[1]
    var5 = insertedvar[2]
    var3 = insertedvar[3]
    int7 = int(var7)
    int6 = int(var6)
    int5 = int(var5)
    int3 = int(var3)
    # first bit check
    sumatorioprimerbitparidad = int1 + int3 + int5 + int7
    if sumatorioprimerbitparidad % 2 == 0:
        int1 = 1
    else:
        int1 = 0
    # second bit check
    sumatoriosegundobitparidad = int2 + int3 + int6 + int7
    if sumatoriosegundobitparidad % 2 == 0:
        int2 = 1
    else:
        int2 = 0
    # third bit check
    sumatoriotercerobitparidad = int4 + int5 + int6 + int7
    if sumatoriotercerobitparidad % 2 == 0:
        int4 = 1
    else:
        int4 = 0

    var1 = str(int1)
    var2 = str(int2)
    var4 = str(int4)
    
    newhamming = (f"Hamming(7,4): {var7}{var6}{var5}{var4}{var3}{var2}{var1}\n\n")
    print(newhamming)
    del bit1uno, bit2uno, bit3uno, bit4uno, bit5uno, bit6uno, bit7uno
    del insertedvar, localcounter, var1, var2, var3, var4, var5, var6, var7
    del int1, int2, int3, int4, int5, int6, int7
    askagain()

askagain()


    
