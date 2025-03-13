# import re

# def check_password_strength(password):
#     score = 0
    
#     # Length Check
#     if len(password) >= 8:
#         score += 1
#     else:
#         print("❌ Password should be at least 8 characters long.")
    
#     # Upper & Lowercase Check
#     if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
#         score += 1
#     else:
#         print("❌ Include both uppercase and lowercase letters.")
    
#     # Digit Check
#     if re.search(r"\d", password):
#         score += 1
#     else:
#         print("❌ Add at least one number (0-9).")
    
#     # Special Character Check
#     if re.search(r"[!@#$%^&*]", password):
#         score += 1
#     else:
#         print("❌ Include at least one special character (!@#$%^&*).")
    
#     # Strength Rating
#     if score == 4:
#         print("✅ Strong Password!")
#     elif score == 3:
#         print("⚠️ Moderate Password - Consider adding more security features.")
#     else:
#         print("❌ Weak Password - Improve it using the suggestions above.")

# # Get user input
# password = input("Enter your password: ")
# check_password_strength(password)








 



# # password ki length check karega.

# def check_length(password):
#     if len(password) >= 8:
#         return True
#     else:
#         return False



# # Uppercase & Lowercase check karna.

# import re

# def check_case(password):
#     if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
#         return True
#     else:
#         return False



# #  Number (0-9) check karna.

# def check_digit(password):
#     if re.search(r"\d", password):   # \d → Ye regex pattern hai jo "koi bhi ek digit (0-9)" ko dhundta hai.
#         return True
#     else:
#         return False


# # special character (!@#$%^&*) check karega

# def check_special(password):
#     if re.search(r"{!@#$%^&*}", password):
#         return True
#     else:
#         return False




# # Get user input

# def check_password_strength(password):
#     if not check_length(password):
#         print("Weak password: Must be at least 8 characters long. ❌")
#     elif not check_case(password):
#         print("Weak password: Must contain both uppercase and lowercase letters. ❌")
#     elif not check_digit(password):
#         print("Medium password: Add at least one number for better security. 🟡")
#     elif not check_special(password):
#         print("Strong password: Try adding a special character for extra strength! 🟢")
#     else:
#         print("Very Strong password! 🔥✅")


# if __name__ == "__main__":
#     password = input("Enter your password: ")
#     check_password_strength(password)






import streamlit as st
import re
import random
import string

# Password Generator
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Password Strength Functions
def check_length(password):
    return len(password) >= 8

def check_case(password):
    return bool(re.search(r"[A-Z]", password) and re.search(r"[a-z]", password))

def check_digit(password):
    return bool(re.search(r"\d", password))

def check_special(password):
    return bool(re.search(r"[!@#$%^&*]", password))

# Blacklist of Common Passwords
weak_passwords = ["password", "123456", "qwerty", "password123", "abc123"]

def check_blacklist(password):
    return password not in weak_passwords

# Strength Checker
def check_password_strength(password):
    score = 0
    debug_info = []

    if not check_blacklist(password):
        return "❌ Very Weak! Choose another password."

    if check_length(password):
        score += 2
        debug_info.append("✅ Length is good")
    else:
        debug_info.append("❌ Too short")

    if check_case(password):
        score += 2
        debug_info.append("✅ Has uppercase & lowercase")
    else:
        debug_info.append("❌ Missing uppercase/lowercase")

    if check_digit(password):
        score += 1
        debug_info.append("✅ Has a digit")
    else:
        debug_info.append("❌ Missing a digit")

    if check_special(password):
        score += 3
        debug_info.append("✅ Has a special character")
    else:
        debug_info.append("❌ Missing special character")

    # Debugging output
    print("Debug Info:", debug_info)

    if score <= 2:
        return "Weak password ❌"
    elif score <= 4:
        return "Medium password ⚠️"
    elif score <= 6:
        return "Strong password ✅"
    else:
        return "Very Strong password! 🎉✅"

# Streamlit UI
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if st.button("Check Strength"):
    if password:
        result = check_password_strength(password)
        st.write(f"**Strength:** {result}")

        if "Weak" in result or "Very Weak" in result:
            suggested_password = generate_password()
            st.warning(f"🔑 Try this strong password: `{suggested_password}`")

        # Debugging output in UI
        st.write("🛠 Debugging Info: Check console for details.")

    else:
        st.error("Please enter a password.")
