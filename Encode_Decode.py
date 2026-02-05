def encode(msg):
    """Encodes a message with a simple transformation."""
    if(len(msg)<3):  # Reverse short messages
        li = list(msg)
        li.reverse()
        return "".join(li) 
    else:
        li = list(msg)
        char = li.pop(0)  # Remove first character
        li.append(char)   # Append it to the end
        li.insert(0, "ran")  # Add prefix
        li.append("dom")     # Add suffix
        return "".join(li)


def decode(code):
    """Decodes a previously encoded message."""
    if(len(code)<3):  # Reverse short messages
        li = list(code)
        li.reverse()
        return "".join(li) 
    else:
        # Remove prefix and suffix
        code = code.removeprefix("ran").removesuffix("dom")
        li = list(code)
        char = li.pop(-1)  # Remove last character
        li.insert(0, char) # Place it at the start
        return "".join(li)



print("=" * 40)
print("✨ Welcome to the Analyzer ✨")
print("=" * 40)
print()
print("Choose an option:")
print("  0 → Encode a message")
print("  1 → Decode a message")
print("-" * 40)

task = int(input("Enter your choice (0/1): "))
print("-" * 40)

match task: 
    case 0:
        msg = input("Enter the message to encode: ")
        code = encode(msg)
        print(f"✅ Encoded string: {code}")
    case 1 :
        code = input("Enter the code to decode: ")
        msg = decode(code)
        print(f"🔓 Decoded message: {msg}")
    case _:
        print("❌ Invalid choice. Please enter 0 or 1.")

print()
print("=" * 40)
print("🎉 Thank you for using the Analyzer!")
print("=" * 40)


