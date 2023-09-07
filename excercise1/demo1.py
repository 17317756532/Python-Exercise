def count_and_replace_word(filename):
    word_count = 0
    new_content = ""
    occurrence = 0

    with open(filename, "r") as file:
        content = file.read()
        words = content.split()

        for word in words:
            if word.lower() == "terrible":
                word_count += 1

                if word_count % 2 == 0:
                    new_content += "pathetic "
                else:
                    new_content += "marvellous "
            else:
                new_content += word + " "

    # Write the modified content to result.txt
    with open("result.txt", "w") as file:
        file.write(new_content)

    return word_count


file_to_read = "file_to_read.txt"
total_occurrences = count_and_replace_word(file_to_read)
print("Total occurrences of 'terrible':", total_occurrences)
