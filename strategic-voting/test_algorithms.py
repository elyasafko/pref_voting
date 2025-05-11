"""
Pytest unit tests for the Strategic-Voting stubs.
All tests are xfail until real implementations are provided.
"""
import math
import random

import pytest
from strategic_voting_algorithms import (
    algorithm1_single_voter,
    algorithm2_coalitional,
)

def dummy_F(profile):
    # Identity SWF for zero‐candidate toy cases.
    return profile[0] if profile else []


#---Algorithm 1---

@pytest.mark.xfail(reason="stub – Algorithm 1 not yet implemented")
def test_algorithm1_empty_input():
    ok, vote = algorithm1_single_voter(dummy_F, [], [], 'p')
    assert not ok and vote is None

@pytest.mark.xfail(reason="stub – Algorithm 1 not yet implemented")
def test_algorithm1_threshold_case():
    # if pos(p, po) < ceil(m/2) ⇒ immediate False
    F = lambda prof: []
    team_profile = [['p','a','b']]          # m=3
    opponent_order = ['p','a','b']          # pos(p)=1 < ceil(3/2)=2
    success, vote = algorithm1_single_voter(F, team_profile, opponent_order, 'p')
    assert not success and vote is None

@pytest.mark.xfail(reason="stub – Algorithm 1 not yet implemented")
def test_algorithm1_simple_case_1():
    # “5-candidate” example (4 honest voters + 1 manipulator)
    F_borda = lambda prof: prof[0]  # placeholder SWF
    team_profile = [
        ['b','a','c','p'], # p>c>a>b
        ['c','a','b','p'], # p>b>a>c
        ['c','a','p','b'], # b>p>a>c
        ['p','c','a','b'], # b>a>c>p
    ]
    opponent_order = ['c','a','p','b'] # b>p>a>c
    success, vote = algorithm1_single_voter(F_borda, team_profile, opponent_order, 'p')
    assert success                     # should find a manipulation
    # returned vote must be a full ranking over the 4 candidates
    assert vote == ['b','c','p','a'] # a>p>c>b

@pytest.mark.xfail(reason="stub – Algorithm 1 not yet implemented")
def test_algorithm1_simple_case_2():
    # “4-candidate” example (3 honest voters + 1 manipulator)
    F_borda = lambda prof: prof[0]  # placeholder SWF
    team_profile = [
        ['c','b','a','p'], # p>a>b>c
        ['c','a','p','b'], # b>p>a>c
        ['c','a','p','b'], # b>p>a>c
    ]
    opponent_order = ['c','a','b','p'] # p>b>a>c
    success, vote = algorithm1_single_voter(F_borda, team_profile, opponent_order, 'p')
    assert success                     # should find a manipulation
    # returned vote must be a full ranking over the 5 candidates
    assert vote == ['b','c','p','a'] # a>p>c>b

@pytest.mark.xfail(reason="stub – Algorithm 1 not yet implemented")
def test_algorithm1_simple_case_3():
    # low rate by other team
    F_borda = lambda prof: prof[0]  # placeholder SWF
    team_profile = []
    opponent_order = ['p','c','a','b'] # b>a>c>p
    success, vote = algorithm1_single_voter(F_borda, team_profile, opponent_order, 'p')
    assert not success and vote is None

@pytest.mark.xfail(reason="stub – Algorithm 1 not yet implemented")
def test_algorithm1_simple_case_3():
    # “11-candidate” example (10 honest voters + 1 manipulator)
    F_borda = lambda prof: prof[0]  # placeholder SWF
    team_profile = [
        # 6 voters exactly follow pt
        ['g', 'f', 'e', 'p', 'd', 'c', 'a', 'b'],
        ['g', 'f', 'e', 'p', 'd', 'c', 'a', 'b'],
        ['g', 'f', 'e', 'p', 'd', 'c', 'a', 'b'],
        ['g', 'f', 'e', 'p', 'd', 'c', 'a', 'b'],
        ['g', 'f', 'e', 'p', 'd', 'c', 'a', 'b'],
        ['g', 'f', 'e', 'p', 'd', 'c', 'a', 'b'],
        ['g', 'f', 'e', 'p', 'd', 'c', 'b', 'a'],
        ['g', 'f', 'e', 'p', 'd', 'b', 'c', 'a'],
        ['g', 'f', 'e', 'p', 'd', 'a', 'b', 'c'],
        ['g', 'f', 'e', 'p', 'a', 'b', 'c', 'd'],
    ]

    opponent_order = ['g','f','e','d','c','p','a','b'] # b>a>p>c>d>e>f>g
    success, vote = algorithm1_single_voter(F_borda, team_profile, opponent_order, 'p')
    assert success                     # should find a manipulation
    # returned vote must be a full ranking over the 10 candidates
    assert vote == ['b','a','e','f','g','c','d','p'] # p>d>c>g>f>e>a>b

@pytest.mark.xfail(reason="stub – Algorithm 1 not yet implemented")
def test_algorithm1_random_threshold_guard():
    """
    If opponent’s rank(pos(preferred)) < ceil(m/2),
    algorithm1 must immediately return (False, None).
    """
    for _ in range(20):
        # pick between 3 and 10 candidates
        m = random.randint(3, 10)
        # build a candidate list ['a','b',...]
        candidates = [chr(ord('a') + i) for i in range(m)]
        preferred = random.choice(candidates)

        # force preferred into opponent_order at a 'too‐low' position
        pos = random.randint(0, math.ceil(m/2) - 2)
        others = [c for c in candidates if c != preferred]
        random.shuffle(others)
        opponent_order = others.copy()
        opponent_order.insert(pos, preferred)

        # random honest team of up to 5 voters
        team_profile = [
            random.sample(candidates, k=m)
            for __ in range(random.randint(0, 5))
        ]

        ok, vote = algorithm1_single_voter(dummy_F, team_profile, opponent_order, preferred)
        assert not ok and vote is None

