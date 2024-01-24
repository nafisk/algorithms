
def encode(self, input_strings: List[str]) -> str:
    encoded_string = ''
    for string in input_strings:
        encoded_string += str(len(string)) + '#' + string
    return encoded_string

def decode(self, encoded_string: str) -> List[str]:
    decoded_strings = []
    index = 0
    while index < len(encoded_string):
        # Find the length of the next string
        count_index = index
        while encoded_string[count_index] != '#':
            count_index += 1
        
        length = int(encoded_string[index:count_index])
        index = count_index + 1

        # Extract the string
        current_string = encoded_string[index: index + length]
        decoded_strings.append(current_string)
        index += length
    
    return decoded_strings
