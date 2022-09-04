import random

#Dictionary of protocols and there ports
portsAndProtocols = {
    "FTP Data": 20,
    "FTP Commands": 21,
    "SSH": 22,
    "SFTP": 22,
    "Telnet": 23,
    "SMTP": 25,
    "DNS": 53,
    "DHCP (Server)": 67,
    "DHCP (Client)": 68,
    "TFTP": 69,
    "HTTP": 80,
    "POP3": 110,
    "NTP": 123,
    "NetBIOS Name Services (TCP)": 137,
    "NetBIOS Session Services (TCP)": 139,
    "NetBIOS Name Services (UDP)": 137,
    "NetBIOS Datagram Services (UDP)": 138,
    "IMAP": 143,
    "SNMP Managers to Agents": 161,
    "SNMP Agents to Managers": 162,
    "LDAP": 389,
    "SLP": 427,
    "HTTPS": 443,
    "SMB (TCP)": 445,
    "SMB Name Services (UDP)": 137,
    "SMB Datagram": 138,
    "SMB Session Service": 139,
    "Syslog": 514,
    "AFP": 548,
    "SMTP (TLS)": 587,
    "LDAP (SSL)": 636,
    "IMAP (SSL)": 993,
    "POP3 (SSL)": 995,
    "SQL Server": 1433,
    "SQL Net": 1521,
    "MySQL": 3306,
    "RDP": 3389,
    "SIP": 5060
}

#Placed everything in a while loop that allows you to choose the number of questions
questNum = input('How many questions would you like?\nPlease enter a number between 1-35: ')

#currentNum used to count questions answered
currentNum = 1

#Number of questions the user gets right
corrNum = 0

while currentNum <= int(questNum):

    #Pulls random protocol from list
    protocol = (random.choice(list(portsAndProtocols)))

    #Pulls the port number from the protocol selected above 
    port = (portsAndProtocols.get(protocol))

    #Asks what they think the port number is
    answer = input('What is the port number for ' + protocol + '? ')

    

    #If statement that compares answer with port number
    if int(answer) == int(port):
        print('Correct!')
        corrNum += 1

    else:
        print('Incorrect. It\'s port ' + str(port) + '.')

    currentNum += 1

#Variable to hold grade
gradeNum = ((int(corrNum)/int(questNum)) * 100)

#Prints how many correct out of total number of questions
print('You got ' + str(corrNum) + ' out of ' + str(questNum) + ' correct.\nThat\'s ' + str(gradeNum) + ' percent.')

#If statement that tells pass/fail
if gradeNum == 100:
    print('Perfect!')

elif gradeNum >= 80:
    print('You passed!')

else:
    print('Keep trying! Don\'t give up!')



#Add question asking what the initialism means 'What does SLP stand for?'
#Add question asking how protocol is used. 'How is SMB used?'
#Ask question with either Port, or protocol
#Add protocol info 'POP3' incoming mail, stores email locally
#Put portsAndProtocols definition in file and call
