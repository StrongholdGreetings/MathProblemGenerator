import os,random,time,sys,platform 
from colorama import Fore, Back, Style, init, AnsiToWin32
null=""
appversion='v1.4.2'
if platform.system()=="Windows":
    clrscr='cls'
else:
    clrscr='clear'
def ResizeWindows():
    if platform.system()=='Windows':
        os.system("mode con cols=65 lines=32")
ResizeWindows()
try:
    try:
        import requests
    except ModuleNotFoundError:
        if platform.system()=='Windows':
            os.system('py -m pip install requests')
        else:
            os.system('pip install requests')
    try:
        from colorama import Fore, Back, Style, init, AnsiToWin32
    except ModuleNotFoundError:
        if platform.system()=='Windows':
            os.system('py -m pip install colorama')
        else:
            os.system('pip install colorama')
except KeyboardInterrupt:
    exit()
def TitlePrint():
    os.system(clrscr)
    print("")
    print("                 TRÌNH TẠO PHÉP TOÁN NGẪU NHIÊN")
    print("")
    print(f"{null:-<65}")
    print("")
def TaskComplete():
    TitlePrint()
    print("     Cài đặt được lưu thành công!")
    print("     Thay đổi sẽ được thiết lập khi bấm phím Enter")
    print("     Nhấn phím Enter để tiếp tục")
    print('')
    print(f"{null:-<65}")
    input()
