PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as data:
    names_list = data.readlines()

with open ("./Input/Letters/starting_letter.txt", "r") as file:
    # read the file and form a paragraph string
    paragraph = file.read()

    # get the names from the file and replace them in the whole string
    for names in names_list:
        new_paragraph = paragraph.replace(PLACEHOLDER, names.strip("\n"))

        # for that name create a new file and add the paragraph
        with open(f"./Output/ReadyToSend/letter_for_{names.strip("\n")}.txt", "w") as letter_for_names:
            letter_for_names.write(new_paragraph)
