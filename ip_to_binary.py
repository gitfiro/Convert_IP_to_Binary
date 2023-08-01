def ip_to_binary(ip_address):
  """Converts an IP address to binary."""
  binary_string = ""
  for octet in ip_address.split("."):
    binary_string += format(int(octet), "08b")
  return binary_string


def binary_to_ip(binary_number):
  """Converts a binary number to IP address."""
  ip_address = ""
  for i in range(0, len(binary_number), 8):
    octet = binary_number[i:i + 8]
    ip_address += str(int(octet, 2)) + "."
  return ip_address[:-1]


def main():
  ip_address = input("Enter an IP address: ")
  binary_string = ip_to_binary(ip_address)
  binary_number = ip_to_binary(ip_address)
  print(f"The binary equivalent of {ip_address} is {binary_string}.")
  print(f"The IP address equivalent of {binary_number} is {binary_to_ip(binary_string)}.")


if __name__ == "__main__":
  main()
