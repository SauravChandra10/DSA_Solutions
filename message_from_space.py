'''
Problem statement:
You have received an encrypted message from space. Your task is to decrypt the message with the following simple rules:

Message string will consist of capital letters, numbers, and brackets only.

When there's a block of code inside the brackets, such as [10AB], it means you need to repeat the letters AB for 10 times.

Message can be embedded in multiple layers of blocks.

Final decrypted message will only consist of capital letters.

Create a function that takes encrypted message str and returns the decrypted message.

Examples
spaceMessage("ABCD")
output = "ABCD"

spaceMessage("AB[3CD]")
output = "ABCDCDCD"
# "AB" = "AB"
# "[3CD]" = "CDCDCD"
# Combine both = "ABCDCDCD"

spaceMessage("IF[2E]LG[5O]D")
output = "IFEELGOOOOOD"
'''

def spaceMessage(encrypted_str):
    i = 0
    result = ""
    
    while i < len(encrypted_str):
        # If the character is a letter (part of the message)
        if encrypted_str[i].isalpha():
            result += encrypted_str[i]
            i += 1
        # If we encounter an opening bracket
        elif encrypted_str[i] == '[':
            # Move past the opening bracket
            i += 1
            
            # Extract the repetition count
            repeat_count = ""
            while i < len(encrypted_str) and encrypted_str[i].isdigit():
                repeat_count += encrypted_str[i]
                i += 1
            
            repeat_count = int(repeat_count)
            
            # Find the content to be repeated (inside brackets)
            bracket_count = 1
            content_start = i
            
            while i < len(encrypted_str):
                if encrypted_str[i] == '[':
                    bracket_count += 1
                elif encrypted_str[i] == ']':
                    bracket_count -= 1
                    if bracket_count == 0:
                        break
                i += 1
            
            # Extract the content without the closing bracket
            content = encrypted_str[content_start:i]
            
            # Recursively decode the content
            decoded_content = spaceMessage(content)
            
            # Add the repeated content to the result
            result += decoded_content * repeat_count
            
        # Skip closing brackets (they're handled in the opening bracket section)
        elif encrypted_str[i] == ']':
            i += 1
        else:
            # For completeness, handle any other characters
            i += 1
    
    return result

print(spaceMessage("IF[2E]LG[5A[3O]]D"))