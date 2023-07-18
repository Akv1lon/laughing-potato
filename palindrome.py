def palindrome_check(s):
    if s == s[::-1]:
        print(True)
    else: 
        print(False)

palindrome_check('лепсспел')
palindrome_check('helloworld')