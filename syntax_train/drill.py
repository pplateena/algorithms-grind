"""Harness for the syntax drills. Not something you edit.

run() executes every check, and never stops at the first problem — a half-filled
file still reports everything it can:

    ..        not filled in yet (the method still raises NotImplementedError)
    ok        matched the expected value
    FAIL      ran, returned the wrong thing (expected vs got is printed)
    ERROR     raised something (the exception is printed)
"""


def run(checks, title=""):
    ok = fail = pending = 0
    width = max((len(c[0]) for c in checks), default=0)
    print(f"\n{title}")
    print("-" * (len(title) or 3))
    for label, fn, expected in checks:
        try:
            got = fn()
        except NotImplementedError:
            pending += 1
            print(f"  ..      {label}")
            continue
        except Exception as e:
            fail += 1
            print(f"  ERROR   {label:<{width}}  {type(e).__name__}: {e}")
            continue
        # subclasses pass (defaultdict/Counter for dict); list vs tuple and bool vs int don't
        same_kind = (isinstance(got, type(expected))
                     and (type(got) is bool) == (type(expected) is bool))
        if got == expected and same_kind:
            ok += 1
            print(f"  ok      {label:<{width}}  -> {got!r}")
        elif got == expected:
            fail += 1
            print(f"  FAIL    {label:<{width}}  right value, wrong type: "
                  f"expected {type(expected).__name__}, got {type(got).__name__} {got!r}")
        else:
            fail += 1
            print(f"  FAIL    {label:<{width}}  expected {expected!r}, got {got!r}")
    print(f"\n  {ok} ok · {fail} fail · {pending} pending")
    return fail
