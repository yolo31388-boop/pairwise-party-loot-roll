import pytest
import math
from gameplay import party_loot_roll as mod

CASES = [
    ("pool", 'm.pool(["a", "b"]) == ["a", "b"]'),
    ("roll", 'm.roll(7, 3) == 10'),
    ("weight", 'm.weight(True) == 2'),
    ("online", 'm.online(True) == 1'),
    ("atomic", 'm.atomic(["a"], "b") == ["a", "b"]'),
    ("lock", 'm.lock(False) is True'),
    ("reset", 'm.reset(0) == []'),
    ("rollback", 'm.rollback(["x"], ["a"]) == ["a"]'),
    ("record", 'm.record([1, 2]) == [1, 2]'),
    ("assign", 'm.can_assign("leader", "leader") is True'),
    ("seed", 'm.seed_for(1, 2) == "1:2"'),
    ("clamp", 'm.clamp_roll(120) == 99'),
    ("need", 'm.is_need("need") is True'),
    ("size", 'm.bag_size(["a", "b"]) == 2'),
    ("key", 'm.pool_key(5) == "loot:5"')
]

@pytest.mark.parametrize("name,expr", CASES, ids=[c[0] for c in CASES])
def test_contract(name, expr):
    assert eval(expr, {"m": mod, "approx": pytest.approx, "math": math})
