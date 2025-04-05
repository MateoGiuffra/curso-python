
def battle_list(list_a, list_b): 
    if len(list_a) != len(list_b): 
        return "Las listas deben ser de la misma longitud"
      
    points = 0
    score = {
        "a": 0, 
        "b": 0
    }
    for i, a_num in enumerate(list_a):
        a_value = a_num + score["a"] 
        b_value = list_b[i] + score["b"]
        points = abs(a_value - b_value)
        if a_value > b_value: 
            score["a"] = points
            score["b"] = 0 
        else: 
            score["b"] = points
            score["a"] = 0 
    
    last_winner = "a" if score["a"] != 0 else "b"
    return "x" if points == 0 else f"{points}{last_winner}"

lista_a = [2, 4, 2]
lista_b = [3, 3, 4]
print(battle_list(lista_a, lista_b))