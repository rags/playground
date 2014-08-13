rev l = do_rev l []
    where
    do_rev [] acc = acc
    do_rev (x:xs) acc = do_rev xs (x:acc)