message = 'MSH|^~\&|GHH LAB|ELAB-3|GHH OE|BLDG4|200202150930||ORU^R01|CNTRL-3456|P|2.4\r'
message += 'PID|||555-44-4444||EVERYWOMAN^EVE^E^^^^L|JONES|196203520|F|||153 FERNWOOD DR.^^STATESVILLE^OH^35292||(206)3345232|(206)752-121||||AC555444444||67-A4335^OH^20030520\r'
message += 'OBR|1|845439^GHH OE|1045813^GHH LAB|1554-5^GLUCOSE|||200202150730||||||||555-55-5555^PRIMARY^PATRICIA P^^^^MD^^LEVEL SEVEN HEALTHCARE, INC.|||||||||F||||||444-44-4444^HIPPOCRATES^HOWARD H^^^^MD\r'
message += 'OBX|1|SN|1554-5^GLUCOSE^POST 12H CFST:MCNC:PT:SER/PLAS:QN||^182|mg/dl|70_105|H|||F'
message += 'ROL|45^RECORDER^ROLE MASTER LIST|AD|CP|KATE^SMITH^ELLEN|199505011201'
message += 'DG1|1|I9|71596^OSTEOARTHROS NOS-L/LEG ^I9|OSTEOARTHROS NOS-L/LEG ||A|'

'''
NK1|1|DUCK^HUEY|SO|3583 DUCK RD^^FOWL^CA^999990000|8885552222||Y||||||||||||||
PV1|1|I|PREOP^101^1^1^^^S|3|||37^DISNEY^WALT^^^^^^AccMgr^^^^CI|||01||||1|||37^DISNEY^WALT^^^^^^AccMgr^^^^CI|2|40007716^^^AccMgr^VN|4|||||||||||||||||||1||G|||20050110045253||||||
GT1|1|8291|DUCK^DONALD^D||111^DUCK ST^^FOWL^CA^999990000|8885551212||19241010|M||1|123121234||||#Cartoon Ducks Inc|111^DUCK ST^^FOWL^CA^999990000|8885551212||PT|
DG1|1|I9|71596^OSTEOARTHROS NOS-L/LEG ^I9|OSTEOARTHROS NOS-L/LEG ||A|
IN1|1|MEDICARE|3|MEDICARE|||||||Cartoon Ducks Inc|19891001|||4|DUCK^DONALD^D|1|19241010|111^DUCK ST^^FOWL^CA^999990000|||||||||||||||||123121234A||||||PT|M|111 DUCK ST^^FOWL^CA^999990000|||||8291
IN2|1||123121234|Cartoon Ducks Inc|||123121234A|||||||||||||||||||||||||||||||||||||||||||||||||||||||||8885551212
'''


'''
MSH|^~\&||.|||199908180016||ADT^A04|ADT.1.1698593|P|2.7
PID|1||000395122||LEVERKUHN^ADRIAN^C||19880517180606|M|||6 66TH AVE NE^^WEIMAR^DL^98052||(157)983-3296|||S||12354768|87654321
NK1|1|TALLIS^THOMAS^C|GRANDFATHER|12914 SPEM ST^^ALIUM^IN^98052|(157)883-6176
NK1|2|WEBERN^ANTON|SON|12 STRASSE MUSIK^^VIENNA^AUS^11212|(123)456-7890
IN1|1|PRE2||LIFE PRUDENT BUYER|PO BOX 23523^WELLINGTON^ON^98111|||19601||||||||THOMAS^JAMES^M|F|||||||||||||||||||ZKA535529776

Where,
The above message is divided into four different types of segments: MSH, PID, NK1 and IN1.
A segment contains fields separated by the | field separator. Fields can be further separated by ^, the so-called component separator, and contain sub-components denoted by the & symbol.
MSH (Message Header) tells the purpose of the message, e.g. its ID, seeding application, sending facility, receiving application, receiving facility, the type, date and time of the message, its HL7 version, etc...
PID (Patient Identification) holds information about the patient e.g. their ID, name, DOB, address, gender, race, admission date and time etc..
NK1 (Next of Kin) contains details of the person's closest relative/friend.
IN1 (Insurance 1) has details about the health insurance the patient has like Medicare, Medicaid, Tricare, etc. It contains the insurance plan ID, the name of the insurance company, the company's address, the name of the insured person, policy number etc...

'''

