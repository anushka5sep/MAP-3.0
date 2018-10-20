# import socket
# #create an INET, STREAMing socket
# s = socket.socket(
#     socket.AF_INET, socket.SOCK_STREAM)
# #now connect to the web server on port 80
# # - the normal http port
# s.connect(('192.168.43.130', 3000))
# # print(x)
# s.send("Hi".encode())
# # import socket
# #
# # def client_program():
# #     message = input(" -> ")
# #     while message.lower().strip() != 'bye':
# #         s.send(message.encode())
# #         message = input(" -> ")
# #     client_socket.close()
# # if __name__ == '__main__':
# #     client_program()
# a


# Import socket module
# import socket
#
# # Create a socket object
# s = socket.socket()
#
# # Define the port on which you want to connect
# port = 3000
# #
# # connect to the server on local computer
# s.connect(('http://192.168.43.130', port))
# s.send("Hi")
# # receive data from the server
# # print s.recv(1024)
# # close the connection
# s.close()
#
# from socketIO_client import SocketIO
# # # x= " {\"KEY\" : \"XYZ\"}"
# with SocketIO('http://192.168.43.130', 3000) as socketIO:
#     socketIO.emit("x.encode()")
#     socketIO.wait(seconds=1)
#
# import requests
#
# # api-endpoint
# URL = "http://192.168.43.130:3000/hi";
#
# # sending get request and saving the response as response object
# r = requests.get(url = URL)
#
# print(r)

# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "http://192.168.43.243:3000/hi";

# data to be sent to api
data = {'api_dev_key':'API_KEY',
        'api_option':'paste',
        'api_paste_code':'source_code',
        'api_paste_format':'python'}

# sending post request and saving response as response object
r = requests.get(url = API_ENDPOINT, data = data)
