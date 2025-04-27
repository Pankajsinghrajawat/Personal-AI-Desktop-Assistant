'''from feature import sendWhatsAppMsg

def whatsapp_command(query):
    try:
        if 'whatsapp message' in query:
            print("To whom do you want to send the message?")
            name = input("Enter Contact Name: ")

            print("What message do you want to send?")
            msg = input("Enter your Message: ")

            sendWhatsAppMsg(name, msg)
            
    except Exception as e:
        print(f"Something went wrong: {e}") '''

from feature import send_WhatsApp_message

if __name__ == "__main__":
    name = input("To whom do you want to send the message?\n")
    message = input("What message do you want to send?\n")
    send_WhatsApp_message(name, message)


