def benchmark(func, *args):
    import time

    t0 = time.time_ns()
    func(*args)
    tf = time.time_ns()
    totaltime = round((tf - t0) / 1e9, 5)
    a = str(args)
    a = a[: len(a) - 2]
    l = 40
    print(
        f"Function {func.__name__}{a if len(a) < l else a[: l - 10] + '... ' + a[len(a) - 10 : len(a)]}) completed in {totaltime}"
    )
