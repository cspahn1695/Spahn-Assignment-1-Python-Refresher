def echo(text: str, repetitions: int = 3) -> str:
    """imitate a real world echo"""
    length = len(text) 

    for i in range(repetitions + 1, 1, -1):
        print(text[length-i+1:length] + '\n')

    print('.')

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))