@pytest.mark.xfail(reason="stub – Algorithm 1 not yet implemented")
def test_algorithm1_random_output_shape():
    """
    Whenever algorithm1 reports success, the returned 'vote' must
    be a full permutation of the candidates.
    """
    for _ in range(20):
        # any random profile & opponent_order
        m = random.randint(3, 8)
        candidates = [chr(ord('a') + i) for i in range(m)]
        preferred = random.choice(candidates)
        opponent_order = random.sample(candidates, k=m)
        team_profile = [
            random.sample(candidates, k=m)
            for __ in range(random.randint(0, 4))
        ]

        ok, vote = algorithm1_single_voter(dummy_F, team_profile, opponent_order, preferred)
        if ok:
            # must be a permutation of the candidate set
            assert sorted(vote) == sorted(candidates)

#---Algorithm 2---

@pytest.mark.xfail(reason="stub – Algorithm 2 not yet implemented")
def test_algorithm2_zero_manipulators():
    ok, prof = algorithm2_coalitional(dummy_F, [], [], 'p', k=0)
    assert not ok and prof is None

@pytest.mark.xfail(reason="stub – Algorithm 2 not yet implemented")
def test_algorithm2_threshold_case():
    # same threshold guard as Algorithm 1
    F = lambda prof: prof[0]
    team_profile = []      # irrelevant, pos(p) check happens first
    opponent_order = ['p','c','b','a'] # a>b>c>p
    success, votes = algorithm2_coalitional(F, team_profile, opponent_order, 'p', k=2)
    assert not success and votes is None

@pytest.mark.xfail(reason="stub – Algorithm 2 not yet implemented")
def test_algorithm2_simple_1approval_case_1():
    # CC-MaNego example with X-approval (x=2), O={a,b,c,d,e,p}, k=2
    F_1app = lambda prof: prof[0]
    team_profile = [
        ['e','c','b','a','d','p'],   # p>d>a>b>c>e
        ['e','d','c','b','p','a'],   # a>p>b>c>d>e
        ['e','d','p','a','c','b'],   # b>c>a>p>d>e
    ]
    opponent_order = ['e','d','c','b','p','a'] # a>p>b>c>d>e
    success, votes = algorithm2_coalitional(F_1app, team_profile, opponent_order, 'p', k=2)
    assert success
    # must return exactly k votes, each a full ranking
    assert isinstance(votes, list) and len(votes) == 2
    assert votes == [['a','b','c','d','e','p'],['a','b','d','e','p','c']]


@pytest.mark.xfail(reason="stub – Algorithm 2 not yet implemented")
def test_algorithm2_simple_1approval_case_1():
    # CC-MaNego example with X-approval (X=1), O={a,b,c,p}, k=2
    F_1app = lambda prof: prof[0]
    team_profile = [
        ['c','b','p','a'],   # a>p>b>c
        ['p','c','a','b'],   # b>a>c>p
    ]
    opponent_order = ['a','b','c','p'] # p>c>b>a
    success, votes = algorithm2_coalitional(F_1app, team_profile, opponent_order, 'p', k=2)
    assert success
    # must return exactly k votes, each a full ranking
    assert isinstance(votes, list) and len(votes) == 2
    assert votes == [['a','b','c','p'],['a','b','c','p']] # p>c>b>a


@pytest.mark.xfail(reason="stub – Algorithm 2 not yet implemented")
def test_algorithm2_random_threshold_guard():
    """
    Same guard as Algorithm 1: If pos(preferred) < ceil(m/2), even a coalition
    of size k>0 cannot succeed.
    """
    for _ in range(20):
        m = random.randint(3, 10)
        candidates = [chr(ord('a') + i) for i in range(m)]
        preferred = random.choice(candidates)
        pos = random.randint(0, math.ceil(m/2) - 2)
        others = [c for c in candidates if c != preferred]
        random.shuffle(others)
        opponent_order = others.copy()
        opponent_order.insert(pos, preferred)

        # pick a coalition size between 1 and 4
        k = random.randint(1, min(4, len(candidates)))
        team_profile = [
            random.sample(candidates, k=m)
            for __ in range(random.randint(0, 5))
        ]

        ok, votes = algorithm2_coalitional(dummy_F, team_profile, opponent_order, preferred, k)
        assert not ok and votes is None


@pytest.mark.xfail(reason="stub – Algorithm 2 not yet implemented")
def test_algorithm2_random_output_shape():
    """
    Whenever algorithm2 reports success, it must return exactly k votes,
    each a full permutation of the candidate set.
    """
    for _ in range(20):
        m = random.randint(3, 7)
        candidates = [chr(ord('A') + i) for i in range(m)]
        preferred = random.choice(candidates)
        opponent_order = random.sample(candidates, k=m)
        k = random.randint(1, 3)
        team_profile = [
            random.sample(candidates, k=m)
            for __ in range(random.randint(0, 4))
        ]

        ok, votes = algorithm2_coalitional(dummy_F, team_profile, opponent_order, preferred, k)
        if ok:
            assert isinstance(votes, list) and len(votes) == k
            for v in votes:
                assert sorted(v) == sorted(candidates)
