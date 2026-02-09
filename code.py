def main():
    A_str = "What are you doing while sending "  # 33 characters
    B_str = " Are you busy? Will you send "      # 29 characters
    f0_str = ("What are you doing at the end of the world? Are you busy? " +
              "Will you save us?")               # 75 characters

    q = int(input())
    results = []

    for _ in range(q):
        n, k = map(int, input().split())
        current_n = n
        current_k = k
        result = '.'  # default if not found

        while True:
  