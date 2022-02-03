import tiny_dancer


def inp():
    for i in range(10):
        yield (0, i)


def double(x):
    return x * 2


def minus_one(x):
    return x - 1


def stringy(x):
    return f"<dance>{x}</dance>"


def peek(x):
    print(f"peekin at {x}")


def hax(x):
    h = hash(x)
    print(f"exchanged {x} with {h}")
    return h


ec = tiny_dancer.Executor()
flow = ec.Dataflow(inp())
flow.map(double)
flow.map(minus_one)
flow.map(stringy)
flow.inspect(peek)


if __name__ == "__main__":
    ec.build_and_run()
