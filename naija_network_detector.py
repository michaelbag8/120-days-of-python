import re

def detect_nigerian_network(phone_number):
    """
    Detects the network provider of a Nigerian telephone number.
    
    Args:
        phone_number (str): The phone number to check
        
    Returns:
        str: The network provider name or 'Unknown' if not recognized
    """
   
    cleaned_number = re.sub(r'\D', '', phone_number)
    
  
    if cleaned_number.startswith('234'):
        cleaned_number = '0' + cleaned_number[3:]
   
    if not (len(cleaned_number) == 11 and cleaned_number.startswith('0')):
        return "Invalid Nigerian number format"
    
  
    prefix = cleaned_number[:4]
    
    # Define network prefixes
    networks = {
        # MTN Nigeria
        'MTN': [
            '0803', '0806', '0703', '0706', '0813', '0816', '0810', '0814',
            '0903', '0906', '0913', '0916', '07025', '07026', '0704'
        ],
        # Glo Nigeria
        'Glo': [
            '0805', '0807', '0705', '0703', '0815', '0811', '0905', '0915'
        ],
        # Airtel Nigeria
        'Airtel': [
            '0802', '0808', '0708', '0701', '0812', '0902', '0901', '0904', '0907', '0912'
        ],
        # 9mobile (Etisalat)
        '9mobile': [
            '0809', '0818', '0817', '0909', '0908'
        ],
        # Ntel (Fixed line but included for completeness)
        'Ntel': ['0804'],
        # Smile Communications
        'Smile': ['0702'],
        # Starcomms
        'starcomms': ["07028", "07029", "0819"],
        # Visafone
        'visafone': ["07025", "07026", "0704"],
        
        # Multilinks
        'multilinks': ["07027", "0709"],

        #Zoom
        'zoom': ["0707"]
    }
    
    # Check which network the prefix belongs to
    for network, prefixes in networks.items():
        if prefix in prefixes:
            return network
            
    return "Unknown network"

def main():
    """Main function to run the network detector"""
    print("Nigerian Mobile Network Detector")
    print("--------------------------------")
    
    while True:
        phone_number = input("\nEnter a Nigerian phone number (or 'quit' to exit): ").strip()
        
        if phone_number.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
            
        if not phone_number:
            print("Please enter a valid phone number")
            continue
            
        network = detect_nigerian_network(phone_number)
        print(f"Network: {network}")

if __name__ == "__main__":
    main()
