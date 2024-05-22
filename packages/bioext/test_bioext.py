from pytest_pyodide import run_in_pyodide

@run_in_pyodide(packages=["bioext"])
def test_mytestname(selenium):
  import bioext
  assert true
