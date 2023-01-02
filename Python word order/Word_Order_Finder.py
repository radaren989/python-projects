def Word_List(Book, Word_Order):
    try:
        with open("stop_words_english.txt", encoding="utf8") as stopR:
            stop_Words = stopR.read().split()
                
        file_Content = []    
        word = ""                     
        #Split words and put them in a list if they are not stop words                         
        with open(Book, encoding="utf8") as rf:
            whole_book = rf.read().strip(' ')
            for c in whole_book:
                c = c.lower().replace("’", "'")
                if c <= "z" and c >= "a" or c == "'":
                    word += c
                elif word != "" and word != "'":
                    if stop_Words.count(word) == 0:
                        file_Content.append(word)
                    word = ""
           
        return file_Content

    except FileNotFoundError:
        print(Book, "Not Found")


def Word_Order_Frequency_One_Book(Book, Word_Order, File_Output):
    try:
        file_Content = Word_List(Book, Word_Order)
        ordered_List = []
        #Makes a list acording to the word order 
        if Word_Order > 1:
            for i in range(len(file_Content) - Word_Order + 1):
                ordered_List.append(file_Content[i])
                for j in range(1, Word_Order):
                    ordered_List[i] += " " + file_Content[i + j]
        else:
            ordered_List = file_Content.copy()
        
        unique_List = list(dict.fromkeys(ordered_List.copy()))
        
        quantity_List = []
        for i in range(len(unique_List)):
            quantity_List.append(ordered_List.count(unique_List[i]))

        # Zip function combines two lists and makes a 2D list
        sorted_List = sorted(
            list(zip(quantity_List, unique_List)), reverse=True, key=lambda x: x[0]
        )

        with open(File_Output, "w") as wf:
            wf.write("<freq>|<word_list>\n")
            for i in range(len(sorted_List)):
                wf.write(
                    "{0: <6} | {1}\n".format(
                        str(sorted_List[i][0]), str(sorted_List[i][1])
                    )
                )

    except TypeError:
        print("Make sure you submit parameters correctly")

    except OSError:
        print("Make sure you submit parameters correctly")


def Word_Order_Frequency_Two_Books(Book_1, Book_2, Word_Order, File_Output):
    try:
        first_Word_List = Word_List(Book_1, Word_Order)
        second_Word_List = Word_List(Book_2, Word_Order)
        combined_List = first_Word_List + second_Word_List

        combined_Ordered_List = []
        first_Ordered_List = []
        second_Ordered_List = []
        #Makes a list acording to the word order 
        if Word_Order > 1:
            for i in range(len(combined_List) - Word_Order + 1):
                combined_Ordered_List.append(combined_List[i])
                for j in range(1, Word_Order):
                    combined_Ordered_List[i] += " " + combined_List[i + j]

            for i in range(len(first_Word_List) - Word_Order + 1):
                first_Ordered_List.append(first_Word_List[i])
                for j in range(1, Word_Order):
                    first_Ordered_List[i] += " " + first_Word_List[i + j]

            for i in range(len(second_Word_List) - Word_Order + 1):
                second_Ordered_List.append(second_Word_List[i])
                for j in range(1, Word_Order):
                    second_Ordered_List[i] += " " + second_Word_List[i + j]

        else:
            combined_Ordered_List = combined_List.copy()
            first_Ordered_List = first_Word_List.copy()
            second_Ordered_List = second_Word_List.copy()
            
            
        unique_List = list(dict.fromkeys(combined_Ordered_List.copy()))

        quantity_List = []        
        for x in unique_List:
            quantity_List.append(combined_Ordered_List.count(x))
  
        # Zip function combines two lists and makes a 2D list
        sorted_List = sorted(
            list(zip(quantity_List, unique_List)), reverse=True, key=lambda x: x[0]
        )

        with open(File_Output, "w") as wf:
            wf.write("<freq_total>|<freq_bk_1>|<freq_bk_2>|<word_list>\n")
            for i in range(len(sorted_List)):
                freq_one = first_Ordered_List.count(sorted_List[i][1])
                freq_two = second_Ordered_List.count(sorted_List[i][1])
                wf.write(
                    "{0: <11} | {1: <9} | {2: <9} | {3}\n".format(
                        str(sorted_List[i][0]),
                        str(freq_one),
                        str(freq_two),
                        sorted_List[i][1],
                    )
                )
        
    except TypeError:
        print("Make sure you submit parameters correctly")


    except OSError:
        print("Make sure you submit parameters correctly")
