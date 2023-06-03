import platform,os,random,time,sys
null=""
clrscr='cls' if platform.system()=="Windows" else 'clear'
def TitlePrint():
    os.system(clrscr)
    print("")
    print("                 TRÌNH TẠO PHÉP TOÁN NGẪU NHIÊN")
    print("")
    print(f"{null:-<65}")
    print("")
appversion='v1.4.5'
devoption=False
mathdata=["Bật","Bật","Bật","Bật"]
def ResizeWindows():
    if platform.system()=='Windows':
        os.system("mode con cols=65 lines=32")
def BeginBSOD():
    print(Back.BLUE+Fore.WHITE+"Error Detected")
    os.system(clrscr)
    time.sleep(0.05)
    print("A problem has been detected and MathProblemGenerator has been shut down to prevent damage to this software")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
    print("The problem seems to be caused by the following: PY.EXE")
    time.sleep(0.05)
    print("")
    time.sleep(0.05)
ResizeWindows()
TitlePrint()
print("             Đang khởi động các thành phần cần thiết.")
print("")
print(f"{null:-<65}")
def ConnectionFailed():
    print("           Hình như PC này chưa kết nối đến Internet!")
    print("")
    print("           Hãy kết nối PC này vào Internet và thử lại!")
    print('')
    print('            Bây giờ thì hãy nhấn phím Enter để thoát')
    print('')
    input(f'{null:-<65}')
def LoadingScreen():
    TitlePrint()
    print("                            Đang tải...")
    print('')
    print("             Đừng bấm phím Enter trong thời điểm này!")
    print("")
    print(f"{null:-<65}")
try:
    try:
        import requests
        requestesrequired=False
    except ModuleNotFoundError:
        requestsrequired=True
    try:
        from colorama import Fore, Back, Style, init, AnsiToWin32
    except ModuleNotFoundError:
        if platform.system()=='Windows':
            os.system('py -m pip install colorama')
        else:
            os.system('pip install colorama')
except KeyboardInterrupt:
    sys.exit()
def TaskComplete():
    TitlePrint()
    print("     Cài đặt được lưu thành công!")
    print("     Thay đổi sẽ được thiết lập khi bấm phím Enter")
    print("     Nhấn phím Enter để tiếp tục")
    print('')
    input(f"{null:-<65}")