RetryVerify=True
enable=True
rounding=3
btd=0
textstylechoice='a'
textshadechoice='a'
textcolorchoice='a'
bgcolorchoice='a'
bgshadechoice='a'
inputexpect=3108
try:
    def exitprogram():
        os.system(clrscr)
        global RetryVerify,settingsexit,confirmsettings,ainputexit,binputexit
        TitlePrint()
        print('                        Đang thoát...')
        print('')
        print(f'{null:-<65}')
        time.sleep(1)
        settingsexit=True
        confirmsettings=True
        ainputexit=True
        binputexit=True
        RetryVerify=False
    def FileVerify():
        global FileNotUsed,TextStyle,TextShade,TextColor,BGShade,BGColor,Negative,Fraction,RoundingError,errorlist,errorloop,UIError,inputexpect
        FileNotUsed=False
        errorloop=True
        TextStyle=0
        TextShade=0
        TextColor=0
        BGShade=0
        BGColor=0
        Negative=0
        Fraction=0
        RoundingError=0
        MathError=False
        UIError=False
        if os.path.isdir("Data")==False:
            os.mkdir("Data")
        try:
            a=open("Data/TextStyleSave.log","r")
            b=a.read()
            if b.title() not in ["Dim","Bright","Normal","Special"]:
                with open('Data/TextStyleSave.log','w') as a:
                    a.write("Normal")
                FileNotUsed=True
                TextStyle=1
                UIError=True
        except FileNotFoundError:
            with open('Data/TextStyleSave.log','w') as a:
                    a.write("Normal")
            FileNotUsed=True
            TextStyle=2
            UIError=True
        try:
            a=open("Data/TextShadeSave.log","r")
            b1=a.read()
            if b1.title() not in ["Light","Normal"]:
                with open('Data/TextShadeSave.log','w') as a:
                    a.write("Normal")
                FileNotUsed=True
                TextShade=1
                UIError=True
        except FileNotFoundError:
            with open('Data/TextShadeSave.log','w') as a:
                a.write("Normal")
            FileNotUsed=True
            TextShade=2
            UIError=True
        try:
            a=open("Data/TextColorSave.log","r")
            b2=a.read()
            if b2.title() not in ["White","Red","Black","Green","Yellow","Blue","Magenta","Cyan"]:
                with open('Data/TextColorSave.log','w') as a:
                    a.write("White")
                FileNotUsed=True
                TextColor=1
                UIError=True
        except FileNotFoundError:
            with open('Data/TextColorSave.log','w') as a:
                    a.write("White")
            FileNotUsed=True
            TextColor=2
            UIError=True
        try:
            a=open("Data/BGShadeSave.log","r")
            b3=a.read()
            if b3.title() not in ["Normal","Light"]:
                with open('Data/BGShadeSave.log','w') as a:
                    a.write("Normal")
                FileNotUsed=True
                BGShade=1
                UIError=True
        except FileNotFoundError:
            with open('Data/BGShadeSave.log','w') as a:
                    a.write("Normal")
            FileNotUsed=True
            BGShade=2
            UIError=True
        try:
            a=open("Data/BGColorSave.log","r")
            b4=a.read()
            if b4.title() not in ["White","Red","Black","Green","Yellow","Blue","Magenta","Cyan"]:
                with open('Data/BGColorSave.log','w') as a:
                    a.write("Black")
                FileNotUsed=True
                BGColor=1
                UIError=True
        except FileNotFoundError:
            with open('Data/BGColorSave.log','w') as a:
                    a.write("Black")
            FileNotUsed=True
            BGColor=2
            UIError=True
        try:
            a=open("Data/AllowNegativeResult.log","r")
            b5=a.read()
            if b5.title() not in ["True", "False"]:
                with open('Data/AllowNegativeResult.log','w') as a:
                    a.write("False")
                FileNotUsed=True
                Negative=1
                MathError=True
        except FileNotFoundError:
            with open('Data/AllowNegativeResult.log','w') as a:
                    a.write("False")
            FileNotUsed=True
            Negative=2
            MathError=True
        try:
            a=open("Data/AllowFractionResult.log","r")
            b6=a.read()
            if b5.title() not in ["True", "False"]:
                with open('Data/AllowFractionResult.log','w') as a:
                    a.write("False")
                Fraction=1
                MathError=True
        except FileNotFoundError:
            with open('Data/AllowFractionResult.log','w') as a:
                    a.write("False")
            FileNotUsed=True
            Fraction=2
            MathError=True
        try:
            a=open("Data/RoundingValue.log","r")
            b6=a.read()
            if b6 not in ["0","1","2","3","4","5"]:    
                with open('Data/RoundingValue.log','w') as a:
                    a.write("3")
                FileNotUsed=True
                RoundingError=1
                MathError=True
        except FileNotFoundError:
            with open('Data/RoundingValue.log','w') as a:
                    a.write("3")
            FileNotUsed=True
            RoundingError=3
            MathError=True
        if FileNotUsed==True:
            while errorloop==True:
                os.system(clrscr)
                print('')
                print("                       TRÌNH KIỂM TRA FILE")
                print('')
                print(f"{null:-<65}")
                print('')
                print("  Một số cài đặt của bạn đã bị chuyển về mặc định.")
                print("  Lý do: Không thể tìm thấy file log/Nội dung file không hợp lệ")
                print("  Tất cả file log bị mất hoặc thay đổi đã được phục hồi.")
                print('')
                print("     [0]: Tiếp tục chạy")
                print('')
                print("     [1]: Danh sách lỗi")
                print("")
                print(f"{null:-<65}")
                print("")
                errorlist=str(input(" Lựa chọn (0-1) -> "))
                try:
                    errorlist=int(errorlist)
                    if errorlist==1:
                        os.system(clrscr)
                        print('')
                        print("                       TRÌNH KIỂM TRA FILE")
                        print('')
                        print(f"{null:-<65}")
                        print('')
                        print("     DANH SÁCH LỖI:")
                        print("")
                        print("     * Giao Diện")
                        print('')
                        if UIError==True:
                            if TextStyle==1: #1
                                print("     - TextStyleSave.log: Nội dung tệp không hợp lệ")
                            elif TextStyle==2:
                                print("     - TextStyleSave.log: Bị di chuyển hoặc xóa đi")
                            else:
                                print("     - TextStyleSave.log: Không gặp vấn đề")
                            print('')
                            if TextShade==1: #2
                                print("     - TextShadeSave.log: Nội dung tệp không hợp lệ")
                            elif TextShade==2:
                                print("     - TextShadeSave.log: Bị di chuyển hoặc xóa đi")
                            else:
                                print("     - TextShadeSave.log: Không gặp vấn đề")
                            print('')
                            if TextColor==1: #3
                                print("     - TextColorSave.log: Nội dung tệp không hợp lệ")
                            elif TextColor==2:
                                print("     - TextColorSave.log: Bị di chuyển hoặc xóa đi")
                            else:
                                print("     - TextColorSave.log: Không gặp vấn đề")
                            print('')
                            if BGShade==1: #4
                                print("     - BGShadeSave.log: Nội dung tệp không hợp lệ")
                            elif BGShade==2:
                                print("     - BGShadeSave.log: Bị di chuyển hoặc xóa đi")
                            else:
                                print("     - BGShadeSave.log: Không gặp vấn đề")
                            print('')
                            if BGColor==1: #5
                                print("     - BGColorSave.log: Nội dung tệp không hợp lệ")
                            elif BGColor==2:
                                print("     - BGColorSave.log: Bị di chuyển hoặc xóa đi")
                            else:
                                print("     - BGColorSave.log: Không gặp vấn đề")
                            print('')
                        else:
                            print(" -Toàn bộ file liên quan đều không gặp vấn đề")
                            print('')
                        print("     * Toán Học")
                        print('')
                        if MathError==True:
                            if Negative==1: #6
                                print("     - AllowNegativeResult.log: Nội dung tệp không hợp lệ")
                            elif Negative==2:
                                print("     - AllowNegativeResult.log: Bị di chuyển hoặc xóa đi")
                            else:
                                print("     - AllowNegativeResult.log: Không gặp vấn đề")
                            print('')
                            if Fraction==1:
                                print("     - AllowFractionResult.log: Nội dung tệp không hợp lệ")
                            elif Fraction==2:
                                print("     - AllowFractionResult.log: Bị di chuyển hoặc xóa đi")
                            else:
                                print("     - AllowFractionResult.log: Không gặp vấn đề")
                            print('')
                            if RoundingError in [1,2]:
                                print("     - RoundingValue.log: Nội dung tệp không hợp lệ")
                            elif RoundingError==3:
                                print("     - RoundingValue.log: Bị di chuyển hoặc xóa đi")
                            else:
                                print("     - RoundingValue.log: Không gặp vấn đề")
                            print('')
                        else:
                            print("     - Toàn bộ file liên quan đều không gặp vấn đề")
                            print('')
                        print(f'{null:-<65}')
                        print("")
                        input("Nhấn phím Enter để tiếp tục chạy chương trình.")
                        errorloop=False
                    elif errorlist==0:
                        errorloop=False
                    else:
                        print(" Số vừa nhập không hợp lệ!")
                except ValueError:
                    print(" Lỗi cú pháp! Vui lòng nhập lại")
                    time.sleep(1)
        else:
            if inputexpect==6:
                os.system(clrscr)
                print('')
                print("                       TRÌNH KIỂM TRA FILE")
                print('')
                print(f"{null:-<65}")
                print('')
                print("              Tất cả các file đều không gặp vấn đề.")
                print("                  Nhấn phím Enter để quay lại.")
                print('')
                print(f'{null:-<65}')
                input()
    def ApplySettings():
        global textstyleviet,textshadeviet,textcolorviet,bgshadeviet,bgcolorviet,DKTru,DKTruDisplay
        if textstylechoice.title()=="Normal":
            print(Style.NORMAL)
            textstyleviet='Thường'
        elif textstylechoice.title()=="Dim":
            print(Style.NORMAL)
            print(Style.DIM)
            textstyleviet='Mờ'
        elif textstylechoice.title()=="Bright":
            print(Style.NORMAL)
            print(Style.BRIGHT)
            textstyleviet='Sáng'
        elif textstylechoice.title()=='Special':
            print(Style.DIM)
            print(Style.BRIGHT)
            textstyleviet='Đặc biệt'
        if textshadechoice.title()=='Light':
            textshadeviet='Nhạt'
            if textcolorchoice.title()=='Black':
                print(Fore.LIGHTBLACK_EX)
                textcolorviet='Đen'
            if textcolorchoice.title()=='Red':
                print(Fore.LIGHTRED_EX)
                textcolorviet='Đỏ'
            if textcolorchoice.title()=='Green':
                print(Fore.LIGHTGREEN_EX)
                textcolorviet='Xanh lục'
            if textcolorchoice.title()=='Yellow':
                print(Fore.LIGHTYELLOW_EX)
                textcolorviet='Vàng'
            if textcolorchoice.title()=='Blue':
                print(Fore.LIGHTBLUE_EX)
                textcolorviet='Xanh lam'
            if textcolorchoice.title()=='Magenta':
                print(Fore.LIGHTMAGENTA_EX)
                textcolorviet='Màu cánh sen'
            if textcolorchoice.title()=='Cyan':
                print(Fore.LIGHTCYAN_EX)
                textcolorviet='Xanh lơ'
            if textcolorchoice.title()=='White':
                print(Fore.LIGHTWHITE_EX)
                textcolorviet='Trắng'
        else:
            textshadeviet='Thường'
            if textcolorchoice.title()=='Black':
                print(Fore.BLACK)
                textcolorviet='Đen'
            if textcolorchoice.title()=='Red':
                print(Fore.RED)
                textcolorviet='Đỏ'
            if textcolorchoice.title()=='Green':
                print(Fore.GREEN)
                textcolorviet='Xanh lục'
            if textcolorchoice=='Yellow':
                print(Fore.YELLOW)
                textcolorviet='Vàng'
            if textcolorchoice.title()=='Blue':
                print(Fore.BLUE)
                textcolorviet='Xanh lam'
            if textcolorchoice=='Magenta':
                print(Fore.MAGENTA)
                textcolorviet='Màu cánh sen'
            if textcolorchoice.title()=='Cyan':
                print(Fore.CYAN)
                textcolorviet='Xanh lơ'
            if textcolorchoice.title()=='White':
                print(Fore.WHITE)
                textcolorviet='Trắng'
        if bgshadechoice.title()=='Light':
            bgshadeviet='Nhạt'
            if bgcolorchoice.title()=='Black':
                print(Back.LIGHTBLACK_EX)
                bgcolorviet='Đen'
            if bgcolorchoice.title()=='Red':
                print(Back.LIGHTRED_EX)
                bgcolorviet='Đỏ'
            if bgcolorchoice.title()=='Green':
                print(Back.LIGHTGREEN_EX)
                bgcolorviet='Xanh lục'
            if bgcolorchoice.title()=='Yellow':
                print(Back.LIGHTYELLOW_EX)
                bgcolorviet='Vàng'
            if bgcolorchoice.title()=='Blue':
                print(Back.LIGHTBLUE_EX)
                bgcolorviet='Xanh lam'
            if bgcolorchoice.title()=='Magenta':
                print(Back.LIGHTMAGENTA_EX)
                bgcolorviet='Màu cánh sen'
            if bgcolorchoice.title()=='Cyan':
                print(Back.LIGHTCYAN_EX)
                bgcolorviet='Xanh lơ'
            if bgcolorchoice.title()=='White':
                print(Back.LIGHTWHITE_EX)
                bgcolorviet='Trắng'
        else:
            bgshadeviet='Thường'
            if bgcolorchoice=='Black':
                print(Back.BLACK)
                bgcolorviet='Đen'
            if bgcolorchoice=='Red':
                print(Back.RED)
                bgcolorviet='Đỏ'
            if bgcolorchoice=='Green':
                print(Back.GREEN)
                bgcolorviet='Xanh lục'
            if bgcolorchoice=='Yellow':
                print(Back.YELLOW)
                bgcolorviet='Vàng'
            if bgcolorchoice=='Blue':
                print(Back.BLUE)
                bgcolorviet='Xanh lam'
            if bgcolorchoice=='Magenta':
                print(Back.MAGENTA)
                bgcolorviet='Màu cánh sen'
            if bgcolorchoice=='Cyan':
                print(Back.CYAN)
                bgcolorviet='Xanh lơ'
            if bgcolorchoice=='White':
                print(Back.WHITE)
                bgcolorviet='Trắng'
    def LogFileRead():
        global t1,t2,t3,bg1,bg2,m1,textstylechoice,textshadechoice,textcolorchoice,bgshadechoice,bgcolorchoice,DKTruNhap,DKthapphanNhap,roundtemp
        t1=open("Data/TextStyleSave.log","r")
        textstylechoice=t1.read()
        t2=open("Data/TextShadeSave.log","r")
        textshadechoice=t2.read()
        t3=open("Data/TextColorSave.log","r")
        textcolorchoice=t3.read()
        bg1=open("Data/BGShadeSave.log","r")
        bgshadechoice=bg1.read()
        bg2=open("Data/BGColorSave.log","r")
        bgcolorchoice=bg2.read()
        m1=open("Data/AllowNegativeResult.log","r")
        DKTruNhap=m1.read()
        m2=open("Data/AllowFractionResult.log","r")
        DKthapphanNhap=m2.read()
        m3=open("Data/RoundingValue.log","r")
        roundtemp=m3.read()
    def ColorMatchTest():
        global textcolorchoice
        global bgcolorchoice
        if textcolorchoice.title()==bgcolorchoice.title():
            os.system(clrscr)
            print('')
            print("                       TRÌNH KIỂM TRA FILE")
            print('')
            print(f'{null:-<65}')
            print('')
            print("              Phát hiện màu nền trùng với màu chữ!")
            print("     Cài đặt màu nền và màu chữ sẽ bị chuyển về mặc định.")
            print('')
            print(f'{null:-<65}')
            print('')
            input("Nhấn phím Enter để tiếp tục!")
            t3=open("Data/TextColorSave.log","w")
            t3.write("White")
            t3.close()
            t3=open("Data/TextColorSave.log","r")
            textcolorchoice=t3.read()
            bg2=open("Data/BGColorSave.log","w")
            bg2.write("Black")
            bg2.close()
            bg2=open("Data/BGColorSave.log","r")
            bgcolorchoice=bg2.read()
    def BundleTest():
        FileVerify()
        LogFileRead()
        ColorMatchTest()
        ApplySettings()
    def MathApply():
        global DKTru,DKthapphan,rounding
        if DKTruNhap=='False':
            DKTru="Tắt"
        else:
            DKTru="Bật"
        if DKthapphanNhap=='False':
            DKthapphan='Tắt'
        else:
            DKthapphan='Bật'
        rounding=int(roundtemp)
    def TotallyApplySettings():
        for i in range (0,3):
            ApplySettings()
            i+=1
            os.system(clrscr)
    def SetColorToDefault():
        global t1,t2,t3,bg1,bg2
        with open('Data/TextStyleSave.log','w') as t1:
            t1.write("Normal")
        with open('Data/TextShadeSave.log','w') as t2:
            t2.write("Normal")
        with open('Data/TextColorSave.log','w') as t3:
            t3.write("White")
        with open('Data/BGShadeSave.log','w') as bg1:
            bg1.write("Normal")
        with open('Data/BGColorSave.log','w') as bg2:
            bg2.write("Black")
    while RetryVerify==True:    
        ca=0
        nq=1
        BundleTest()
        MathApply()
        TotallyApplySettings()
        TitlePrint()
        print('     [0]: Thoát chương trình'),'\n' #2 tab
        print('')
        print('     [1]: Cộng')
        print('')
        print('     [2]: Trừ')
        print('')
        print('     [3]: Nhân')
        print('')
        print('     [4]: Chia')
        print('')
        print('     [5]: Cài đặt')
        print("")
        print(f'{null:-<65}')
        print('')
        pt=str(input(" Lựa chọn (0-5) -> "))
        settingsexit=False
        try:
            pt=int(pt)
            if pt not in [0,1,2,3,4,5]:
                print(' Số vừa nhập không hợp lệ!')
                time.sleep(1)
        except ValueError:
            print(' Lỗi cú pháp!')
            time.sleep(1)
        if pt==0:
            TitlePrint()
            print('     BẠN CÓ CHẮC CHẮN MUỐN THOÁT KHÔNG?')
            print("")
            print('     [0]: Không')
            print("")
            print('     [1]: Có')
            print('')
            print(f"{null:-<65}")
            print("")
            confirmexit=str(input(' Lựa chọn (0-1) ->  '))
            try:
                confirmexit=int(confirmexit)
                if confirmexit==1:
                    exitprogram() 
                    RetryVerify=False
                elif confirmexit not in [0,1]:
                    print(' Số vừa nhập không hợp lệ!')
                    time.sleep(1)
            except ValueError:
                print(' Lỗi cú pháp!')
                time.sleep(1)
        if pt==5:
            while settingsexit==False:
                TotallyApplySettings()
                TitlePrint()
                print('     CÀI ĐẶT:')
                print('')
                print('     [0]: Quay lại')
                print('')
                print('     [1]: Cài đặt giao diện')
                print('')
                print('     [2]: Cài đặt toán học')
                print('')
                print('     [3]: Xem cài đặt hiện tại')
                print('')
                print('     [4]: Thông tin phần mềm')
                print('')
                print('     [5]: Thông tin hệ thống')
                print('')
                print('     [6]: Kiểm tra file log')
                print('')
                print('     [7]: Cập nhật phần mềm (Beta)')
                print("")
                print(f'{null:-<65}')
                print('')
                inputexpect=str(input(' Lựa chọn (0-7) -> '))
                uisettingsexit=False
                mathsettingsexit=False
                viewsettingsexit=False
                mikuloop=True
                try:
                    inputexpect=int(inputexpect)
                    if inputexpect not in [0,1,2,3,4,5,6,7,31082007]: 
                        print(' Số vừa nhập không hợp lệ!')
                        time.sleep(1)
                except ValueError:
                    if inputexpect.lower() in ['3.141592654','3,141592654','pi']:
                        os.system(clrscr)
                        TitlePrint()
                        print('                3.141592653589793238462643383279  ')
                        print('              5028841971693993751058209749445923  ')
                        print('             07816406286208998628034825342117067  ')
                        print('             9821       48086      5132           ')
                        print('            823         06647     09384           ')
                        print('           46           0955      58223           ')
                        print('           17           25359     4081            ')
                        print('                        2848      1117            ')
                        print('                        4502      8410            ')
                        print('                        2701      9385            ')
                        print('                       21105     55964            ')
                        print('                       46229     48954            ')
                        print('                       9303      81964            ')
                        print('                       4288      10975            ')
                        print('                      66593      34461            ')
                        print('                     284756      48233            ')
                        print('                     78678       31652        71  ')
                        print('                    2019091      456485       66  ')
                        print('                   9234603        48610454326648  ')
                        print('                  2133936         0726024914127   ')
                        print('                  3724587          00660631558    ')
                        print('                  817488            152092096     ')
                        print('')
                        print("Nhấn phím Enter để quay lại cài đặt")
                        print('')
                        input(f"{null:-<65}")
                    elif inputexpect.title()=='Rickroll' or inputexpect.upper()=='WYNS2022ID':
                        os.system('start \"\" https://www.youtube.com/watch?v=dQw4w9WgXcQ')      
                    elif inputexpect.title()=='Python':
                        os.system(clrscr)
                        import this
                        print('')
                        print('Lưu ý:')
                        print('Do bản chất của nó là một câu lệnh import, nó chỉ dùng được 1 lần trên mỗi lần chạy chương trình')
                        input('Nhấn phím Enter để thoát.')
                    else:
                        print(' Lỗi cú pháp!')
                        time.sleep(1)
                if inputexpect==31082007:
                   while mikuloop:
                       os.system(clrscr)
                       print("")
                       print("                            MIKU ZONE")
                       print("")
                       print(f"{null:-<65}")
                       print('')
                       print("      MIKU ASCII:")
                       print('')
                       print('      [0]: Thoát')
                       print('')
                       print('      [1]: MIKU')
                       print('')
                       print('      [2]: MORE MORE JUMP!')
                       print("")
                       print(f'{null:-<65}')
                       print('')
                       mikuinput=str(input(' Lựa chọn (0-2) -> '))
                       try:
                           mikuinput=int(mikuinput)
                           if mikuinput==0:
                               mikuloop=False
                           elif mikuinput==1:
                               if platform.system()=='Windows':
                                   os.system("mode con cols=65 lines=43")
                               os.system(clrscr)
                               print('')
                               print("                  TRÌNH QUẢN LÝ EASTER EGG")
                               print('')
                               print(f"{null:-<65}")
                               print(null)
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⣴⠟⠋⢠⣴⣾⣿⡟⠋⠉⡳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠑⠒⠦⢤⣄⡀⠀⣴⡟⠋⡀⢠⣬⣿⣿⡿⠳⣄⠀⠀⠀⠀")#1
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⣴⣫⡾⠋⠀⣶⣿⢿⣿⣥⠄⠠⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣌⣩⣿⡯⠁⣬⣭⣽⣿⣿⡟⠁⠈⠉⠝⢦⠀⠀")#2
                               print("⠀⠀⠀⠀⠀⠀⠀⡼⣽⣟⡀⣠⣼⣿⣿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⠃⠀⢠⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠱⣄")#3
                               print("⠀⠀⠀⠀⠀⠀⠸⠃⠻⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣧⣀⣼⠘⣿⠿⣸⠏⠀⣄⠀⠀⠀⠀⠀⠀⠈")#4
                               print("⠀⠀⠀⠀⠀⠀⠇⠀⠀⠘⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⣿⣿⣏⠀⠀⠈⡄⠀⠀⠀⠀⠀⠀")#5
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠀⢀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⡝⠳⠀⢰⢱⡀⠀⠀⠀⠀⠀")#6
                               print("⠀⠀⠀⠀⠀⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⢠⣾⣇⠀⢸⠀⠀⠀⠀⠀⠀⠀⢱⢹⣷⠀⠀⠀⠀⠀⠰⡆⠉⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣷⡄⠀⠀⡏⡇⠀⠀⠀⠀⠀")#7
                               print("⠀⠀⠀⠀⠀⠀⢠⠞⠀⢀⡔⠀⠀⠀⠀⠀⢀⣿⡿⢹⠀⢸⠀⠀⠀⠀⠀⡀⠀⠘⣿⡿⣷⠀⠀⠀⠀⠀⠹⡀⠀⢳⡀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⡄⠀⢿⣻⠀⠀⠀⠀⠀")#8
                               print("⠀⠀⠀⠀⠀⠀⠀⡴⢣⡞⠀⠀⠀⠀⠀⢀⣾⡿⠁⢸⡇⢸⡇⠀⠀⠀⠀⣇⠀⠀⣿⠁⠙⣧⠀⠀⠀⠀⠀⢳⡀⠈⣇⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣆⢸⣟⠀⠀⠀⠀⠀")#9
                               print("⠀⠀⠀⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⣼⡿⣁⣘⣀⢧⠈⣿⠀⠀⠀⠀⠸⡄⠀⣸⣀⣀⣹⣷⡀⠀⠀⠀⠀⢧⠀⢸⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡿⣿⣿⢀⠀⠀⠀⠀")#10
                               print("⠀⠀⠀ ⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⣰⡿⠋⡽⠉⠉⠘⡆⣿⣧⠀⠀⠀⠀⢧⠀⣿⣿⠉⠉⠙⣯⡑⠒⠀⠀⠘⣧⠘⡇⠀⠀⠀⠀⠀⢿⠐⠂⣩⠏⠀⣿⢿⡜⠀⠀  ")#11
                               print("⠀⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⢰⣿⠃⣴⠁⠀⠀⠀⢻⣼⠹⡆⠀⠀⠀⢸⡇⣿⡟⠀⠀⠀⠈⢿⣄⠀⠀⠀⠙⡆⣷⠀⠀⠀⠀⠀⢸⣄⣠⣏⠀⢠⣿⡎⢧⣂⠀⠀⠀")#12
                               print("⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⣾⠏⢠⣀⣀⣀⡠⠄⠀⢿⣧⠹⡄⠀⠀⠀⣿⣿⣣⠀⠳⣄⠀⠀⠹⣧⡀⠀⠀⢻⢻⠀⠀⠀⠀⠀⠀⣿⣷⣾⣷⡾⣿⡇⠸⣿⠀⠀⠀")#13
                               print("⠀⠀⠀⠀⠀⢰⡇⠀⠀⠀⠀⠀⣸⣿⢀⣶⡿⠟⢛⣿⣷⣄⠈⣿⣆⠹⡄⠀⠀⢸⡇⣿⣀⣴⣾⠿⢿⣷⣮⣍⡀⠀⠀⣾⠀⡀⠀⠀⠀⠀⣿⡟⢻⠋⣻⣿⡇⠀⢿⡄⠀⠀")#14
                               print("⠀⠀⠀⠀⡀⡜⠀⠀⠀⠀⠀⠀⣿⣿⡿⠋⠀⠐⢻⣿⣿⣿⡀⠈⣿⣦⡙⣄⠀⠸⡇⢸⠛⠛⠀⠀⠠⣾⣿⣿⣿⣦⡀⢸⠀⡇⠀⠀⠀⠀⣿⣶⣾⣿⣿⣿⠃⠀⢸⡇⠀⠀")#15
                               print("⠀⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⢠⣿⡼⠃⠀⠀⣶⣾⣿⣿⣿⡇⠀⠈⢷⡙⢮⣀⠀⣿⠈⠄⠀⠀⢠⣤⣿⣿⣿⣿⣿⣿⣾⢲⡇⠀⠀⠀⠀⡿⣿⣿⣿⣿⡟⠀⠀⢸⣷⠀⠀")#16
                               print("⠀⠀⠀⣤⡇⢰⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀⠀⢻⡿⣿⣷⢿⠇⠀⠀⠀⠳⡄⠈⠳⢼⡀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡟⢸⡏⣼⠁⠀⠀⢀⡶⣷⣿⣿⣿⣿⠃⠀⠀⠀⣿⠀⠀")#17
                               print("⠀⠀⢰⣻⠀⢸⡇⠀⠀⠀⠀⣼⣿⣿⡄⠀⠀⠘⢧⣀⣰⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠤⠀⣹⠁⢠⣣⠇⠀⠀⠀⢸⡇⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⠀⠀")#18
                               print("⠀⠀⡄⠀⠀⢸⣇⠀⢀⠀⠀⣷⣿⡿⢿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠒⠚⠃⠀⣸⡿⠀⠀⠀⠀⢸⡇⣿⣿⣿⣿⣿⠀⠀⠀⠀⣿⠀⠀")#19
                               print("⠀⢰⠁⠀⠀⠀⣿⡄⠘⢦⠀⣿⡫⠐⣺⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠘⠀⠀")#20
                               print("⠀⢸⠀⠀⠀⣷⣹⣷⠀⠈⡾⠋⠀⠀⣿⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⢹⡇⣼⠀⠀⠀⠀⣼⣿⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")#21
                               print("⠀⠈⠁⠀⠀⠀⢷⡻⢧⡞⠁⠉⠉⠭⣅⣈⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⣼⣸⠃⠀⠀⠀⢀⣿⡏⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")#22
                               print("⠀⠀⠀⠀⠀⠀⠀⠁⠀⣿⣄⠀⠀⠀⠀⠈⠙⠳⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣷⡇⠀⠀⠀⡀⢸⡿⠀⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")#23
                               print("⡄⠀⠀⠀⠀⠀⠀⠀⠀⡟⢸⡷⣄⠀⠀⠀⠀⠀⠀⠉⠢⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⣾⠙⣿⠁⠀⠀⢠⡇⣾⣷⣼⠥⠤⠤⣤⣄⣀⡀⠀⠀⠀⠀⠀")#24
                               print("⡀⠀⠀⠀⠀⠀⠀⠀⢠⡇⣿⡇⣿⣳⣄⠀⠀⠀⠀⠀⠀⠈⠑⣦⣄⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⠒⠋⣀⡾⠃⢠⡏⠀⠀⢠⣿⣿⣯⣿⡏⢀⡔⠋⠁⠀⠈⠉⠲⡄⠀⠀⠀")#25
                               print("⡇⠀⠀⠀⠀⠀⠀⠀⢸⡇⣿⣷⢸⣿⣿⡷⢤⠀⠀⠀⠀⠀⠀⠈⢻⣓⢦⣀⣀⣤⠶⠚⠉⠀⢀⡠⠞⠁⠀⢀⡾⠀⠀⢀⣾⣯⢿⣿⠋⠰⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")#26
                               print("⡃⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⣹⣯⣿⠃⢧⠀⡷⡄⠀⠀⠀⠀⠀⠀⢡⡿⠛⢙⣿⣦⣠⠴⠚⠉⠀⠀⢀⣠⡿⠁⠀⣠⣾⣯⡽⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")#27
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⡇⠈⠻⡆⠀⡾⠁⠀⠀⠀⠀⠀⠀⢀⣾⣧⠴⢺⣿⡉⠀⠀⠀⠀⢀⣤⢾⡟⠁⢀⣴⠟⠉⠁⢸⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")#28
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⡼⠀⠀⠀⢀⡼⠁⠀⠀⠀⠀⠀⠀⠀⣼⠋⠀⠀⠀⡝⢷⠀⢀⡤⠖⠋⣀⣮⠴⠚⠋⠁⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")#29
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⠀⠀⢠⠞⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⢀⣼⣧⠈⡗⣿⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⡾⠁⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")#31
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⠀⣠⣶⠃⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⠀⠀⢠⣾⠉⢸⢷⣼⣿⡇⠀⠀⠀⢀⡠⠊⠀⠀⠀⡼⠁⢰⠟⢹⡗⢶⣶⡶⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")#31
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⡼⠀⣰⣿⢿⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡇⠀⣰⠟⢹⠀⠀⠈⡽⠛⢷⡀⠀⠀⠁⠀⠀⠀⠀⣸⠁⢠⣾⠀⣼⠃⢠⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")#34
                               print("⠀⠀⠀⠀⠀⠀⠀⢀⣧⣾⣏⢹⣿⠀⠀⠀⠀⠀⠀⠀⡸⠋⢰⡁⢰⠏⣰⣿⠀⠀⣼⣧⡴⠛⣿⠀⠀⠀⠀⠀⢀⡼⠃⠀⠘⢿⣿⣃⣀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")#33
                               print("")
                               print(f'{null:-<65}')
                               print(null)
                               input("Nhấn phím Enter để quay lại")
                               ResizeWindows()
                           elif mikuinput==2:
                               if platform.system()=="Windows":
                                    os.system("mode con cols=65 lines=43")
                               os.system(clrscr)
                               print(null)
                               print("                  TRÌNH QUẢN LÝ EASTER EGG")
                               print(null)
                               print(f"{null:-<65}")
                               print(null)
                               print("⠀⠀⢀⡀⠄⠀⠒⠀⠈⠉⠀⠐⠂⢤⡤⠀⠀⠀⢀⣾⡷⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡀⠀⢧⠀⠀⠉⣧⠀⠉⢧⡀⠀⠈⠈⠙⢿⣿⣿⣄⣤⢟⡂⠀⠀⠀⠀⠀⠱⣀")#1
                               print("⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡞⠀⠀⠀⢀⡾⡿⢁⡟⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⡇⠀⠘⣧⠀⠀⢿⡆⠀⢈⢷⡀⠀⠀⠀⠈⢻⣿⣿⣄⡾⢇⠀⠀⠀⠀⢀⣠⠧⠁")#2
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⣼⣿⠁⢸⠀⠀⣴⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣆⠀⠈⣇⠀⠈⢿⣧⠀⠀⠰⣦⠈⢿⣏⠻⣄⣼⣷⠀⠤⣠⠁⠀⢄⠀")#3
                               print("⠀⠐⡀⠀⠀⠀⠀⠀⢀⣤⢶⡏⠀⠀⠀⢀⣰⣿⠇⠀⢸⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠹⡄⠀⢻⡄⠀⠈⣿⣆⠀⠀⠈⠻⣌⣿⡷⠿⣿⣿⠇⠀⢻⡆⠀⠈⢣")#4
                               print("⠀⠀⢃⠀⠀⠀⠀⠀⠈⠀⣸⢁⡆⠀⣠⠏⣿⡏⠀⠀⣼⠀⠀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢸⠀⢧⠀⢸⠻⣄⠀⠘⣿⡄⠀⠀⣄⠈⠻⡆⠀⣨⣧⡀⠀⠀⠀⠀⠀⠀")#5
                               print("⠀⠀⠈⡄⠀⠀⠀⠀⠀⠀⡿⡼⠀⢰⠏⠀⣿⠃⠀⢰⡿⡄⠀⣿⣧⢠⡀⠸⠀⠀⠀⠀⠀⠀⠀⢸⣀⣤⣾⠒⢺⠀⡾⠂⠬⢷⡄⠈⣿⡄⠀⢹⣧⡀⠙⣾⣿⣿⠟⠀⠀⠀⠁⠀⢠")#6
                               print("⠀⠀⠀⡜⢆⠀⠀⠀⠀⢠⢿⠃⢠⡏⠀⢸⣿⠀⠀⡾⠀⣧⠀⣯⢸⡀⣇⠀⠀⠀⠀⠀⠀⠀⠀⣾⠉⢀⡟⠀⢸⣄⡇⠀⠀⠀⠹⣆⢸⣷⠀⠸⣿⢳⣄⠘⢮⣧⡀⠀⡀⠢⡀⢊")#7
                               print("⠀⠀⠀⠀⠈⠳⣄⠀⠀⢸⣼⠀⡿⠀⠀⢸⡿⠀⢀⡇⠀⢸⣦⣿⠛⣿⡿⣇⠀⠀⠀⠀⢸⠀⢰⡿⠀⡾⠁⠀⢸⡿⠀⠀⠀⣀⠀⠘⣾⡏⣆⠀⡿⡆⢹⣦⠈⣿⠟⠻⡃⣴⡧⠊⠀")#8
                               print("⠀⠀⢰⠀⠀⠀⠈⠻⣆⣆⢿⣼⠃⠀⡄⡾⡇⠀⢸⣧⠞⠉⠻⣻⡀⠘⣗⠘⣆⢀⠀⠀⣾⢀⡟⡇⣸⠃⠔⣯⣾⣿⣛⣛⠿⢿⣶⣤⣼⣿⠹⠀⠀⣷⢸⠟⢧⢸⣇⠀⠀⠀⢹⡄⠀")#9
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣼⣿⠀⢠⠃⡇⠉⠠⣿⠃⠀⠀⠀⠙⣧⡠⢘⣃⡸⣾⠀⣠⣏⡾⣹⡿⠃⠀⡸⠿⢿⣿⠿⣿⣶⣄⠈⢻⣿⢻⠀⡆⠀⢸⣾⠀⠘⣆⣿⠀⠀⠀⠀⢧⠀")#10
                               print("⠀⠀⡀⠀⠐⠀⠀⠀⠀⢸⡀⡿⠀⢸⠀⣧⠀⠀⢹⠀⠀⢀⣤⣶⣶⣖⣲⣶⣄⣹⡴⣻⡟⠵⠋⠀⠀⠀⠀⢻⣾⣿⣶⣿⠟⢻⠀⠀⡟⢸⠀⡇⠀⢸⣿⡄⠀⢻⠿⡆⠀⠀⢠⠈⠀")#11
                               print("⠀⢀⠁⠀⠀⠀⠀⠀⠀⠀⢳⡇⠀⣾⠀⣿⡄⠀⢸⠀⢸⣿⠿⣧⣿⣿⠿⣿⣾⡏⠀⠟⠀⠀⠀⠀⠀⠀⠀⠘⣎⠙⠛⠋⢀⡾⠀⠀⠀⢸⠀⠇⠀⠀⡇⡇⠀⠛⠀⢷⠀⠀⠈⠂⠀")#12
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⡟⠀⢏⢷⠀⢸⣶⣿⠋⠀⣉⣿⣿⣦⣾⣛⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠓⠒⠒⠚⠐⠋⠀⠘⡿⠀⠀⠀⠀⣷⡇⠀⠀⠀⠘⠀⠀⢠⠀⠀")#13
                               print("⠀⠂⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⡇⠀⠈⠈⢧⠈⡿⣿⠀⠀⢿⣻⡛⠟⠛⢺⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠇⣀⢸⠀⢰⡟⡇⠀⠀⠀⠀⠀⠀⠸⠀⢀")#14
                               print("⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⣿⡀⠀⠀⠘⣷⣳⡈⠀⠀⠀⠙⢲⡶⠚⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣴⡟⣸⠀⢸⠇⡇⠀⠀⠀⠀⡆⠀⠀⠃⠀")#15
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⢹⠀⡏⢷⣴⡀⠘⡏⢻⣷⡄⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⣀⣤⡤⠖⠒⠒⠒⠶⣄⠀⠀⠀⠀⢠⡾⠋⣸⣽⣿⠀⡿⠀⡇⠀⠀⠀⠀⠇⠀⠀⠀⠀")#16
                               print("⠆⠀⠀⠀⠄⠀⠀⠀⠈⠀⠀⠀⣷⡇⠀⢿⡇⢀⣷⠤⢹⣿⠆⠀⠀⠀⠀⠀⠀⠀⢀⣶⠋⣩⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀⢠⡿⠁⡏⣼⠃⠀⡇⠀⠀⠀⠀⠀⠀⠀⢀⠀")#17
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠋⠻⠦⠀⣧⠘⣿⣶⣼⢿⣧⠀⠀⠀⠀⠀⠀⠀⠀⢿⠛⠁⠀⠀⠀⠀⠀⠀⢀⡟⠀⠀⠀⠀⠀⢠⡟⠀⣰⣿⣫⠀⠀⡇⠀⠀⠀⠀⠀⢀⠀⠸⠀")#18
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⢻⡀⣿⣿⡻⣾⠛⢷⡄⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⢀⣠⠞⠀⠀⠀⠀⣠⠴⠋⠀⠠⠟⢹⢻⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀")#19
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⢧⢹⠈⠛⠚⠀⠈⠻⣤⡀⠀⠀⠀⠀⠀⠀⠈⠙⠒⠒⠚⠉⠁⠀⠀⢀⣠⡞⠋⠀⠀⠀⠀⠀⣿⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")#20
                               print("⠀⠀⠀⠀⠀⠀⠀⠀⡼⠃⠀⠀⠀⠀⠀⠀⠀⠈⢿⣇⠀⠀⠀⠀⠀⠀⠉⠓⠶⢤⣤⣀⣀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠋⣿⣄⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⡇⠀⠀")#21
                               print("⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⣿⠉⠉⠓⠒⠶⠖⠋⠁⠀⠀⣿⠸⣆⠀⠀⠀⠀⢸⠃⠀⠀⠸⠀⠀⠀⠀⠀⠃⠀⡇⠀⢀")#22
                               print("⠀⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣼⠇⣹⡀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡟⠀⠹⣷⣤⡀⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀")#23
                               print("⠀⠀⠀⠀⠜⠁⠀⠀⠀⠀⠀⣠⠾⠿⠿⠒⠒⠒⠲⢤⣄⣀⣀⣀⣀⣠⣤⣶⣿⡿⠃⠀⠙⢧⡀⠀⠀⠀⠀⠀⣀⣾⠏⠀⠀⠀⠹⣿⣿⣶⣅⠀⠀⠀⠆⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀")#24
                               print("⠀⠀⠠⠂⠀⠀⠀⢀⣤⣴⡋⠁⠀⠀⠀⠀⠀⠢⠀⠀⣼⣿⣽⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠙⠲⣤⣤⣦⠞⠋⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣶⣴⣤⣄⣀⠀⠀⠃⠀⠀⠂⠢⠐")#25
                               print("⠀⡰⠁⠀⠀⠀⢀⣸⣮⣁⣈⠉⠛⠒⠲⠦⢤⡤⣄⣼⢿⣿⣿⣿⣿⣿⣿⣿⡗⠀⣀⡀⠀⠀⠀⢀⣤⣥⣄⠀⠀⠀⠀⠀⠀⠀⢈⡏⣿⡌⡉⣻⣿⣿⣿⣿⡟⢦⠀⠀⠀⠀⠀⠀⠀")#26
                               print("⣼⡁⠴⠖⠋⠉⠉⠀⣀⡤⠘⠉⢑⡶⠒⠒⠺⠧⠀⢸⠀⣿⣿⣿⣦⣴⣼⣿⡇⠀⠀⠀⠀⣠⠞⠁⢀⣿⡌⠳⣄⠀⠀⠀⠀⠀⢸⠇⢻⣿⣿⣿⣿⣿⣿⣿⡇⣼⢶⠀⠀⠀⠀⠀⠀")#27
                               print("⠳⢄⠀⠀⠀⠀⣠⠞⠉⠀⢀⡴⠋⠀⣀⣠⠤⠤⣤⢼⠀⢻⣿⣿⣿⡟⢛⡇⢸⠀⢀⡠⠚⠁⠀⢀⡞⠃⠻⣄⠈⠳⣄⠀⠀⠀⡏⠀⢸⡿⣿⣿⣿⣿⣿⣿⡞⠛⠛⠒⠲⣶⣂⠈⠁")#28
                               print("⠀⠈⠳⡀⢠⡞⠁⠀⠀⣠⠋⢠⠖⠋⢉⣡⠤⠤⣤⡤⠴⣛⣻⡋⠉⢹⣿⠃⠘⠷⠋⠀⣤⣴⣲⡯⠴⠓⠒⠈⠕⢲⣼⡷⣄⡼⠁⠀⢸⣷⡏⠉⢩⣭⣍⡉⠉⣽⠛⠻⣷⣦⡌⠳⠀")#29
                               print("⢢⠀⠀⡿⠋⠀⠀⢀⡼⠃⢰⠏⢈⣾⣿⢛⡷⠺⢧⣄⣰⠟⠈⠛⢶⡾⣿⠀⠀⠀⠀⠀⠉⠙⠳⢦⣤⠀⣿⡷⠖⠋⠉⠀⠀⠀⠀⠀⠘⢸⣧⣤⠏⠀⠈⠛⢾⠁⠀⠀⠀⣩⡜⠀⠀")#31
                               print("⠒⠁⠀⢧⣄⠀⠀⣼⣁⠀⢸⠀⢸⠙⢿⡟⠁⠀⠀⢹⣇⡀⠀⠀⣰⢿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⡆⣻⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⢀⡷⣄⠀⠀⣰⢿⢷⣦⡀⣄⣐⣻⣷⠀")#31
                               print("⠀⠀⠀⠀⠈⠉⣹⠃⠈⠛⢿⡆⣸⢀⣼⣷⣦⣀⣰⡟⡁⠙⡷⠾⣇⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠈⣽⠛⠿⣿⣿⠟⠀⠈⠻⠿⠁⠀")#34
                               print("⠀⠀⢄⣀⡀⣰⠃⠀⠀⠀⢈⡇⠙⡿⣿⣿⣿⠋⠈⠻⢿⡟⠁⠀⠀⢙⡟⠛⠓⠲⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠤⠄⠀⢺⠉⠻⡞⠁⠀⠀⢈⣿⣄⡀⠀⣠⣿⣶⠀")#33
                               print("")
                               print(f'{null:-<65}')
                               print(null)
                               input("Nhấn phím Enter để quay lại")
                               ResizeWindows()
                           else:
                               print(' Số vừa nhập không hợp lệ!')
                               time.sleep(1)
                       except ValueError:
                           if mikuinput.title()=='Mannequin':
                            os.system('start \"\" https://www.youtube.com/watch?v=Q1_vm1TwYyU')
                           else:
                            print(' Lỗi cú pháp!')
                            time.sleep(1)
                if inputexpect==7:
                    os.system(clrscr)
                    TitlePrint()
                    print("                       CẬP NHẬT PHẦN MỀM:")
                    print("")
                    print('                    Đang kiểm tra cập nhật...')
                    print('')
                    print(f"{null:-<65}")
                    time.sleep(1)
                    try:
                        response = requests.get("https://api.github.com/repos/StrongholdGreetings/MathProblemGenerator_Vietnamese/releases/latest")
                        latest=response.json()["name"]
                        if appversion>=latest:
                            os.system(clrscr)
                            TitlePrint()
                            print('                       CẬP NHẬT PHẦN MỀM:')
                            print('')
                            print('             Ứng dụng này đang ở phiên bản mới nhất!')
                            print('')
                            print(f'                   Phiên bản hiện tại: {appversion}')
                            print('')
                            print('                    Nhấn phím Enter để thoát.')
                            print('')
                            input(f'{null:-<65}')
                        elif appversion<latest:
                            os.system(clrscr)
                            TitlePrint()
                            print('     CẬP NHẬT PHẦN MỀM:')
                            print('')
                            print('     Ứng dụng này hiện có bản cập nhật mới!')
                            print('')
                            print(f'     Phiên bản hiện tại: {appversion}')
                            print('')
                            print(f'     Phiên bản mới nhất: {latest}')
                            print('')
                            print('     Bạn có muốn cài đặt bây giờ không?')
                            print('')
                            print('     [0]: Không (Quay lại)')
                            print('')
                            print('     [1]: Có')
                            print('')
                            print(' * Lưu ý: Sau khi tải xong, nó sẽ ở chung thư mục của phiên bản')
                            print(' hiện tại.')
                            print(f'{null:-<65}')
                            print('')
                            updatechoice=str(input(" Lựa chọn (0-1) -> "))
                            try:
                                updatechoice=int(updatechoice)
                                if updatechoice not in [0,1]:
                                    print(' Số vừa nhập không hợp lệ!')
                                    time.sleep(1)
                            except ValueError:
                                print(' Lỗi cú pháp!')
                                time.sleep(1)
                            if updatechoice==1:
                                updatedir=f'MathProblemGenerator {latest}.exe'
                                os.system(clrscr)
                                TitlePrint()
                                print('                       CẬP NHẬT PHẦN MỀM')       
                                print('')
                                print('                           Đang tải...')
                                print('')
                                print('              Việc này sẽ chỉ mất vài giây thôi...')                           
                                print('')
                                print(f'{null:-<65}')
                                url = f'https://github.com/StrongholdGreetings/MathProblemGenerator_Vietnamese/releases/download/Math/MathProblemGenerator.exe'
                                response = requests.get(url)
                                with open(updatedir, 'wb') as tempdown:
                                    tempdown.write(response.content)
                                TitlePrint()
                                print('                       CẬP NHẬT PHẦN MỀM')
                                print('')
                                print('                    Tải xuống thành công!!!')
                                print()
                                print(f'{null:-<65}')
                                time.sleep(1)
                    except requests.exceptions.RequestException:
                        os.system(clrscr)
                        TitlePrint()
                        print('                       CẬP NHẬT PHẦN MỀM:')
                        print('')
                        print("           Hình như PC này chưa kết nối đến Internet!")
                        print("")
                        print("           Hãy kết nối PC này vào Internet và thử lại!")
                        print('')
                        print('            Bây giờ thì hãy nhấn phím Enter để thoát')
                        print('')
                        input(f'{null:-<65}')
                if inputexpect==0:
                    settingsexit=True
                if inputexpect==6:
                    FileVerify()
                if inputexpect==2:
                    while mathsettingsexit==False:
                        MathApply()
                        TitlePrint()
                        print('     CÀI ĐẶT TOÁN HỌC:')
                        print(null)
                        print('     [0]: Thoát')
                        print('')
                        print('     [1]: Phép cộng')
                        print('')
                        print('     [2]: Phép trừ')
                        print('')
                        print('     [3]: Phép nhân')
                        print('')
                        print('     [4]: Phép chia')
                        print("")
                        print(f'{null:-<65}')
                        print(null)
                        mathsettingsinput=str(input(' Lựa chọn (0-4) -> '))
                        try:
                            mathsettingsinput=int(mathsettingsinput)
                            if mathsettingsinput not in [0,1,2,3,4]:
                                print(' Số vừa nhập không hợp lệ!')
                                time.sleep(1)
                        except ValueError:
                            print(' Lỗi cú pháp!')
                            time.sleep(1)
                        if mathsettingsinput==0:
                            mathsettingsexit=True
                        elif mathsettingsinput in [1,3]:
                            TitlePrint()
                            print('     Hiện tại tính năng này chưa có gì để chỉnh sửa.')
                            print("     Nhấn phím Enter để quay lại.")
                            print('')
                            print(f'{null:-<65}')
                            print('')
                            input()
                        elif mathsettingsinput==4:
                            divisionexit=False
                            while divisionexit==False:
                                FileVerify()
                                MathApply()
                                TitlePrint()
                                print('     CÀI ĐẶT PHÉP CHIA:')
                                print('')
                                print('     [0]: Quay lại')
                                print('')
                                print(f'     [1]: Cho phép kết quả thập phân ({DKthapphan})')
                                print('')
                                if DKthapphanNhap=="False":
                                    print(f'     [2]: Tùy chỉnh giá trị làm tròn (Tắt)')
                                else:
                                    print(f'     [2]: Tùy chỉnh giá trị làm tròn (Hiện tại: {rounding})')
                                print("")
                                print(f"{null:-<65}")
                                print("")
                                decimalloop=True
                                decimalacceptloop=True
                                divisioninput=str(input(' Lựa chọn (0-2) -> '))
                                try:
                                    divisioninput=int(divisioninput)
                                    if divisioninput not in [0,1,2]:
                                        print(' Số vừa nhập không hợp lệ!')
                                        time.sleep(1)
                                except ValueError:
                                    print(' Lỗi cú pháp!')
                                    time.sleep(1)
                                if divisioninput==0:
                                    divisionexit=True
                                elif divisioninput==1:
                                    while decimalacceptloop:
                                        FileVerify()
                                        TitlePrint()
                                        print('     CHO PHÉP KẾT QUẢ THẬP PHÂN?:')
                                        print('')
                                        print('     [0]: Quay lại')
                                        print('')
                                        print('     [1]: Bật')
                                        print('')
                                        print('     [2]: Tắt')
                                        print("")
                                        print(f'{null:-<65}')
                                        print("")
                                        allowfraction=str(input(' Lựa chọn (0-2) -> '))
                                        try:
                                            allowfraction=int(allowfraction)
                                            if allowfraction not in [0,1,2]:
                                                print(' Số vừa nhập không hợp lệ!')
                                                time.sleep(1)
                                        except ValueError:
                                            print(' Lỗi cú pháp!')
                                            time.sleep(1)
                                        if allowfraction==1:
                                            DKthapphanNhap='True'
                                        elif allowfraction==2:
                                            DKthapphanNhap='False'
                                        if allowfraction in [1,2]:    
                                            TaskComplete()
                                            with open("Data/AllowFractionResult.log","w") as m1:
                                                m1.write(DKthapphanNhap)
                                            decimalacceptloop=False
                                        elif allowfraction==0:
                                            decimalacceptloop=False
                                elif divisioninput==2:
                                    if DKthapphanNhap.title()=='False':
                                        TitlePrint()
                                        print('                   TRUY CẬP BỊ TỪ CHỐI!')    
                                        print('')
                                        print('  Bạn phải bật "cho phép kết quả thập phân" để thay đổi tùy chọn ')
                                        print('  này!')
                                        print('')
                                        print("  Nhấn phím Enter để quay lại.")
                                        print("")
                                        print(f"{null:-<65}")
                                        input()
                                    else:
                                        while decimalloop==True:
                                            TitlePrint()
                                            print('     THAY ĐỔI GIÁ TRỊ LÀM TRÒN:')
                                            print('')
                                            print('     [0]: Thoát')
                                            print('')
                                            print('     [1-5]: Vị trí làm tròn số thập phân')
                                            print("")
                                            print(f'{null:-<65}')
                                            print('')
                                            rounding=str(input(" Lựa chọn (0, 1-5) -> "))
                                            try:
                                                rounding=int(rounding)
                                                if rounding not in [0,1,2,3,4,5]:
                                                    if rounding<0:
                                                        print(" Số không hợp lệ! Vui lòng thử lại")
                                                        time.sleep(1)
                                                    elif rounding>5:
                                                        print(" Giá trị vượt quá giới hạn (Giá trị phải nhỏ hơn/bằng 5)")
                                                        time.sleep(1)
                                            except ValueError:
                                                print(' Lỗi cú pháp!')
                                                time.sleep(1)
                                            if rounding in [1,2,3,4,5]:
                                                roundtemp=str(rounding)
                                                TaskComplete()
                                                with open("Data/RoundingValue.log","w") as m1:
                                                    m1.write(roundtemp)
                                                decimalloop=False
                                            elif rounding==0:
                                                decimalloop=False
                        elif mathsettingsinput==2:
                            subtractionexit=False
                            while subtractionexit==False:
                                MathApply()
                                os.system(clrscr)
                                TitlePrint()
                                print('     CÀI ĐẶT PHÉP TRỪ:')
                                print('')
                                print('     [0]: Quay lại')
                                print('')
                                print(f'     [1]: Cho phép kết quả âm ({DKTru})')
                                print('')
                                print(f"{null:-<65}")
                                print('')
                                subtractioninput=str(input(" Lựa chọn (0-1) -> "))
                                try:
                                    subtractioninput=int(subtractioninput)
                                    if subtractioninput not in [0,1]:
                                        print(' Số vừa nhập không hợp lệ!')
                                        time.sleep(1)
                                except ValueError:
                                    print(' Lỗi cú pháp!')
                                    time.sleep(1)
                                if subtractioninput==0:
                                    subtractionexit=True
                                if subtractioninput==1:
                                    TitlePrint()
                                    print('     CHO PHÉP KẾT QUẢ ÂM?')
                                    print('')
                                    print('     [0]: Quay lại')
                                    print('')
                                    print('     [1]: Bật')
                                    print('')
                                    print('     [2]: Tắt')
                                    print('')
                                    print(f'{null:-<65}')
                                    print('')
                                    allownegative=str(input(' Lựa chọn (0-2) -> '))
                                    try:
                                        allownegative=int(allownegative)
                                        if allownegative not in [0,1,2]:
                                            print(' Số vừa nhập không hợp lệ!')
                                            time.sleep(1)
                                    except ValueError:
                                        print(' Lỗi cú pháp!')
                                        time.sleep(1)
                                    if allownegative==1:
                                        DKTruNhap='True'
                                    elif allownegative==2:
                                        DKTruNhap="False"
                                    if allownegative in [1,2]:    
                                        TaskComplete()
                                        with open("Data/AllowNegativeResult.log","w") as m1:
                                            m1.write(DKTruNhap)   
                elif inputexpect==5:
                    TitlePrint()
                    print("     THÔNG TIN HỆ THỐNG:")
                    print('')
                    print(f"        + Tên thiết bị: {platform.node()}")
                    print('')
                    print(f"        + Kiến trúc vi xử lý: {platform.machine()}")
                    print('')
                    print(f"        + Tên hệ điều hành: {platform.system()}")
                    print('')
                    print(f"        + Bản dựng: {platform.version()}")
                    print('')
                    print("     Nhấn phím Enter để quay lại")
                    print('')
                    print(f'{null:-<65}')
                    input()
                elif inputexpect==1:
                    repeat=True
                    while repeat==True:
                        BundleTest()
                        TitlePrint()
                        print("     CÀI ĐẶT GIAO DIỆN:")
                        print('')
                        print("     [0]: Thoát")
                        print('')
                        print("     [1]: Chữ")
                        print('')
                        print("     [2]: Nền")
                        print('')
                        print("     [3]: Đảo ngược màu")
                        print('')
                        print("     [4]: Khôi phục cài đặt gốc")
                        print('')
                        print("     [5]: Lưu ý")
                        print("")
                        print(f"{null:-<65}")
                        print("")
                        uiselect=str(input(" Lựa chọn (0-5) -> "))
                        textexit=False
                        bgexit=False
                        resetallexit=False
                        try:
                            uiselect=int(uiselect)
                            if uiselect not in [0,1,2,3,4,5]:
                                print(" Số vừa nhập không hợp lệ.")
                                time.sleep(1)
                        except ValueError:
                            if uiselect.lower()=='textcolortest':
                                print(Style.RESET_ALL)
                                os.system(clrscr)
                                print('')
                                print("                         KIỂM TRA MÀU CHỮ")
                                print('')
                                print(f"{null:-<65}")
                                print('')
                                print(Fore.WHITE+"      1. TRẮNG"+Style.RESET_ALL)
                                print(Fore.LIGHTWHITE_EX+"      2. TRẮNG (NHẠT)"+Style.RESET_ALL)
                                print(Fore.RED+"      3. ĐỎ"+Style.RESET_ALL)
                                print(Fore.LIGHTRED_EX+"      4. ĐỎ (NHẠT)"+Style.RESET_ALL)
                                print(Fore.GREEN+"      5. XANH LỤC"+Style.RESET_ALL)
                                print(Fore.LIGHTGREEN_EX+"      6. XANH LỤC (NHẠT)"+Style.RESET_ALL)
                                print(Fore.BLUE+"      7. XANH LAM"+Style.RESET_ALL)
                                print(Fore.LIGHTBLUE_EX+"      8. XANH LAM (NHẠT)"+Style.RESET_ALL)
                                print(Fore.CYAN+"      9. XANH LƠ (*)"+Style.RESET_ALL)
                                print(Fore.LIGHTCYAN_EX+"      10. XANH LƠ (NHẠT) (*)"+Style.RESET_ALL)
                                print(Fore.MAGENTA+"      11. MÀU CÁNH SEN (*)"+Style.RESET_ALL)
                                print(Fore.LIGHTMAGENTA_EX+"      12. MÀU CÁNH SEN (NHẠT) (*)"+Style.RESET_ALL)
                                print(Fore.YELLOW+"      13. VÀNG"+Style.RESET_ALL)
                                print(Fore.LIGHTYELLOW_EX+"      14. VÀNG (NHẠT)"+Style.RESET_ALL)
                                print('      '+Back.LIGHTBLACK_EX+Fore.BLACK+"15. ĐEN "+Style.RESET_ALL)
                                print(Style.RESET_ALL+Fore.LIGHTBLACK_EX+"      16. ĐEN (NHẠT)")
                                print(Style.RESET_ALL)
                                print("-  Lựa chọn màu không thể chọn ở đây.")
                                print("- Tên màu được lấy và dịch từ tên lệnh thực thi")
                                print("(*) Tên màu được dịch từ Wikipedia Tiếng Việt")
                                print('')
                                print('https://pypi.org/project/colorama/ sẽ có thêm thông tin chi tiết!')
                                print('Nhấn phím Enter để thoát')
                                print('')
                                input(f"{null:-<65}")
                            elif uiselect.lower()=='textstyletest':
                                print(Style.RESET_ALL)
                                os.system(clrscr)
                                print('')
                                print("                         KIẺM TRA KIỂU CHỮ")
                                print('')
                                print(f"{null:-<65}")
                                print('')
                                print(Style.DIM+Style.BRIGHT+"      1. ĐẶC BIỆT (Mờ + Sáng)")
                                print(Style.NORMAL+Style.DIM+"      2. MỜ")
                                print(Style.NORMAL+"      3. THƯỜNG")
                                print(Style.BRIGHT+"      4. SÁNG")
                                print('')
                                print(Style.RESET_ALL+"Lưu ý: Nếu bạn chọn kiểu 'sáng', màu chữ được tự động chuyển sang màu nhạt")
                                print("Hiện tại không rõ lý do lỗi này bắt nguồn từ đâu")
                                print('Nhấn phím Enter để thoát')
                                print('')
                                input(f"{null:-<65}")
                            elif uiselect.lower()=='bgcolortest':
                                print(Style.RESET_ALL)
                                os.system(clrscr)
                                print('')
                                print("                         KIẺM TRA MÀU NỀN")
                                print('')
                                print(f"{null:-<65}")
                                print('')
                                print("     "+Back.WHITE+Fore.BLACK+"1. TRẮNG"+Back.BLACK)
                                print("     "+Back.LIGHTWHITE_EX+"2. TRẮNG (NHẠT)"+Back.BLACK)
                                print("     "+Back.RED+"3. ĐỎ"+Back.BLACK)
                                print("     "+Back.LIGHTRED_EX+"4. ĐỎ (NHẠT)"+Back.BLACK)
                                print("     "+Back.GREEN+"5. XANH LỤC"+Back.BLACK)
                                print("     "+Back.LIGHTGREEN_EX+"6. XANH LỤC (NHẠT)"+Back.BLACK)
                                print("     "+Back.BLUE+"7. XANH LAM"+Back.BLACK)
                                print("     "+Back.LIGHTBLUE_EX+"8. XANH LAM (NHẠT)"+Back.BLACK)
                                print("     "+Back.CYAN+"9. XANH LƠ (*)"+Back.BLACK)
                                print("     "+Back.LIGHTCYAN_EX+"10. XANH LƠ (NHẠT) (*)"+Back.BLACK)
                                print("     "+Back.MAGENTA+"11. MÀU CÁNH SEN (*)"+Back.BLACK)
                                print("     "+Back.LIGHTMAGENTA_EX+"12. MÀU CÁNH SEN (NHẠT) (*)"+Back.BLACK)
                                print("     "+Back.YELLOW+"13. VÀNG"+Back.BLACK)
                                print("     "+Back.LIGHTYELLOW_EX+"14. VÀNG (NHẠT)"+Back.BLACK)
                                print("     "+Back.BLACK+Fore.WHITE+"15. ĐEN"+Back.BLACK)
                                print("     "+Back.LIGHTBLACK_EX+"16. ĐEN (NHẠT)"+Back.BLACK)
                                print(Style.RESET_ALL)
                                print("-  Lựa chọn màu không thể chọn ở đây.")
                                print("- Tên màu được lấy và dịch từ tên lệnh thực thi")
                                print("(*) Tên màu được dịch từ Wikipedia Tiếng Việt")
                                print('')
                                print('https://pypi.org/project/colorama/ sẽ có thêm thông tin chi tiết!')
                                print('Nhấn phím Enter để thoát')
                                print('')
                                input(f"{null:-<65}")
                            else:
                                print(" Lỗi cú pháp!")
                            time.sleep(1)
                        if uiselect==0:
                            repeat=False
                        if uiselect==5:
                            TitlePrint()
                            print('     LƯU Ý:')
                            print('')
                            print('- Một số cài đặt màu sẽ không được hiển thị chính xác! Nó sẽ tùy ')
                            print('thuộc vào console bạn đang dùng')
                            print('')
                            print('- Nếu bạn dùng Windows 10 1903 (10.0.18362.0) trở lên, hãy dùng')
                            print('Windows Terminal để có trải nghiệm tốt nhất!')
                            print('')
                            print(" Nhấn phím Enter để quay lại.")
                            print('')
                            print(f"{null:-<65}")
                            input()
                        if uiselect==1:
                            BundleTest()
                            while textexit==False:
                                TitlePrint()
                                print("     CÀI ĐẶT CHỮ:")
                                print('')
                                print('     [0]: Quay lại')
                                print('')
                                print(f'     [1]: Kiểu chữ (Hiện tại: {textstyleviet})')
                                print('')
                                print(f'     [2]: Độ đậm nhạt của chữ (Hiện tại: {textshadeviet.title()})')
                                print('')
                                print(f'     [3]: Màu chữ (Hiện tại: {textcolorviet})')
                                print('')
                                print(f'{null:-<65}')
                                print('')
                                textselect=str(input(" Lựa chọn (0-3) -> "))
                                textstyleexit=False
                                textshadeexit=False
                                textcolorexit=False
                                try:
                                    textselect=int(textselect)
                                    if textselect not in [0,1,2,3]:
                                        print(" Số vừa nhập không hợp lệ.")
                                        time.sleep(1)
                                    else:
                                        textexit=True
                                except ValueError:
                                    print(" Lỗi cú pháp!")
                                    time.sleep(1)
                                if textselect==1:
                                    BundleTest()
                                    while textstyleexit==False:        
                                        TitlePrint()
                                        print("     KIỂU CHỮ")
                                        print('')
                                        print("     [0]: Quay lại")
                                        print('')
                                        print("     [1]: Mờ")
                                        print('')
                                        print("     [2]: Thường")
                                        print('')
                                        print("     [3]: Sáng")
                                        print('')
                                        print("     [4]: Đặc biệt")
                                        print('')
                                        print(f'{null:-<65}')
                                        print('')
                                        textstyleselect=str(input(" Lựa chọn (0-4) -> "))
                                        try:
                                            textstyleselect=int(textstyleselect)
                                            if textstyleselect not in [0,1,2,3,4]:
                                                print(" Số vừa nhập không hợp lệ.")
                                                time.sleep(1)
                                            else:
                                                textstyleexit=True
                                        except ValueError:
                                            print(" Lỗi cú pháp!")
                                            time.sleep(1)
                                        if textstyleselect==0:
                                            textstyleexit=True
                                            textexit=False
                                        if textstyleselect==1:
                                            textstylechoice='Dim'
                                        if textstyleselect==2:
                                            textstylechoice='Normal'    
                                        if textstyleselect==3:
                                            textstylechoice='Bright'
                                        if textstyleselect==4:
                                            textstylechoice='Special'
                                        if textstyleselect in [1,2,3,4]:    
                                            TaskComplete()
                                            with open("Data/TextStyleSave.log","w") as m1:
                                                m1.write(textstylechoice)
                                            textstyleexit=True       
                                if textselect==0:
                                    textexit=True
                                if textselect==2:
                                    BundleTest()
                                    while textshadeexit==False:
                                        TitlePrint()
                                        print("     ĐỘ ĐẬM NHẠT CỦA CHỮ:")
                                        print('')
                                        print('     [0]: Quay lại')
                                        print('')
                                        print('     [1]: Nhạt')
                                        print('')
                                        print('     [2]: Thường')
                                        print('')
                                        print(f'{null:-<65}')
                                        print('')
                                        textshadeselect=str(input(" Lựa chọn (0-2) -> "))
                                        try:
                                            textshadeselect=int(textshadeselect)
                                            if textshadeselect not in [0,1,2]:
                                                print(" Số vừa nhập không hợp lệ.")
                                                time.sleep(1)
                                            else:
                                                textshadeexit=True
                                        except ValueError:
                                            print(" Lỗi cú pháp!")
                                            time.sleep(1)
                                        if textshadeselect==0:
                                            textshadeexit=True
                                            textexit=False
                                        if textshadeselect==1:
                                            textshadechoice='Light'
                                        if textshadeselect==2:
                                            textshadechoice='Normal'
                                        if textshadeselect in [1,2]:
                                            TaskComplete()
                                            with open("Data/TextShadeSave.log","w") as m1:
                                                m1.write(textshadechoice)
                                if textselect==3:
                                    BundleTest()
                                    while textcolorexit==False:
                                        TitlePrint()
                                        print("     MÀU CHỮ:")
                                        print('')
                                        print('     [0]: Quay lại')
                                        print('')
                                        print('     [1]: Đen')
                                        print('')
                                        print('     [2]: Đỏ')
                                        print('')
                                        print('     [3]: Xanh lục')
                                        print('')
                                        print('     [4]: Vàng')
                                        print('')
                                        print('     [5]: Xanh lam')
                                        print('')
                                        print('     [6]: Màu cánh sen')
                                        print('')
                                        print('     [7]: Xanh lơ')
                                        print('')
                                        print('     [8]: Trắng')
                                        print('')
                                        print(f'{null:-<65}')
                                        print('')
                                        textcolorselect=str(input(" Lựa chọn (0-8) -> "))
                                        try:
                                            textcolorselect=int(textcolorselect)
                                            if textcolorselect not in [0,1,2,3,4,5,6,7,8]:
                                                print(" Số vừa nhập không hợp lệ.")
                                                time.sleep(1)
                                        except ValueError:
                                            print(" Lỗi cú pháp!")
                                            time.sleep(1)                   
                                        if textcolorselect==0:
                                            textcolorexit=True
                                            textexit=False
                                        elif textcolorselect in [1,2,3,4,5,6,7,8]:    
                                            if textcolorselect==1:
                                                textcolortemp='Black'
                                            elif textcolorselect==2:
                                                textcolortemp='Red'
                                            elif textcolorselect==3:
                                                textcolortemp='Green'
                                            elif textcolorselect==4:
                                                textcolortemp='Yellow'
                                            elif textcolorselect==5:
                                                textcolortemp='Blue'
                                            elif textcolorselect==6:
                                                textcolortemp='Magenta'
                                            elif textcolorselect==7:
                                                textcolortemp='Cyan'
                                            elif textcolorselect==8:
                                                textcolortemp='White'
                                            if textcolortemp==bgcolorchoice:
                                                print('Màu chữ bị trùng với màu nền!')
                                                time.sleep(1)
                                                textcolorexit=False                   
                                            else:
                                                textcolorchoice=textcolortemp
                                                with open("Data/TextColorSave.log","w") as m1:
                                                    m1.write(textcolorchoice)
                                                TaskComplete()
                                                textcolorexit=True
                        if uiselect==2:
                            BundleTest()
                            while bgexit==False:              
                                os.system(clrscr)
                                TitlePrint()
                                print("     CÀI ĐẶT NỀN:")
                                print('')
                                print('     [0]: Quay lại')
                                print('')
                                print(f'     [1]: Độ đậm nhạt của nền (Hiện tại: {bgshadeviet.title()})')
                                print('')
                                print(f'     [2]: Màu nền (Hiện tại: {bgcolorviet.title()})')
                                print('')
                                print(f'{null:-<65}')
                                print('')
                                bgselect=str(input(' Lựa chọn (0-2) -> '))
                                bgshadeexit=False
                                bgcolorexit=False
                                try:
                                    bgselect=int(bgselect)
                                    if bgselect not in [0,1,2]:
                                        print(" Số vừa nhập không hợp lệ!")
                                        time.sleep(1)
                                    else:
                                        bgexit=True
                                except ValueError:
                                    print(" Lỗi cú pháp!")
                                    time.sleep(1)
                                if bgselect==0:
                                    bgexit=True
                                if bgselect==1:
                                    BundleTest()
                                    while bgshadeexit==False:
                                        os.system(clrscr)
                                        TitlePrint()
                                        print("     ĐỘ ĐẬM NHẠT CỦA NỀN:")
                                        print('')
                                        print('     [0]: Quay lại')
                                        print('')
                                        print('     [1]: Nhạt')
                                        print('')
                                        print('     [2]: Thường')
                                        print('')
                                        print(f'{null:-<65}')
                                        print('')
                                        bgshadeselect=str(input(" Lựa chọn (0-2) -> "))
                                        try:
                                            bgshadeselect=int(bgshadeselect)
                                            if bgshadeselect not in [0,1,2]:
                                                print(" Số vừa nhập không hợp lệ.")
                                                time.sleep(1)
                                            else:
                                                bgshadeexit=True
                                        except ValueError:
                                            print(" Lỗi cú pháp!")
                                            time.sleep(1)
                                        if bgshadeselect==0:
                                            bgshadeexit=True
                                            bgexit=False
                                        if bgshadeselect==1:
                                            bgshadechoice='Light'                        
                                        if bgshadeselect==2:
                                            bgshadechoice='Normal'
                                        if bgshadeselect in [1,2]:
                                            TaskComplete()
                                            with open("Data/BGShadeSave.log","w") as m1:
                                                m1.write(bgshadechoice)
                                if bgselect==2:
                                    BundleTest()
                                    while bgcolorexit==False:
                                        os.system(clrscr)
                                        TitlePrint()
                                        print("     MÀU NỀN:")
                                        print('')
                                        print('     [0]: Quay lại')
                                        print('')
                                        print('     [1]: Đen')
                                        print('')
                                        print('     [2]: Đỏ')
                                        print('')
                                        print('     [3]: Xanh lục')
                                        print('')
                                        print('     [4]: Vàng')
                                        print('')
                                        print('     [5]: Xanh lam')
                                        print('')
                                        print('     [6]: Màu cánh sen')
                                        print('')
                                        print('     [7]: Xanh lơ')
                                        print('')
                                        print('     [8]: Trắng')
                                        print('')
                                        print(f'{null:-<65}')
                                        print('')
                                        bgcolorselect=str(input(" Lựa chọn (0-8) -> "))
                                        try:
                                            bgcolorselect=int(bgcolorselect)
                                            if bgcolorselect not in [0,1,2,3,4,5,6,7,8]:
                                                print(" Số vừa nhập không hợp lệ.")
                                                time.sleep(1)
                                        except ValueError:
                                            print(" Lỗi cú pháp!")
                                            time.sleep(1)                   
                                        if bgcolorselect==0:
                                            bgcolorexit=True
                                            bgexit=False
                                        elif bgcolorselect in [1,2,3,4,5,6,7,8]:    
                                            if bgcolorselect==1:
                                                bgcolortemp='Black'
                                            elif bgcolorselect==2:
                                                bgcolortemp='Red'
                                            elif bgcolorselect==3:
                                                bgcolortemp='Green'
                                            elif bgcolorselect==4:
                                                bgcolortemp='Yellow'
                                            elif bgcolorselect==5:
                                                bgcolortemp='Blue'
                                            elif bgcolorselect==6:
                                                bgcolortemp='Magenta'
                                            elif bgcolorselect==7:
                                                bgcolortemp='Cyan'
                                            elif bgcolorselect==8:
                                                bgcolortemp='White'
                                            if textcolorchoice==bgcolortemp:
                                                print('Màu nền trùng với màu chữ!')
                                                time.sleep(1)
                                            else:    
                                                bgcolorchoice=bgcolortemp
                                                TaskComplete()
                                                with open("Data/BGColorSave.log","w") as m1:
                                                    m1.write(bgcolorchoice)
                                                bgcolorexit=True
                        if uiselect==4:
                            ApplySettings()
                            os.system(clrscr)
                            TitlePrint()
                            print("     LƯU Ý:")
                            print('')
                            print("* Bạn sẽ KHÔI PHỤC TẤT CẢ cài đặt giao diện về mặc định!")
                            print("  Bạn chắc chắn muốn tiếp tục không?")
                            print('')
                            print("     [0]: Không")
                            print('')
                            print("     [1]: Có")
                            print('')
                            print(f'{null:-<65}')
                            print('')
                            resetallselect=str(input(" Lựa chọn (0-1) -> "))
                            try:
                                resetallselect=int(resetallselect)
                                if resetallselect not in [0,1]:
                                    print(" Số vừa nhập không hợp lệ!")
                                    time.sleep(1)
                            except ValueError:
                                print(" Lỗi cú pháp!")
                                time.sleep(1)
                            if resetallselect==1:
                                TaskComplete()
                                SetColorToDefault()
                        if uiselect==3:
                            BundleTest()
                            TitlePrint()
                            print("                         LƯU Ý!")
                            print('')
                            print("     Màu giao diện sẽ bị đảo ngược từ:")
                            print('')
                            print(f"     (Chữ {textcolorviet.lower()} → Chữ {bgcolorviet.lower()})")
                            print('')
                            print(f"     (Nền {bgcolorviet.lower()} → Nền {textcolorviet.lower()})")
                            print('')
                            print("     Bạn chắc chắn muốn tiếp tục không?")
                            print('')
                            print("     [0]: Không")
                            print('')
                            print("     [1]: Có")
                            print('')
                            print(f"{null:-<65}")
                            print('')
                            invertselect=str(input(" Lựa chọn (0-1) -> "))
                            try:
                                invertselect=int(invertselect)
                                if invertselect not in [0,1]:
                                    print(" Số vừa nhập không hợp lệ!")
                                    time.sleep(1)
                            except ValueError:
                                print(" Lỗi cú pháp!")
                                time.sleep(1)
                            if invertselect==1:
                                bgcolorchoice,textcolorchoice=textcolorchoice,bgcolorchoice
                                with open("Data/TextColorSave.log","w") as m1:
                                    m1.write(textcolorchoice)
                                with open("Data/BGColorSave.log","w") as m1:
                                    m1.write(bgcolorchoice)
                                TaskComplete()
                elif inputexpect==4:
                    TitlePrint()
                    print("     THÔNG TIN PHẦN MỀM:")
                    print('')
                    print("     - Phiên bản 1.4.2")
                    print('')
                    print(f'     - Phiên bản Python: {platform.python_version()}')
                    print('')
                    print("     Nhấn phím Enter để quay lại")
                    print('')
                    print(f"{null:-<65}")
                    input()
                elif inputexpect==3:
                   while viewsettingsexit==False: 
                        ApplySettings()
                        TitlePrint()
                        print("     XEM CÀI ĐẶT:")
                        print('')
                        print('     [0]: Thoát')
                        print('')
                        print('     [1]: Cài đặt giao diện')
                        print('')
                        print('     [2]: Cài đặt toán học')
                        print('')
                        print(f"{null:-<65}")
                        print("")
                        viewchoice=str(input(' Lựa chọn (0-2) -> '))
                        try:
                            viewchoice=int(viewchoice)
                            if viewchoice not in [0,1,2]:
                                print(" Số vừa nhập không hợp lệ!")
                                time.sleep(1)
                        except ValueError:
                            print(" Lỗi cú pháp!")
                            time.sleep(1)
                        if viewchoice==0:
                            viewsettingsexit=True
                        elif viewchoice==1:
                            TitlePrint()
                            print("                     CÀI ĐẶT GIAO DIỆN:")
                            print('')
                            print("           --------------- Chữ: ---------------")
                            print('')
                            print(f"           - Kiểu chữ: {textstyleviet}")
                            print('')
                            print(f"           - Độ đậm nhạt của chữ: {textshadeviet}")
                            print('')
                            print(f"           - Màu chữ: {textcolorviet}")
                            print('')
                            print("           -------------- Nền: ---------------")
                            print('')
                            print(f"           - Độ đậm nhạt của nền: {bgshadeviet}")
                            print('')
                            print(f"           - Màu nền: {bgcolorviet}")
                            print('')
                            print("Nhấn phím Enter để quay lại")
                            print('')
                            print(f'{null:-<65}')
                            input()
                        elif viewchoice==2:
                            TitlePrint()
                            print("                       CÀI ĐẶT TOÁN HỌC:")
                            print('')
                            print("           --------------- Phép cộng ---------------")
                            print('')
                            print('                 - Cài đặt không tồn tại')
                            print('')
                            print("           --------------- Phép trừ  ---------------")
                            print('')
                            print(f"                - Cho phép kết quả âm: {DKTru}")
                            print('')
                            print("           --------------- Phép nhân ---------------")
                            print('')
                            print('                 - Cài đặt không tồn tại')
                            print('')
                            print("           --------------- Phép chia ---------------")
                            print('')
                            print(f"                - Cho phép kết quả thập phân: {DKthapphan}")
                            print('')
                            if DKthapphan=="Tắt":
                                print("                - Làm tròn đến hàng thập phân thứ (Tắt)")
                            else:
                                print(f"               - Làm tròn đến hàng thập phân thứ {rounding}")
                            print('')
                            print("Nhấn phím Enter để quay lại")
                            print('')
                            print(f'{null:-<65}')
                            input()
        elif pt==1:
            dau="+"
            phep='cộng'
        elif pt==3:
            dau="x"
            phep='nhân'
        elif pt==2:
            dau='-'
            phep='trừ'
        else:
            dau=':'
            phep='chia'
        if pt in [1,2,3,4]:    
            os.system(clrscr)
            while settingsexit==False:
                TitlePrint()              
                print(f"     * Phép {phep}:")
                print('')
                print("     Số bài toán bạn muốn thực hiện: ")
                print('')
                print("     [0]: Thoát")
                print('')
                print("     [1-∞]: Nhập số tương ứng với số bài toán")
                print('')
                print(f"{null:-<65}")
                print('')
                sbt=str(input(" Lựa chọn (0, 1-∞) -> "))
                ainputexit=False
                try: 
                    sbt=int(sbt)
                    if sbt<0:
                        TitlePrint()
                        print("                         LỖI GIÁ TRỊ!!!")
                        print('')
                        print(" Số bài toán không được phép nhỏ hơn 1! Nhấn Enter để nhập lại!")
                        print("")
                        print(f"{null:-<65}")
                        print('')
                        input()
                    if sbt>=1:    
                        while ainputexit==False:
                            TitlePrint()
                            print(f"     * Phép {phep}:")
                            print('')
                            print(f"     + Số bài toán bạn muốn thực hiện: {sbt}")
                            print('')
                            print("     Giá trị lớn nhất của số a:")
                            print('')
                            print("     [0]: Quay lại")
                            print('')
                            print("     [1-∞]: Nhập giá trị lớn nhất")
                            print('')
                            print(f"{null:-<65}")
                            print('')
                            a=str(input(" Lựa chọn (0, 1-∞) -> "))
                            binputexit=False
                            try:
                                a=int(a)
                                if a==0:
                                    ainputexit=True
                                if a<0:
                                    print(" Giá trị này không được bé hơn 0")
                                    time.sleep(1)
                                if a>0:
                                    while binputexit==False:
                                        os.system(clrscr)
                                        TitlePrint()
                                        print(f"     * Phép {phep}:")
                                        print('')
                                        print(f"     + Số bài toán bạn muốn thực hiện: {sbt}")
                                        print('')
                                        print(f"     + Giá trị lớn nhất của số a: {a}")
                                        print('')
                                        print("     Giá trị lớn nhất của số b:")
                                        print('')
                                        print("     [0]: Quay lại")
                                        print('')
                                        print("     [1-∞]: Nhập giá trị lớn nhất")
                                        print('')
                                        print(f"{null:-<65}")
                                        print('')
                                        b=str(input(" Lựa chọn (0, 1-∞) -> "))
                                        confirmsettings=False
                                        try:
                                            b=int(b)
                                            if b==0:
                                                binputexit=True
                                            if b>=1:
                                                while confirmsettings==False:
                                                    MathApply()
                                                    TitlePrint()
                                                    print(f"     * Phép {phep}:")
                                                    print('')
                                                    print(f"     + Số bài toán bạn muốn thực hiện: {sbt}")
                                                    print('')
                                                    print(f"     + Giá trị lớn nhất của số a: {a}")
                                                    print('')
                                                    print(f"     + Giá trị lớn nhất của số b: {b}")
                                                    print('')
                                                    if pt==2:
                                                        print(f"     + Cho phép tạo phép tính với kết quả âm: {DKTru}")
                                                    elif pt==4:
                                                        print(f"     + Cho phép tạo phép tính với kết quả thập phân: {DKthapphan}")
                                                        print('')    
                                                        if DKthapphanNhap.title()=='True':
                                                            print(f"     + Làm tròn tới số thập phân thứ {rounding}")
                                                            print('')
                                                    print(f"     Cài đặt này ổn với bạn không?")
                                                    print('')
                                                    print("     [0]: Không")
                                                    print('')
                                                    print("     [1]: Có")
                                                    print('')
                                                    print(f"{null:-<65}")
                                                    print('')
                                                    confirminput=str(input(" Lựa chọn (0-1) -> "))
                                                    if DKthapphan.title()=='Bật' and pt==4 and confirminput=='1':
                                                        os.system(clrscr)
                                                        TitlePrint()
                                                        print("Lưu ý:")
                                                        print('')
                                                        print(' * Với bài toán có dư: ')
                                                        print('')
                                                        print("     + Không được viết kết quả dưới dạng a/b!")
                                                        print("")
                                                        print('         Ví dụ: 5 : 4 = 5/4 (✗)')
                                                        print('')
                                                        print("     + Kí hiệu của dấu phẩy là dấu chấm.")
                                                        print('')
                                                        print('         Ví dụ: - 5 : 4 = 1.25 (✓)')
                                                        print('                - 5 : 4 = 1,25 (✗)')   
                                                        print('')
                                                        print(' * Với bài toán chia hết: ')
                                                        print('')
                                                        print('     + Bạn chỉ cần ghi kết quả như thường')
                                                        print('')
                                                        print('         Ví dụ: - 4 : 2 = 2 (✓)')
                                                        print('                - 4 : 2 = 2.000000 (Không cần thiết)')
                                                        print('')
                                                        print('Nhấn phím Enter để bắt đầu')
                                                        print('')
                                                        input(f"{null:-<65}")
                                                    exitpro=False
                                                    nq=1
                                                    ca=0
                                                    try:
                                                        confirminput=int(confirminput)
                                                        if confirminput==0:
                                                            confirmsettings=True
                                                            ainputexit=True
                                                            binputexit=True
                                                            settingsexit=True
                                                        elif confirminput not in [0,1]:
                                                            print(' Số vừa nhập không hợp lệ!')
                                                            time.sleep(1)
                                                        os.system(clrscr)
                                                        if confirminput==1:
                                                            while nq<=sbt:
                                                                if pt in [1,3]:
                                                                    c=random.randint(0,a)
                                                                    d=random.randint(0,b)
                                                                if pt==2 and DKTruNhap=='False':
                                                                    while c<d:
                                                                        c=random.randint(0,a)
                                                                        d=random.randint(0,b)
                                                                else:
                                                                    c=random.randint(0,a)
                                                                    d=random.randint(1,b)
                                                                    if DKthapphanNhap=="False":
                                                                        while c%d!=0:
                                                                            c=random.randint(0,a)
                                                                            d=random.randint(1,b)
                                                                exitpro=False
                                                                TitlePrint()
                                                                print("     [Exit]: Thoát")
                                                                print('')
                                                                print(f"     Bài {nq}/{sbt}:")
                                                                print('')
                                                                print(f"     {c} {dau} {d} = ?") 
                                                                print('')
                                                                print(f"{null:-<65}")
                                                                print('')
                                                                kq=str(input(' Nhập kết quả -> '))
                                                                print('')
                                                                try:
                                                                   kq=float(kq)
                                                                   errorValue=False
                                                                except ValueError:
                                                                   if kq.lower()=='exit':
                                                                       nq=sbt
                                                                       errorValue=False
                                                                       exitpro=True
                                                                   else:
                                                                       errorValue=True
                                                                       print(" Giá trị không hợp lệ. Hệ thống sẽ tự tạo ra bài khác và đánh dấu bài này sai.")
                                                                nq+=1
                                                                if pt==1:
                                                                     kqd=c+d
                                                                elif pt==2:
                                                                    kqd=c-d
                                                                elif pt==3:
                                                                     kqd=c*d
                                                                else:
                                                                    if DKthapphanNhap=="True":
                                                                        kqd=round(c/d,rounding)
                                                                    else:
                                                                        kqd=round(c/d)
                                                                if kq==kqd:
                                                                    print(" Kết quả chính xác!")
                                                                    print(" Nhấn phím Enter để tiếp tục.")
                                                                    input()
                                                                    os.system(clrscr)
                                                                    ca+=1
                                                                else:
                                                                    if errorValue==False:
                                                                        print(" Kết quả vừa nhập không chính xác.")
                                                                    if exitpro==False:
                                                                     print(f" Kết quả đúng của bài toán {c} {dau} {d} là {kqd}")
                                                                     print(" Nhấn phím Enter để tiếp tục.")
                                                                     input()
                                                                    os.system(clrscr)
                                                                resultexit=False
                                                            while resultexit==False:
                                                                TitlePrint()
                                                                print("     TỔNG KẾT:")
                                                                print('')
                                                                print(f"     Bạn đã làm được {ca}/{sbt} câu đúng")
                                                                print('')
                                                                print(f"     Tỉ lệ câu đúng là: {round(ca/sbt*100)}%")
                                                                print('')
                                                                print("     [0]: Thoát chương trình")
                                                                print('')
                                                                print("     [1]: Quay lại màn hình chính")
                                                                print('')
                                                                print(f"{null:-<65}")
                                                                print('')
                                                                expected=str(input(" Lựa chọn (0-1) -> "))
                                                                try:
                                                                    expected=int(expected)
                                                                    if expected not in [0,1]:
                                                                        print(" Giá trị không hợp lệ! Vui lòng thử lại.")
                                                                    elif expected==1:
                                                                        resultexit=True
                                                                        settingsexit=True
                                                                        confirmsettings=True
                                                                        ainputexit=True
                                                                        binputexit=True
                                                                    else:
                                                                        TitlePrint()
                                                                        print('     BẠN CÓ CHẮC CHẮN MUỐN THOÁT KHÔNG?')
                                                                        print("")
                                                                        print('     [0]: Không')
                                                                        print("")
                                                                        print('     [1]: Có')
                                                                        print('')
                                                                        print(f"{null:-<65}")
                                                                        print("")
                                                                        confirmexit=str(input(' Lựa chọn (0-1) -> '))
                                                                        try:
                                                                            confirmexit=int(confirmexit)
                                                                            if confirmexit==1:
                                                                                resultexit=True
                                                                                exitprogram()
                                                                            elif confirmexit not in [0,1]:
                                                                                print(' Số vừa nhập không hợp lệ!')
                                                                                time.sleep(1)
                                                                        except ValueError:
                                                                            print(' Lỗi cú pháp!')
                                                                            time.sleep(1)
                                                                except ValueError:
                                                                    print(" Lỗi cú pháp!")
                                                    except ValueError:
                                                        print(' Lỗi cú pháp!')
                                                        time.sleep(1)
                                        except ValueError:
                                            if b.lower()=='exit':
                                                exitprogram()
                                            print(" Giá trị không hợp lệ.")
                                            time.sleep(1)
                            except ValueError:
                                if a.lower()=='exit':
                                    exitprogram()
                                print(" Giá trị không hợp lệ.")
                                time.sleep(1)
                    elif sbt==0:
                        settingsexit=True
                except ValueError:
                    print(" Giá trị không hợp lệ.")
                    time.sleep(1)
except KeyboardInterrupt:
    exitprogram()
