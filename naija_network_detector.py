import re

NETWORK_PREFIXES = {
    "MTN": (
        "0803", "0806", "0703", "0706", "0813", "0816", "0810", "0814",
        "0903", "0906", "0913", "0916", "0704"
    ),
    "Glo": (
        "0805", "0807", "0705", "0815", "0811", "0905", "0915"
    ),
    "Airtel": (
        "0802", "0808", "0708", "0701", "0812", "0902", "0901",
        "0904", "0907", "0912"
    ),
    "9mobile": ("0809", "0818", "0817", "0909", "0908"),
    "Ntel": ("0804",),
    "Smile": ("0702",),
    "visafone": ("07025", "07026"),
    "multilinks": ("07027", "0709"),
    "starcomms": ("07028", "07029", "0819"),
    "zoom": ("0707",),
}


def normalize_phone_number(phone_number):
    """Strip non-digits and normalize the Nigerian format."""
    cleaned_number = re.sub(r"\D", "", phone_number)

    if cleaned_number.startswith("234"):
        cleaned_number = "0" + cleaned_number[3:]

    return cleaned_number


def detect_nigerian_network(phone_number):
    """Return the network provider for a Nigerian mobile number."""
    cleaned_number = normalize_phone_number(phone_number)

    if not (len(cleaned_number) == 11 and cleaned_number.startswith("0")):
        return "Invalid Nigerian number format"

    sorted_prefixes = sorted(
        (
            prefix
            for network_prefixes in NETWORK_PREFIXES.values()
            for prefix in network_prefixes
        ),
        key=len,
        reverse=True,
    )

    for prefix in sorted_prefixes:
        if cleaned_number.startswith(prefix):
            for network_name, network_prefixes in NETWORK_PREFIXES.items():
                if prefix in network_prefixes:
                    return network_name

    return "Unknown network"


def main():
    """Main function to run the network detector."""
    print("Nigerian Mobile Network Detector")
    print("--------------------------------")

    while True:
        phone_number = input("\nEnter a Nigerian phone number (or 'quit' to exit): ").strip()

        if phone_number.lower() in {"quit", "exit", "q"}:
            print("Goodbye!")
            break

        if not phone_number:
            print("Please enter a valid phone number")
            continue

        network = detect_nigerian_network(phone_number)
        print(f"Network: {network}")


if __name__ == "__main__":
    main()
