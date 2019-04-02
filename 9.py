def question9():
    """
    With splicing you can use the <step> number to skip items in the splice.
    e.g. my_list = [1, 2, 3, 4, 5, 6] then; my_list[0, 5, 2] => [1, 3, 5]
    Use splicing with a step to generate the sublist ["a", "c", "e", "h"]
    """

    l = ["a", "b", "c", "d", "e", "f", "g", "h"]
    a = l
    return a

assert question9() == ["a", "c", "e", "h"] 
