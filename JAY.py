#Tlotliso Lekhoba
#0611275442088
#2BR
def validate_rfid(tag: str) -> bool:
    tag = tag.strip()
    return (
        len(tag) == 7 and
        tag[0].isdigit() and           
        tag[1].isalpha() and           
        tag[2:6].isdigit() and         
        tag[6] == 'Z'                  
    )

if __name__ == "__main__":
    tag = input("Enter the RFID tag: ")
    if validate_rfid(tag):
        print("RFID tag is valid.")
    else:
        print("RFID tag is invalid.")