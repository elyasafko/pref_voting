"""
Pytest unit tests for the Strategic-Voting stubs.
All tests are xfail until real implementations are provided.
"""

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
