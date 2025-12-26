def is_trees_synchronized(tree1, tree2):
    if not tree1 and not tree2:
        return [True, None]

    if not tree1 or not tree2:
        return [False, None]

    value1 = tree1.get("value")
    value2 = tree2.get("value")

    if value1 != value2:
        return [False, value1]

    left1 = tree1.get("left")
    right1 = tree1.get("right")
    left2 = tree2.get("left")
    right2 = tree2.get("right")

    left_ok, _ = is_trees_synchronized(left1, right2)
    right_ok, _ = is_trees_synchronized(right1, left2)

    if left_ok and right_ok:
        return [True, value1]

    return [False, value1]