mainloop=True
enable=True
btd=0
inputexpect=3108
try:
    def exitprogram():
        os.system(clrscr)
        global settingsexit,confirmsettings,ainputexit,binputexit
        TitlePrint()
        print('                        Đang thoát...')
        print('')
        print(f'{null:-<65}')
        time.sleep(1)
        sys.exit()
    default=["Normal","Normal","White","Normal","Black","False","False","3","False","False"]
    randomcolor=['Black','Red','Green','Blue','Yellow','Magenta','Cyan','White']
    def FileVerify():
        global data
        try:
            error=False
            a=open("SaveFile.txt","r")
            data=a.readlines()
            try:
                if data[0].removesuffix("\n") not in ["Dim","Normal",'Bright','Special']:#0
                    data[0]=default[0]+"\n"
                    error=True
                if data[1].removesuffix("\n") not in ["Normal",'Light']:#1
                    data[1]=default[1]+"\n"
                    error=True
                if data[2].removesuffix("\n") not in randomcolor:#2
                    data[2]=default[2]+"\n"
                    error=True
                if data[3].removesuffix("\n") not in ["Normal","Light"]:#3
                    data[3]=default[3]+"\n"
                    error=True
                if data[4].removesuffix("\n") not in randomcolor:#4
                    data[4]=default[4]+"\n"
                    error=True
                if data[5].removesuffix("\n") not in ["True","False"]:#5
                    data[5]=default[5]+"\n"
                    error=True
                if data[6].removesuffix("\n") not in ["True","False"]:#6
                    data[6]=default[6]+"\n"
                    error=True
                if data[7].removesuffix("\n") not in ["1","2","3","4","5"]:#7
                    data[7]=default[7]+"\n"
                    error=True
                if data[8].removesuffix("\n") not in ["True","False"]:#8
                    data[8]=default[8]+"\n"
                    error=True
                if data[9].removesuffix("\n") not in ["True","False"]:#9
                    data[9]=default[9]+"\n"
                    error=True
                if error==True:
                    with open("SaveFile.txt","w") as f:
                        for lines in data:
                            f.write(lines)
            except IndexError:
                with open("SaveFile.txt","w") as f:
                    for lines in default:
                        f.write(lines)
                        f.write('\n')
        except FileNotFoundError:
            with open("SaveFile.txt","w") as f:
                for lines in default:
                    f.write(lines)
                    f.write('\n')
    FileVerify()
    def ApplySettings():
        global textstyleviet,textshadeviet,textcolorviet,bgshadeviet,bgcolorviet,DKTru,DKTruDisplay
        LogFileRead()
        if textstylechoice.title()=="Normal"+"\n":
            print(Style.NORMAL)
            textstyleviet='Thường'
        elif textstylechoice.title()=="Dim"+"\n":
            print(Style.NORMAL)
            print(Style.DIM)
            textstyleviet='Mờ'
        elif textstylechoice.title()=="Bright"+"\n":
            print(Style.NORMAL)
            print(Style.BRIGHT)
            textstyleviet='Sáng'
        elif textstylechoice.title()=='Special'+"\n":
            print(Style.DIM)
            print(Style.BRIGHT)
            textstyleviet='Đặc biệt'
        if textshadechoice.title()=='Light'+"\n":
            textshadeviet='Nhạt'
            if textcolorchoice.title()=='Black'+"\n":
                print(Fore.LIGHTBLACK_EX)
                textcolorviet='Đen'
            if textcolorchoice.title()=='Red'+"\n":
                print(Fore.LIGHTRED_EX)
                textcolorviet='Đỏ'
            if textcolorchoice.title()=='Green'+"\n":
                print(Fore.LIGHTGREEN_EX)
                textcolorviet='Xanh lục'
            if textcolorchoice.title()=='Yellow'+"\n":
                print(Fore.LIGHTYELLOW_EX)
                textcolorviet='Vàng'
            if textcolorchoice.title()=='Blue'+"\n":
                print(Fore.LIGHTBLUE_EX)
                textcolorviet='Xanh lam'
            if textcolorchoice.title()=='Magenta'+"\n":
                print(Fore.LIGHTMAGENTA_EX)
                textcolorviet='Màu cánh sen'
            if textcolorchoice.title()=='Cyan'+"\n":
                print(Fore.LIGHTCYAN_EX)
                textcolorviet='Xanh lơ'
            if textcolorchoice.title()=='White'+"\n":
                print(Fore.LIGHTWHITE_EX)
                textcolorviet='Trắng'
        else:
            textshadeviet='Thường'
            if textcolorchoice.title()=='Black'+"\n":
                print(Fore.BLACK)
                textcolorviet='Đen'
            if textcolorchoice.title()=='Red'+"\n":
                print(Fore.RED)
                textcolorviet='Đỏ'
            if textcolorchoice.title()=='Green'+"\n":
                print(Fore.GREEN)
                textcolorviet='Xanh lục'
            if textcolorchoice=='Yellow'+"\n":
                print(Fore.YELLOW)
                textcolorviet='Vàng'
            if textcolorchoice.title()=='Blue'+"\n":
                print(Fore.BLUE)
                textcolorviet='Xanh lam'
            if textcolorchoice=='Magenta'+"\n":
                print(Fore.MAGENTA)
                textcolorviet='Màu cánh sen'
            if textcolorchoice.title()=='Cyan'+"\n":
                print(Fore.CYAN)
                textcolorviet='Xanh lơ'
            if textcolorchoice.title()=='White'+"\n":
                print(Fore.WHITE)
                textcolorviet='Trắng'
        if bgshadechoice.title()=='Light'+"\n":
            bgshadeviet='Nhạt'
            if bgcolorchoice.title()=='Black'+"\n":
                print(Back.LIGHTBLACK_EX)
                bgcolorviet='Đen'
            if bgcolorchoice.title()=='Red'+"\n":
                print(Back.LIGHTRED_EX)
                bgcolorviet='Đỏ'
            if bgcolorchoice.title()=='Green'+"\n":
                print(Back.LIGHTGREEN_EX)
                bgcolorviet='Xanh lục'
            if bgcolorchoice.title()=='Yellow'+"\n":
                print(Back.LIGHTYELLOW_EX)
                bgcolorviet='Vàng'
            if bgcolorchoice.title()=='Blue'+"\n":
                print(Back.LIGHTBLUE_EX)
                bgcolorviet='Xanh lam'
            if bgcolorchoice.title()=='Magenta'+"\n":
                print(Back.LIGHTMAGENTA_EX)
                bgcolorviet='Màu cánh sen'
            if bgcolorchoice.title()=='Cyan'+"\n":
                print(Back.LIGHTCYAN_EX)
                bgcolorviet='Xanh lơ'
            if bgcolorchoice.title()=='White'+"\n":
                print(Back.LIGHTWHITE_EX)
                bgcolorviet='Trắng'
        else:
            bgshadeviet='Thường'
            if bgcolorchoice=='Black'+"\n":
                print(Back.BLACK)
                bgcolorviet='Đen'
            if bgcolorchoice=='Red'+"\n":
                print(Back.RED)
                bgcolorviet='Đỏ'
            if bgcolorchoice=='Green'+"\n":
                print(Back.GREEN)
                bgcolorviet='Xanh lục'
            if bgcolorchoice=='Yellow'+"\n":
                print(Back.YELLOW)
                bgcolorviet='Vàng'
            if bgcolorchoice=='Blue'+"\n":
                print(Back.BLUE)
                bgcolorviet='Xanh lam'
            if bgcolorchoice=='Magenta'+"\n":
                print(Back.MAGENTA)
                bgcolorviet='Màu cánh sen'
            if bgcolorchoice=='Cyan'+"\n":
                print(Back.CYAN)
                bgcolorviet='Xanh lơ'
            if bgcolorchoice=='White'+"\n":
                print(Back.WHITE)
                bgcolorviet='Trắng'
    def LogFileRead():
        global textstylechoice,textshadechoice,textcolorchoice,bgshadechoice,bgcolorchoice,DKTruNhap,DKthapphanNhap,roundtemp
        global devdata,devoption,searchengine,bsod,bsodviet,logindex,data,bsodbool
        try:
            with open("SaveFile.txt","r") as b:
                data=b.readlines()
                logindex=len(default)-1
            textstylechoice=data[0]
            textshadechoice=data[1]
            textcolorchoice=data[2]
            bgshadechoice=data[3]
            bgcolorchoice=data[4]
            DKTruNhap=data[5]
            DKthapphanNhap=data[6]
            roundtemp=data[7]
            devdata=data[8]   
            bsod=data[9]
            if devdata=="True"+"\n":
                devoption=True
            else:
                devoption=False
            if bsod=='True'+"\n":
                bsodviet='Bật'
                bsodbool=True
            elif bsod=='False'+"\n":
                bsodviet='Tắt'
                bsodbool=False
        except IndexError:
            with open("SaveFile.txt","w") as f:
                for lines in default:
                    f.write(lines)
                    f.write('\n')
            LogFileRead()
    def SetColorToDefault():
        data[0]=default[0]+"\n"
        data[1]=default[1]+"\n"
        data[2]=default[2]+"\n"
        data[3]=default[3]+"\n"
        data[4]=default[4]+"\n"
        with open("SaveFile.txt","w") as f:
            for lines in data:
                f.writelines(lines)
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
            SetColorToDefault()
            ApplySettings()
    def BundleTest():
        FileVerify()
        LogFileRead()
        ColorMatchTest()
        ApplySettings()
    def MathApply():
        global DKTru,DKthapphan,rounding,roundtemp
        LogFileRead()
        if DKTruNhap=='False'+"\n":
            DKTru="Tắt"
        else:
            DKTru="Bật"
        if DKthapphanNhap=='False'+"\n":
            DKthapphan='Tắt'
        else:
            DKthapphan='Bật'
        rounding=int(roundtemp.removesuffix("\n"))
    def TotallyApplySettings():
        for i in range (0,3):
            ApplySettings()
            i+=1
            os.system(clrscr)
    while mainloop:    
        ca=0
        nq=1
        BundleTest()
        MathApply()
        TotallyApplySettings()
        TitlePrint()
        print("     MÀN HÌNH CHÍNH\n")
        print('     [0]: Thoát chương trình') #2 tab
        print('')
        print('     [1]: Cộng')
        print('')
        print('     [2]: Trừ')
        print('')
        print('     [3]: Nhân')
        print('')
        print('     [4]: Chia')
        print('')
        print('     [5]: Hỗn hợp')
        print('')
        print('     [6]: Cài đặt')
        print("")
        print(f'{null:-<65}')
        print('')
        pt=str(input(" Lựa chọn (0-6) -> "))
        settingsexit=False
        try:
            pt=int(pt)
            if pt not in [0,1,2,3,4,5,6]:
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
                elif confirmexit not in [0,1]:
                    print(' Số vừa nhập không hợp lệ!')
                    time.sleep(1)
            except ValueError:
                print(' Lỗi cú pháp!')
                time.sleep(1)
        elif pt==6:
            while settingsexit==False:
                BundleTest()
                TitlePrint()
                print('     CÀI ĐẶT:')
                print('')
                print('     [0]: Quay lại')
                print('')
                print('     [1]: Cài đặt giao diện')
                print('')
                print('     [2]: Cài đặt toán học')
                print('')
                print('     [3]: Thông tin phần mềm')
                print('')
                print('     [4]: Thông tin hệ thống')
                print('')
                print('     [5]: Cập nhật phần mềm')
                print("")
                if data[8]=="True"+"\n":
                    print('     [6]: Tùy chọn nhà phát triển')
                    print('')
                print(f'{null:-<65}')
                print('')
                if devdata=="True"+"\n":
                    inputexpect=str(input(' Lựa chọn (0-6) -> '))
                else:
                    inputexpect=str(input(' Lựa chọn (0-5) -> '))
                uisettingsexit=False
                mathsettingsexit=False
                viewsettingsexit=False
                mikuloop=True
                commandloop=True
                othertoolsloop=True
                try:
                    inputexpect=int(inputexpect)
                    if devoption==False and inputexpect not in [0,1,2,3,4,5,310082007]:
                        print(' Số vừa nhập không hợp lệ!')
                        time.sleep(1)
                    if inputexpect not in [0,1,2,3,4,5,6,31082007] and devdata=="True"+"\n":
                        print(' Số vừa nhập không hợp lệ!')
                        time.sleep(1)
                except ValueError:
                    LogFileRead()
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
                    elif inputexpect in ['//allowdevoption=true','//allowdevoption=True']:
                        data[8]="True"+"\n"
                        with open("SaveFile.txt","w") as f:
                            for lines in data:
                                f.writelines(lines)
                        devoption=True
                        print(" Changes applied successfully!")
                        time.sleep(1)
                    elif inputexpect in ['//allowdevoption=false','//allowdevoption=False']:
                        data[8]="False"+"\n"
                        data[9]="False"+'\n'
                        with open("SaveFile.txt","w") as f:
                            for lines in data:
                                f.writelines(lines)
                        devoption=False
                        print(" Changes applied successfully!")
                        time.sleep(1)
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
                               print("                  TRÌNH QUẢN LÝ EASTER EGG\n")
                               print(f"{null:-<65}")
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
                            print("Enjoy!")
                            time.sleep(1)
                            os.system('start \"\" https://www.youtube.com/watch?v=Q1_vm1TwYyU')
                           else:
                            print(' Lỗi cú pháp!')
                            time.sleep(1)
                elif inputexpect==6 and devoption==True:
                    devloop=True
                    LogFileRead()
                    while devloop:
                        TitlePrint()
                        print("     TUỲ CHỌN NHÀ PHÁT TRIỂN:")
                        print("")
                        print("     [0]: Quay lại")
                        print('')
                        print('     [1]: Xem giá trị đã lưu')
                        print('')
                        print("     [2]: Kiểm tra hiển thị")
                        print("")
                        print('     [3]: Cài đặt vui')
                        print('')
                        print(' * Khi tắt mục này, mọi thay đổi ở đây sẽ được trở về mặc định')
                        print(f'{null:-<65}')
                        print('')
                        devinput=str(input(" Lựa chọn (0-3) -> "))
                        try:
                            devinput=int(devinput)
                            if devinput not in [0,1,2,3]:
                               print(' Số vừa nhập không hợp lệ!')
                               time.sleep(1)
                        except ValueError:
                            print(' Lỗi cú pháp!')
                            time.sleep(1)
                        if devinput==0:
                            devloop=False
                        elif devinput==1:
                            textcolorchoicedisplay=textcolorchoice.removesuffix("\n")
                            textstylechoicedisplay=textstylechoice.removesuffix("\n")
                            textshadechoicedisplay=textshadechoice.removesuffix("\n")
                            bgcolorchoicedisplay=bgcolorchoice.removesuffix("\n")
                            bgshadechoicedisplay=bgshadechoice.removesuffix("\n")
                            DKTruNhapdisplay=DKTruNhap.removesuffix("\n")
                            DKthapphanNhapdisplay=DKthapphanNhap.removesuffix("\n")
                            roundtempdisplay=roundtemp.removesuffix("\n")
                            bsoddisplay=bsod.removesuffix("\n")
                            TitlePrint()
                            print("     GIÁ TRỊ ĐÃ LƯU:")
                            print("")
                            print(f"     - TextStyleChoice: {textstylechoicedisplay}")
                            print(f"     - TextShadeChoice: {textshadechoicedisplay}")
                            print(f"     - TextColorChoice: {textcolorchoicedisplay}")
                            print(f"     - BGShadeChoice: {bgshadechoicedisplay}")
                            print(f"     - BGColorChoice: {bgcolorchoicedisplay}")
                            print(f"     - AllowNegativeResult: {DKTruNhapdisplay}")
                            print(f"     - AllowFractionResult: {DKthapphanNhapdisplay}")
                            print(f"     - RoundingValue: {roundtempdisplay}")
                            print("     - AllowDeveloperOption: True")
                            print(f"     - BSODWhenCtrlC: {bsoddisplay}")
                            print('')
                            print('     Các giá trị này được lưu trong file log ở thư mục Data')
                            print('')
                            print('     Nhấn phím Enter để quay lại')
                            print('')
                            input(f'{null:-<65}')
                        elif devinput==2:
                            colortestloop=True
                            while colortestloop:
                                ApplySettings()
                                TitlePrint()
                                print("     KIỂM TRA HIỂN THỊ:")
                                print("")
                                print("     [0]: Quay lại")
                                print("")
                                print("     [1]: Hiển thị màu chữ")
                                print("")
                                print("     [2]: Hiển thị màu nền")
                                print("")
                                print("     [3]: Hiển thị kiểu chữ")
                                print("")
                                print("* Cài đặt màu sẽ tạm thời quay về mặc định sau khi chọn kiểm tra.")
                                print("  Khi thoát kiểm tra, cài đặt màu sẽ trở về bình thường.\n")
                                print(f"{null:-<65}")
                                print("")
                                colortestinput=str(input(" Lựa chọn (0-3) -> "))
                                try:
                                    colortestinput=int(colortestinput)
                                    if colortestinput not in [0,1,2,3]:
                                        print(' Số vừa nhập không hợp lệ!')
                                        time.sleep(1)
                                except ValueError:
                                    print(' Lỗi cú pháp!')
                                    time.sleep(1)
                                if colortestinput==0:
                                    colortestloop=False
                                elif colortestinput==1:
                                    print(Style.RESET_ALL)
                                    TitlePrint()
                                    print("      KIỂM TRA MÀU CHỮ")
                                    print("")
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
                                    print(" -  Màu không thể được chọn ở đây.")
                                    print(" -  Tên màu được lấy và dịch từ tên lệnh thực thi")
                                    print("(*) Tên màu được dịch từ Wikipedia Tiếng Việt")
                                    print('')
                                    print('https://pypi.org/project/colorama/ sẽ có thêm thông tin chi tiết!')
                                    print('Nhấn phím Enter để thoát')
                                    print('')
                                    input(f"{null:-<65}")
                                    LoadingScreen()
                                elif colortestinput==2:
                                    print(Style.RESET_ALL)
                                    TitlePrint()
                                    print("      KIỂM TRA MÀU NỀN")
                                    print("")
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
                                    print(" -  Màu không thể được chọn ở đây.")
                                    print(" -  Tên màu được lấy và dịch từ tên lệnh thực thi")
                                    print("(*) Tên màu được dịch từ Wikipedia Tiếng Việt")
                                    print('')
                                    print('https://pypi.org/project/colorama/ sẽ có thêm thông tin chi tiết!')
                                    print('Nhấn phím Enter để thoát')
                                    print('')
                                    input(f"{null:-<65}")
                                    LoadingScreen()
                                elif colortestinput==3:
                                    print(Style.RESET_ALL)
                                    TitlePrint()
                                    print("      KIẺM TRA KIỂU CHỮ")
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
                                    LoadingScreen()
                        elif devinput==3:
                            funloop=True
                            while funloop:
                                LogFileRead()
                                TitlePrint()
                                print("     CÀI ĐẶT VUI:")
                                print('')
                                print('     [0]: Quay lại')
                                print('')
                                print(f'     [1]: Hiển thị BSOD khi gặp lỗi ({bsodviet})')
                                print("")
                                print(f"{null:-<65}")
                                print("")
                                funinput=str(input(" Lựa chọn (0-1) -> "))
                                try:
                                    funinput=int(funinput)
                                    if funinput not in [0,1]:
                                        print(' Số vừa nhập không hợp lệ!')
                                        time.sleep(1)
                                except ValueError:
                                    print(' Lỗi cú pháp!')
                                    time.sleep(1)
                                if funinput==0:
                                    funloop=False
                                elif funinput==1:
                                    if bsodbool==False:
                                        data[9]="True"+"\n"
                                    else:
                                        data[9]="False"+"\n"
                                    with open("SaveFile.txt","w") as a:
                                        for lines in data:
                                            a.writelines(lines)
                elif inputexpect==5:
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
                                print('                       CẬP NHẬT PHẦN MỀM:')       
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
                                print('                       CẬP NHẬT PHẦN MỀM:')
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
                        ConnectionFailed()
                    except PermissionError:
                        TitlePrint()
                        print('                       CẬP NHẬT PHẦN MỀM:')
                        print('')
                        print('              Phần mềm không thể ghi lại bản cập nhật.')
                        print('        Hãy kiểm tra quyền truy cập ổ đĩa và/hoặc file sau:')
                        print(f'                 {updatedir}')
                        print('')
                        print('                    Nhấn phím Enter để thoát!')
                        print('')
                        input(f"{null:-<65}")
                if inputexpect==0:
                    settingsexit=True
                if inputexpect==5:
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
                            if mathsettingsinput==1:
                                print('     CÀI ĐẶT PHÉP CỘNG:')
                            else:
                                print('     CÀI ĐẶT PHÉP NHÂN:')
                            print('')
                            print('     Hiện tại tính năng này chưa có gì để chỉnh sửa.')
                            print("     Nhấn phím Enter để quay lại.")
                            print('')
                            input(f'{null:-<65}')
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
                                if DKthapphanNhap=="False"+"\n":
                                    print(f'     [2]: Tùy chỉnh giá trị làm tròn (Tắt)')
                                else:
                                    print(f'     [2]: Tùy chỉnh giá trị làm tròn (Hiện tại: {rounding})')
                                print("")
                                print(f"{null:-<65}")
                                print("")
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
                                    if DKthapphanNhap=="False"+"\n":
                                        data[6]="True"+"\n"
                                    else:
                                        data[6]="False"+"\n"
                                    with open("SaveFile.txt","w") as f:
                                        for lines in data:
                                            f.writelines(lines)
                                elif divisioninput==2:
                                    if DKthapphanNhap.title()=='False'+"\n":
                                        TitlePrint()
                                        print('                     TRUY CẬP BỊ TỪ CHỐI!')    
                                        print('')
                                        print(' Bạn phải bật "cho phép kết quả thập phân" để thay đổi tùy chọn ')
                                        print(' này!')
                                        print('')
                                        print(" Nhấn phím Enter để quay lại.")
                                        print("")
                                        print(f"{null:-<65}")
                                        input()
                                    else:
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
                                                    print(" Số vừa nhập không hợp lệ!")
                                                    time.sleep(1)
                                                elif rounding>5:
                                                    print(" Giá trị vượt quá giới hạn (Giá trị phải nhỏ hơn/bằng 5)")
                                                    time.sleep(1)
                                        except ValueError:
                                            print(' Lỗi cú pháp!')
                                            time.sleep(1)
                                        if rounding in [1,2,3,4,5]:
                                            data[7]=str(rounding)+"\n"
                                            with open("SaveFile.txt","w") as f:
                                                for lines in data:
                                                    f.writelines(lines)
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
                                    if DKTruNhap=="False"+"\n":
                                         data[5]="True"+"\n"
                                    else:
                                         data[5]="False"+"\n"
                                    with open("SaveFile.txt","w") as f:
                                        for lines in data:
                                            f.writelines(lines)
                elif inputexpect==4:
                    TitlePrint()
                    print("     THÔNG TIN HỆ THỐNG:")
                    print('')
                    print(f"     - Tên thiết bị: {platform.node()}")
                    print('')
                    print(f"     - Kiến trúc vi xử lý: {platform.machine()}")
                    print('')
                    print(f"     - Tên hệ điều hành: {platform.system()}")
                    print('')
                    print(f"     - Bản dựng: {platform.version()}")
                    print('')
                    print("     Nhấn phím Enter để quay lại")
                    print('')
                    input(f'{null:-<65}')
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
                        print("     [3]: Màu chữ + nền ngẫu nhiên")
                        print("")
                        print("     [4]: Đảo ngược màu")
                        print('')
                        print("     [5]: Khôi phục cài đặt gốc")
                        print('')
                        print("     [6]: Lưu ý")
                        print("")
                        print(f"{null:-<65}")
                        print("")
                        uiselect=str(input(" Lựa chọn (0-5) -> "))
                        textexit=False
                        bgexit=False
                        resetallexit=False
                        textstyleselect=3108
                        try:
                            uiselect=int(uiselect)
                            if uiselect not in [0,1,2,3,4,5,6]:
                                print(" Số vừa nhập không hợp lệ.")
                                time.sleep(1)
                        except ValueError:
                            print(" Lỗi cú pháp!")
                            time.sleep(1)
                        if uiselect==0:
                            repeat=False
                        if uiselect==6:
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
                            input(f"{null:-<65}")
                        if uiselect==1:
                            while textexit==False:
                                BundleTest()
                                TitlePrint()
                                print("     CÀI ĐẶT CHỮ:")
                                print('')
                                print('     [0]: Quay lại')
                                print('')
                                print(f'     [1]: Kiểu chữ (Hiện tại: {textstyleviet})')
                                print('')
                                print(f'     [2]: Độ đậm nhạt của chữ (Hiện tại: {textshadeviet})')
                                print('')
                                print(f'     [3]: Màu chữ (Hiện tại: {textcolorviet})')
                                print('')
                                print('     * Kiểu chữ sáng nhìn giống màu chữ nhạt')
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
                                    while textstyleexit==False:        
                                        BundleTest()
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
                                        except ValueError:
                                            print(" Lỗi cú pháp!")
                                            time.sleep(1)
                                        if textstyleselect==0:
                                            textstyleexit=True
                                            textexit=False
                                        if textstyleselect in [1,2,3,4]:
                                            if textstyleselect==1:
                                                textstylechoice='Dim'
                                            elif textstyleselect==2:
                                                textstylechoice='Normal'
                                            elif textstyleselect==3:
                                                textstylechoice='Bright'
                                            elif textstyleselect==4:
                                                textstylechoice='Special'
                                            data[0]=textstylechoice+"\n"
                                            with open("SaveFile.txt","w") as f:
                                                for lines in data:
                                                    f.writelines(lines)
                                if textselect==0:
                                    textexit=True
                                if textselect==2:
                                    while textshadeexit==False:
                                        BundleTest()
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
                                        except ValueError:
                                            print(" Lỗi cú pháp!")
                                            time.sleep(1)
                                        if textshadeselect==0:
                                            textshadeexit=True
                                            textexit=False
                                        if textshadeselect==1:
                                            data[1]='Light'+"\n"
                                        if textshadeselect==2:
                                            data[1]='Normal'+"\n"
                                        if textshadeselect in [1,2]:
                                            with open("SaveFile.txt","w") as f:
                                                for lines in data:
                                                    f.writelines(lines)
                                if textselect==3:
                                    while textcolorexit==False:
                                        BundleTest()
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
                                            if textcolortemp==bgcolorchoice.removesuffix("\n"):
                                                print(' Màu chữ bị trùng với màu nền!')
                                                time.sleep(1)
                                                textcolorexit=False                   
                                            else:
                                                data[2]=textcolortemp+"\n"
                                                with open("SaveFile.txt","w") as f:
                                                    for lines in data:
                                                        f.writelines(lines)
                        if uiselect==3:                            
                            textcolorchoice=random.choice(randomcolor)
                            bgcolorchoice=random.choice(randomcolor)
                            data[0]="Normal"+"\n"
                            data[1]="Normal"+"\n"
                            data[3]="Normal"+"\n"
                            while textcolorchoice==bgcolorchoice:
                                textcolorchoice=random.choice(randomcolor)
                                bgcolorchoice=random.choice(randomcolor)
                            data[2]=textcolorchoice+"\n"
                            data[4]=bgcolorchoice+"\n"
                            with open("SaveFile.txt","w") as f:
                                for lines in data:
                                    f.writelines(lines)
                        if uiselect==2:
                            BundleTest()
                            while bgexit==False:              
                                os.system(clrscr)
                                TitlePrint()
                                print("     CÀI ĐẶT NỀN:")
                                print('')
                                print('     [0]: Quay lại')
                                print('')
                                print(f'     [1]: Độ đậm nhạt của nền (Hiện tại: {bgshadeviet})')
                                print('')
                                print(f'     [2]: Màu nền (Hiện tại: {bgcolorviet})')
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
                                    while bgshadeexit==False:
                                        BundleTest()
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
                                        except ValueError:
                                            print(" Lỗi cú pháp!")
                                            time.sleep(1)
                                        if bgshadeselect==0:
                                            bgshadeexit=True
                                            bgexit=False
                                        if bgshadeselect==1:
                                            data[3]='Light'+"\n"                     
                                        if bgshadeselect==2:
                                            data[3]='Normal'+"\n"
                                        if bgshadeselect in [1,2]:
                                            with open("SaveFile.txt","w") as f:
                                                for lines in data:
                                                    f.writelines(lines)
                                if bgselect==2:
                                    while bgcolorexit==False:
                                        BundleTest()
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
                                            if textcolorchoice.removesuffix("\n")==bgcolortemp:
                                                print(' Màu nền trùng với màu chữ!')
                                                time.sleep(1)
                                            else:    
                                                data[4]=bgcolortemp+"\n"
                                                with open("SaveFile.txt","w") as f:
                                                    for lines in data:
                                                        f.writelines(lines)
                        if uiselect==5:
                            ApplySettings()
                            TitlePrint()
                            print("     LƯU Ý!")
                            print('')
                            print("     Bạn sẽ KHÔI PHỤC TẤT CẢ cài đặt giao diện về mặc định!")
                            print("     Bạn chắc chắn muốn tiếp tục không?")
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
                                SetColorToDefault()
                                ApplySettings()
                        if uiselect==4:
                            BundleTest()
                            TitlePrint()
                            print("     LƯU Ý!")
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
                                data[4],data[2]=data[2],data[4]
                                with open("SaveFile.txt","w") as f:
                                    for lines in data:
                                        f.writelines(lines)
                elif inputexpect==3:
                    TitlePrint()
                    print("     THÔNG TIN PHẦN MỀM:")
                    print('')
                    print("     - Phiên bản 1.4.5")
                    print('')
                    print(f'     - Phiên bản Python: {platform.python_version()}')
                    print('')
                    print("     Nhấn phím Enter để quay lại")
                    print('')
                    input(f"{null:-<65}")
        #Main Software
        if pt in [1,2,3,4,5]:
            multiple=3108
            codegen=False
            while settingsexit==False:
                if pt==1:
                    dau="+"
                    phep='cộng'
                elif pt==3:
                    dau="x"
                    phep='nhân'
                elif pt==2:
                    dau='-'
                    phep='trừ'
                elif pt==4:
                    dau=':'
                    phep='chia'
                else:
                    codegen=True
                    multiloop=True
                    while multiloop:
                        TitlePrint()
                        print('     Chọn phép toán mà bạn muốn có:')
                        print('')
                        print('     [0]: Quay lại')
                        print('')
                        print(f'     [1]: Cộng ({mathdata[0]})')
                        print('')
                        print(f'     [2]: Trừ ({mathdata[1]})')
                        print('')
                        print(f'     [3]: Nhân ({mathdata[2]})')
                        print('')
                        print(f'     [4]: Chia ({mathdata[3]})')
                        print("")
                        print("     Sau khi xong, nhập 'ok' để tiếp tục")
                        print('')
                        print(f"{null:-<65}")
                        print("")
                        multiple=str(input(" Nhập ở đây -> "))
                        try:
                            multiple=int(multiple)
                            if multiple==0:
                                multiloop=False
                                settingsexit=True
                                pt=0
                                break
                            elif multiple==1:
                                if mathdata[0]=="Bật":
                                    mathdata[0]="Tắt"
                                else:
                                    mathdata[0]="Bật"
                            elif multiple==2:
                                if mathdata[1]=="Bật":
                                    mathdata[1]="Tắt"
                                else:
                                    mathdata[1]="Bật"
                            elif multiple==3:
                                if mathdata[2]=="Bật":
                                    mathdata[2]="Tắt"
                                else:
                                    mathdata[2]="Bật"
                            elif multiple==4:
                                if mathdata[3]=="Bật":
                                    mathdata[3]="Tắt"
                                else:
                                    mathdata[3]="Bật"
                            else:
                                print(" Số vừa nhập không hợp lệ.")
                                time.sleep(1)
                        except ValueError:
                            if multiple.title()=="Ok":
                                if mathdata[0]=="Tắt" and mathdata[1]=="Tắt" and mathdata[2]=="Tắt" and mathdata[3]=="Tắt":
                                    print(" Phải bật ít nhất 1 phép tính để tiếp tục!")
                                    time.sleep(1)
                                else:
                                    multiloop=False
                            else:
                                print(" Giá trị không hợp lệ!")
                                time.sleep(1)
                if multiple==0:
                    break
                MathApply()
                TitlePrint()              
                if pt in [1,2,3,4]:
                    print(f"     * Phép {phep}:")
                else:
                    print("     Hỗn hợp")
                print("")
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
                            if pt in [1,2,3,4]:
                                print(f"     * Phép {phep}:")
                            else:
                                print("     Hỗn hợp")
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
                                        TitlePrint()
                                        if pt in [1,2,3,4]:
                                            print(f"     * Phép {phep}:\n")
                                        else:
                                            print("     Hỗn hợp\n")
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
                                                    if platform.system()=='Windows' and pt==5:
                                                        os.system("mode con cols=65 lines=36")
                                                    MathApply()
                                                    TitlePrint()
                                                    if pt in [1,2,3,4]:
                                                        print(f"     * Phép {phep}:\n")
                                                    else:
                                                        print("     Hỗn hợp\n")
                                                    print(f"     + Số bài toán bạn muốn thực hiện: {sbt}")
                                                    print('')
                                                    print(f"     + Giá trị lớn nhất của số a: {a}")
                                                    print('')
                                                    print(f"     + Giá trị lớn nhất của số b: {b}")
                                                    print('')
                                                    if pt==2:
                                                        print(f"     + Cho phép tạo phép tính với kết quả âm: {DKTru}")
                                                        print('')
                                                    elif pt==4:
                                                        print(f"     + Cho phép tạo phép tính với kết quả thập phân: {DKthapphan}")
                                                        print('')
                                                        if DKthapphanNhap=='True'+"\n":
                                                            print(f"     + Làm tròn tới số thập phân thứ {rounding}\n")
                                                    elif pt==5:
                                                        print(f"     Phép cộng: {mathdata[0]}\n")
                                                        print(f"     Phép trừ: {mathdata[1]}\n")
                                                        print(f"     Phép nhân: {mathdata[2]}\n")
                                                        print(f"     Phép chia: {mathdata[3]}\n")
                                                    print(f"     Cài đặt này ổn với bạn không?")
                                                    print('')
                                                    print("     [0]: Quay lại")
                                                    print('')
                                                    print("     [1]: Có")
                                                    print('')
                                                    print('     [2]: Không')
                                                    print('')
                                                    print(f"{null:-<65}")
                                                    print('')
                                                    confirminput=str(input(" Lựa chọn (0-2) -> "))
                                                    if (DKthapphan.title()=='Bật' and pt==4 and confirminput=='1') or (mathdata[3]=="Bật" and confirminput==1):
                                                        if platform.system()=='Windows':
                                                            os.system("mode con cols=65 lines=32")
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
                                                        if confirminput==2:
                                                            confirmsettings=True
                                                            ainputexit=True
                                                            binputexit=True
                                                            settingsexit=True
                                                        elif confirminput==0:
                                                            confirmsettings=True
                                                        elif confirminput not in [0,1,2]:
                                                            print(' Số vừa nhập không hợp lệ!')
                                                            time.sleep(1)
                                                        os.system(clrscr)
                                                        if confirminput==1:
                                                            if pt==5:
                                                                mathchoice=[1,2,3,4]
                                                                if mathdata[0]=="Tắt":
                                                                    mathchoice.remove(1)
                                                                if mathdata[1]=="Tắt":
                                                                    mathchoice.remove(2)
                                                                if mathdata[2]=="Tắt":
                                                                    mathchoice.remove(3)
                                                                if mathdata[3]=="Tắt":
                                                                    mathchoice.remove(4)
                                                            if platform.system()=='Windows':
                                                                os.system("mode con cols=65 lines=32")
                                                            while nq<=sbt:
                                                                if codegen==True:
                                                                    pt=random.choice(mathchoice)
                                                                c=random.randint(0,a)
                                                                d=random.randint(0,b)
                                                                if pt in [1,3]:
                                                                    c=random.randint(0,a)
                                                                    d=random.randint(0,b)
                                                                    if pt==1:
                                                                        dau="+"
                                                                        kqd=c+d
                                                                    else:
                                                                        dau="x"
                                                                        kqd=c*d
                                                                elif pt==2:
                                                                    if DKTruNhap=='False'+"\n":
                                                                        while c<d:
                                                                            c=random.randint(0,a)
                                                                            d=random.randint(0,b)
                                                                    else:
                                                                        c=random.randint(0,a)
                                                                        d=random.randint(1,b)
                                                                    dau="-"
                                                                    kqd=c-d
                                                                elif pt==4:
                                                                    if DKthapphanNhap=='False'+"\n":
                                                                        while c%d!=0:
                                                                            c=random.randint(0,a)
                                                                            d=random.randint(1,b)
                                                                        dau=":"
                                                                        kqd=round(c/d)
                                                                    elif DKthapphanNhap=="True\n":
                                                                        c=random.randint(0,a)
                                                                        d=random.randint(1,b)
                                                                        dau=":"
                                                                        kqd=round(c/d,rounding)
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
                                                                       print(" Giá trị không hợp lệ.")
                                                                nq+=1
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
                                                                    time.sleep(1)
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
                        if pt==5:
                            multiloop=True
                            settingsexit=False
                            pt=0
                        else:
                            settingsexit=True
                except ValueError:
                    print(" Giá trị không hợp lệ.")
                    time.sleep(1)
