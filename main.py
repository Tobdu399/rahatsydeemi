nums = {
    10: 0,  # Rahan suuruus ja niiden palautettava määrä
    5: 0,
    2: 0,
    1: 0,
}


def main():
    while True:
        try:
            total = int(input("Total > "))
            payment = int(input("Payment > "))
            break
        except ValueError:
            print("Use only integers\n")

    if total == payment:
        print("No change\n")
    else:
        payment = payment - total
        print(f"\nReturn: {payment}\n")

        for num in nums:
            reduction = payment//num
            payment -= reduction*num
            nums[num] = nums[num] + reduction

    for num in nums:
        print(f"Amount of {num}s: {nums[num]}")


if __name__ == "__main__":
    main()
