def mygen():
    loc =1
    print("loc is ",loc)
    yield loc
    loc +=1
    print("loc is ",loc)
    yield loc
    loc += 1
    print("loc is ", loc)
    yield loc
if __name__ == '__main__':
    mg= mygen()
    print(next(mg))
    print(next(mg))
    print(next(mg))
