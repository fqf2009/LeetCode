from unittest.mock import Mock, MagicMock, patch
import pytest
from leetcode import lc0278_FirstBadVersion 


@pytest.mark.parametrize('solution,n,expected',
    [[lc0278_FirstBadVersion.Solution, 105, 10], 
     [lc0278_FirstBadVersion.Solution, 20, 10], 
     [lc0278_FirstBadVersion.Solution, 500, 10]])
def test_firstBadVersion(solution, n, expected):

    # is_bad = MagicMock(side_effect = lambda v: v >= n)
    # @patch('lc0278_FirstBadVersion.isBadVersion')
    # def mock_isBadVersion(version: int) -> bool:
    #     return version >= expected
    with patch('.isBadVersion') as mock_is_bad:
        mock_is_bad.side_effect = lambda v: v >= expected
        sol = solution()
        r = sol.firstBadVersion(n)
        print(r)
        assert r == expected

pytest.main()
