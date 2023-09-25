def generate_candidates(prev_frequent_itemsets, k):
    candidates = []
    n = len(prev_frequent_itemsets)

    for i in range(n):
        for j in range(i + 1, n):
            itemset1 = prev_frequent_itemsets[i]
            itemset2 = prev_frequent_itemsets[j]

            # Gabungkan dua itemset jika k-1 item pertama sama
            if list(itemset1)[:k - 2] == list(itemset2)[:k - 2]:
                new_itemset = sorted(list(set(itemset1) | set(itemset2)))
                candidates.append(new_itemset)

    return candidates

def find_frequent_itemsets(transactions, min_support):
    unique_items = set(item for transaction in transactions for item in transaction)

    itemsets = {frozenset([item]): 0 for item in unique_items}

    for transaction in transactions:
        for item in unique_items:
            if item in transaction:
                itemsets[frozenset([item])] += 1

    frequent_itemsets = []
    for itemset, support in itemsets.items():
        if support >= min_support:
            frequent_itemsets.append(itemset)
            print(f"{itemset}: {support}")

    k = 2
    while frequent_itemsets:
        candidates = generate_candidates(frequent_itemsets, k)
        itemsets = {frozenset(candidate): 0 for candidate in candidates}

        for transaction in transactions:
            for itemset in itemsets.keys():
                if itemset.issubset(transaction):
                    itemsets[itemset] += 1

        frequent_itemsets = []
        for itemset, support in itemsets.items():
            if support >= min_support:
                frequent_itemsets.append(itemset)
                print(f"{itemset}: {support}")

        k += 1

transactions = [
    ["item1", "item2", "item5"],
    ["item2", "item4"],
    ["item2", "item3"],
    ["item1", "item2", "item4"],
    ["item1", "item3"],
    ["item2", "item3"],
    ["item1", "item3"],
    ["item1", "item2", "item3", "item5"],
]

min_support = 2 

print("Itemset yang sering muncul:")
find_frequent_itemsets(transactions, min_support)
