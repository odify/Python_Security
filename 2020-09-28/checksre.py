import httplib2
from sys import argv

h = httplib2.Http()

print("1- Enter a domain")
print("2 - From a list")
choice = input("Enter your choice:")

#input URLS:

redirect_payloads = ['/\google.com/', '///www.google.com/%2e%2e', '//youtube.com/%2F..', '//www.yahoo.com//', '//www.yahoo.com/%2F%2E%2E','//attreya.in/', '///www.yahoo.com/%2F%2E%2E'
]

if choice == '2':
    filename = input("Please enter the name of a file: ")
    for payload in redirect_payloads:
        with open(filename) as f:
            for line in f:
                url = 'http://'+line.rstrip()
                try:
                    resp,content = h.request(url)
                   

                    if resp.status == 301:# and resp.status <=400:
                        print('Redirect at: '+ url)
                        
                except:
                    print("Error at: "+url)

elif choice == '1':
    domain_name = input("Please enter the domain name: ")
    for payload in redirect_payloads:
        url = 'http://'+domain_name+payload
        try:
                    resp,content = h.request(url)
                    print(resp.status)
                    if resp.status >= 300 and resp.status <=400:
                        print('Redirect at: '+ url)
                       
        except:
                    print("Error at: "+url)

else:
    print("Failed")
