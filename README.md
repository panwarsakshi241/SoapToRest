# SoapToRest
Soap to rest conversion using wsdl in python
I've  used SUDS lib to convert the soap to rest. you can use zeep also, but i faced some lxml tree issue on aws packaging so i had to change. Anyway both are reliable.

I've hosted my code on lambda function bundled with api gateway. So there's is few code written which might not be useful based on your usecase. 

for me event={'parameter':'10'} is something similar to this. 
url will be your wsdl location. e.g. https://example.com?.wsdl 

After fetching the parameter from the event i'm validating the payload too. Its better to think every edge scenario before putting the thoughts into code.

Happy Coding !!!

