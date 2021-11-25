# Caesar Cipher

def caesar_cipher():
    user_input = input("Please input your code: \n").strip().upper()
    shift = int(input("Please set your shift number: \n")) % 26
    flag = input("Encrypt or Decrypt?\n")
    result = ""
    original_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    shifted_list = []
    
    if flag == "E" or "encrypt" or "Encrypt":
        temp_list = []
        for item in original_list:
            if original_list.index(item) < shift:
                temp_list.append(item)
            else:
                shifted_list.append(item)
        for item in temp_list:
            shifted_list.append(item)
        buffer = []
        for letter in user_input:
            buffer.append(shifted_list[original_list.index(letter)])
        result = ''.join(buffer)

    # if flag == "D" or "decrypt" or "Decrypt":
    #     temp_list = []
    #     for item in original_list:
    #         if original_list.index(item) < shift:
    #             temp_list.append(item)
    #         else:
    #             shifted_list.append(item)
    #     for item in temp_list:
    #         shifted_list.append(item)
    #     buffer = []
    #     for letter in user_input:
    #         buffer.append(original_list[shifted_list.index(letter)])
    #     result = ''.join(buffer)
    
    print(f"Result: {result}")

caesar_cipher()