except KeyboardInterrupt:
    if bsod=="True"+"\n":
        BeginBSOD()
        print("KEYBOARD_INTERRUPT")
        time.sleep(0.05)
        print("")
        time.sleep(0.05)
        print("If this is the first time you've seen this stop error screen, restart this software. If this screen appears again, follow these steps:")
        time.sleep(0.05)
        print("")
        time.sleep(0.05)
        print("If the software launch normally, don't use Ctrl+C")
        time.sleep(0.05)
        print("")
        time.sleep(0.05)
        print("Technical information:")
        time.sleep(0.05)
        print("")
        time.sleep(0.05)
        print("*** STOP: KEYBOARD_INTERRUPT")
        time.sleep(0.05)
        print("")
        time.sleep(0.05)
        print("PRESS ENTER TO EXIT")
        time.sleep(0.05)
        input()
        sys.exit()
    else:    
        exitprogram()
except PermissionError:
    try:
        if bsod=="True"+"\n":
            BeginBSOD()
            print("PERMISSION_ERROR")
            time.sleep(0.05)
            print("")
            time.sleep(0.05)
            print("If this is the first time you've seen this stop error screen, restart this software. If this screen appears again, follow these steps:")
            time.sleep(0.05)
            print("")
            time.sleep(0.05)
            print("Check your file/disk permission. If it's read only, allow it to write in propeties.")
            time.sleep(0.05)
            print("")
            time.sleep(0.05)
            print("Technical information:")
            time.sleep(0.05)
            print("")
            time.sleep(0.05)
            print("*** STOP: PERMISSION_ERROR")
            time.sleep(0.05)
            print("")
            time.sleep(0.05)
            print("PRESS ENTER TO EXIT")
            time.sleep(0.05)
            input()
            sys.exit()
        else:
            TitlePrint()
            print('                           LỖI ĐỌC/GHI:')
            print('')
            print('               Phần mềm không thể ghi lại file log.')
            print(' Hãy kiểm tra quyền truy cập ổ đĩa và/hoặc file log của phần mềm.')
            print('')
            print('                    Nhấn phím Enter để thoát!')
            print('')
            input(f"{null:-<65}")
    except Exception:
        TitlePrint()
        print('                           LỖI ĐỌC/GHI:')
        print('')
        print('               Phần mềm không thể ghi lại file log.')
        print(' Hãy kiểm tra quyền truy cập ổ đĩa và/hoặc file log của phần mềm.')
        print('')
        print('                    Nhấn phím Enter để thoát!')
        print('')
        input(f"{null:-<65}")
except Exception:
    if bsod=="True"+"\n":
        BeginBSOD()
        print("UNEXPECTED_ERROR_DETECTED")
        time.sleep(0.05)
        print("")
        time.sleep(0.05)
        print("If this is the first time you've seen this stop error screen, restart this software. If this screen appears again, follow these steps:")
        time.sleep(0.05)
        print("")
        time.sleep(0.05)
        print("Let me know about this error. I will try to fix it.")
        time.sleep(0.05)
        print("")
        time.sleep(0.05)
        print("Technical information:")
        time.sleep(0.05)
        print("")
        time.sleep(0.05)
        print("*** STOP: UNEXPECTED_ERROR")
        time.sleep(0.05)
        print("")
        time.sleep(0.05)
        print("PRESS ENTER TO EXIT")
        time.sleep(0.05)
        input()
        sys.exit()
    else:    
        TitlePrint()
        print('                       LỖI KHÔNG XÁC ĐỊNH')
        print('')
        print('                Phần mềm gặp lỗi không xác định.')
        print(' Hãy báo cáo lỗi này để nó có thể khắc phục trong thời gian ngắn.\n')
        print('                    Nhấn phím Enter để thoát\n')
        input(f"{null:-<65}")
        sys.exit()
