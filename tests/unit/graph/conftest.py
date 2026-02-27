import pytest

from dbt.tests.util import safe_set_invocation_context


@pytest.fixture(autouse=True)
def _set_invocation_context():
    """Ensure DBT_INVOCATION_CONTEXT_VAR is set for all graph tests."""
    safe_set_invocation_context()
