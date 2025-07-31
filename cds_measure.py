import serial
import time
import signal
import threading
import sys

line = [] #라인 단위로 데이터 가져올 리스트 변수

port = 'COM6' # 시리얼 포트
baud = 9600 # 시리얼 보드레이트(통신속도)

global exitThread
exitThread = False   # 쓰레드 종료용 변수

f = open('cds_result/res.csv', 'w')

global start_t
start_t = 0

global csv
csv = 'time,A0 (RED),A1 (PURPLE),A2 (YELLOW),A3 (BLACK)'

#쓰레드 종료용 시그널 함수
def handler(signum, frame):
    print("SIGNAL : " + str(signum))
    f.write(csv)
    f.close()
    global exitThread
    exitThread = True
    sys.exit(0)


#데이터 처리할 함수
def parsing_data(data):
    # 리스트 구조로 들어 왔기 때문에
    # 작업하기 편하게 스트링으로 합침
    tmp = ''.join(data).replace('\n', '')

    global start_t

    try:
        itg = list(map(int, tmp.split('/')))

        t = time.time()-start_t
        a = itg[0]
        b = itg[1]
        c = itg[2]
        d = itg[3]

        global csv
        csv += f'\n{t},{a},{b},{c},{d}'

        #출력!
        print(t, itg[0], itg[1], itg[2], itg[3])
    except ValueError as e:
        print('Parse error:', e)

#본 쓰레드
def readThread(ser):
    global line
    global exitThread

    global start_t
    start_t = time.time()

    # 쓰레드 종료될때까지 계속 돌림
    while not exitThread:
        #데이터가 있있다면
        for c in ser.read():
            #line 변수에 차곡차곡 추가하여 넣는다.
            line.append(chr(c))

            if c == 10: #라인의 끝을 만나면.. (\n)
                #데이터 처리 함수로 호출
                parsing_data(line)

                #line 변수 초기화
                del line[:]    

signal.signal(signal.SIGINT, handler)
ser = serial.Serial(port, baud, timeout=0)
thread = threading.Thread(target=readThread, args=(ser,))
thread.start()

while not exitThread:
    time.sleep(0.1)