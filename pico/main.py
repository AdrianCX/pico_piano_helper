import wifi
import time

from ws_connection import ClientClosedError
from ws_server import WebSocketServer, WebSocketClient
from gradients import Gradient

class StateMachine:
    def __init__(self):
        self.gradient = Gradient()
        self.show_gradient()

    def show_gradient(self):
        self.showing = "gradient"
        self.gradient.show_gradient()
        
    def update(self):
        if self.showing == "gradient":
            self.gradient.update()
        else:
            try:
                elapsed=time.ticks_diff(time.ticks_ms(), self.start) / self.speed

                keyshown = False
                while elapsed + self.start_timeout >= self.timeout:
                    if self.on == 1:
                        self.gradient.show_key(self.note)
                        keyshown = True
                    elif self.on == 0:
                        self.gradient.clear_key(self.note)
                
                    self.readKey()
                    
                if keyshown:
                    self.start = self.start + self.minkeylength
                    
            except Exception as e:
                print("StateMachine::update exception:" + str(e))
                self.showing = "gradient"
                self.gradient.show_gradient()
                

    def readKey(self):
        current = self.f.readline().split(" ")
        self.timeout=int(current[0])
        self.note=int(current[1])
        self.on=int(current[2])

    def play(self, fileName, speed, minkeylength):
        try:
            self.minkeylength = minkeylength
            self.speed = 100.0 / speed
            self.showing = "keys"
            self.gradient.clear()
            self.f = open("songs/" + fileName, 'r')
            self.readKey()
            self.start = time.ticks_ms()
            self.start_timeout=self.timeout
        except Exception as e:
            print("StateMachine::play exception:" + str(e))
            self.showing = "gradient"
            self.gradient.show_gradient()

class TestClient(WebSocketClient):
    def __init__(self, conn):
        super().__init__(conn)

    def process(self):
        try:
            msg = self.connection.read()
            if not msg:
                return
            msg = msg.decode("utf-8")
            msg = msg.split("\n")[-2]
            msg = msg.split(" ")
            print(msg)

            if len(msg) >= 1 and msg[0] == "play":
                statemachine.play(msg[1] + ".txt", int(msg[2]), int(msg[3]))
            if len(msg) >= 1 and msg[0] == "gradient":
                statemachine.show_gradient()
                        
        except ClientClosedError:
            print("Connection close error")
            self.connection.close()
        except Exception as e:
            print("TestClient::process exception:" + str(e) + "\n")
            raise e

class TestServer(WebSocketServer):
    def __init__(self):
        super().__init__("index.html", 100)

    def _make_client(self, conn):
        return TestClient(conn)

wifi.run()

server = TestServer()
server.start()

statemachine = StateMachine()

while True:
    server.process_all()
    statemachine.update()

server.stop()