'''
MSH|^~\&|AccMgr|1|||20050110045504||ADT^A01|599102|P|2.3||| EVN|A01|20050110045502||||| PID|1||10006579^^^1^MRN^1||DUCK^DONALD^D||19241010|M||1|111 DUCK ST^^FOWL^CA^999990000^^M|1|8885551212|8885551212|1|2||40007716^^^AccMgr^VN^1|123121234|||||||||||NO NK1|1|DUCK^HUEY|SO|3583 DUCK RD^^FOWL^CA^999990000|8885552222||Y|||||||||||||| PV1|1|I|PREOP^101^1^1^^^S|3|||37^DISNEY^WALT^^^^^^AccMgr^^^^CI|||01||||1|||37^DISNEY^WALT^^^^^^AccMgr^^^^CI|2|40007716^^^AccMgr^VN|4|||||||||||||||||||1||G|||20050110045253|||||| GT1|1|8291|DUCK^DONALD^D||111^DUCK ST^^FOWL^CA^999990000|8885551212||19241010|M||1|123121234||||#Cartoon Ducks Inc|111^DUCK ST^^FOWL^CA^999990000|8885551212||PT| DG1|1|I9|71596^OSTEOARTHROS NOS-L/LEG ^I9|OSTEOARTHROS NOS-L/LEG ||A| IN1|1|MEDICARE|3|MEDICARE|||||||Cartoon Ducks Inc|19891001|||4|DUCK^DONALD^D|1|19241010|111^DUCK ST^^FOWL^CA^999990000|||||||||||||||||123121234A||||||PT|M|111 DUCK ST^^FOWL^CA^999990000|||||8291 IN2|1||123121234|Cartoon Ducks Inc|||123121234A|||||||||||||||||||||||||||||||||||||||||||||||||||||||||8885551212 IN1|2|NON-PRIMARY|9|MEDICAL MUTUAL CALIF.|PO BOX 94776^^HOLLYWOOD^CA^441414776||8003621279|PUBSUMB|||Cartoon Ducks Inc||||7|DUCK^DONALD^D|1|19241010|111 DUCK ST^^FOWL^CA^999990000|||||||||||||||||056269770||||||PT|M|111^DUCK ST^^FOWL^CA^999990000|||||8291 IN2|2||123121234|Cartoon Ducks Inc||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||8885551212 IN1|3|SELF PAY|1|SELF PAY|||||||||||5||1

'''
import hl7
h = hl7.parse(message)

type(h)
print(h)
str(h) == message

isinstance(h, list)

print(len(h))

print ('********************* \n')
print ('line0 -- > ', h[0])
print ('********************* \n')
print ('********************* \n')
print ('line1 -- > ', h[1])
print ('********************* \n')
print ('********************* \n')
print ('line2 -- > ', h[2])
print ('********************* \n')
print ('********************* \n')
print ('line3 -- > ', h[3])
print ('********************* \n')
print(h[3][3][0][1][0] is h(4)(3)(1)(2)(1))
print(h[3][3][0][1][0])
print ('********************* \n')
print(h['OBX'][0][3][0][1][0] is h['OBX'](1)(3)(1)(2)(1))
print(h['OBX'][0][3][0][1][0])
print ('********************* \n')
print(h.segment('PID')[3][0] is h.segment('PID')(3)(1))
print(h[4])
##
## h[3] is h(4)
##
## h[3][0]
##
## h[3][1]
##
## h[3][2]
##
## h(4)(2)
##
## str(h[3])
##
## h[3][3][0][1][0]
##
## h[3][3][0][1][0] is h(4)(3)(1)(2)(1)
##
## h[3][5][0][1][0]
##
## h[3][5][0][1][0] is h(4)(5)(1)(2)(1)
##
## h.segments('OBX')[0][3][0][1][0]
##
## h['OBX'][0][3][0][1][0]
##
## h['OBX'][0][3][0][1][0] is h['OBX'](1)(3)(1)(2)(1)
##
## h.segment('PID')[3][0]
##
## h.segment('PID')[3][0] is h.segment('PID')(3)(1)
##
## type(h)
##
## type(h[3])
##
## type(h[3][3])
##
## type(h[3][3][0])
##
## type(h[3][3][0][1])
##
## type(h[3][3][0][1][0])
##
## type(h[3][1])
##
## type(h[3][1][0])
