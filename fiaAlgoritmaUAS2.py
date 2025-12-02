from collections import deque

stack = deque()

while True:
    print("\n=== PROGRAM STACK ===")
    print("1. Append")
    print("2. AppendLeft")
    print("3. Pop")
    print("4. PopLeft")
    print("5. Clear")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        data = input("Masukkan data: ")
        stack.append(data)
        print("Data berhasil ditambahkan:", data)

    elif pilihan == "2":
        data = input("Masukkan data: ")
        stack.appendleft(data)
        print("Data berhasil ditambahkan di kiri:", data)

    elif pilihan == "3":
        if len(stack) > 0:
            print("Data terambil (Pop):", stack.pop())
        else:
            print("Stack kosong!")

    elif pilihan == "4":
        if len(stack) > 0:
            print("Data terambil (PopLeft):", stack.popleft())
        else:
            print("Stack kosong!")

    elif pilihan == "5":
        stack.clear()
        print("Stack telah dikosongkan.")

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")