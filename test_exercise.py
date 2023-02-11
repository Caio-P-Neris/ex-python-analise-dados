import pytest
import src.exercise

def test_exercise(capfd):
    input_values = [[1, 190, 198, 198.1], [25, 50, 197.9, 199], [400], [1, 2, 3, 4, 5]]
    output = []

    def mock_input():
        return input_values[0].pop(0)

    for _ in range(4):
        src.exercise.input = mock_input
        src.exercise.main()
        out, err = capfd.readouterr()
        output.append(out)
        input_values.pop(0)

    assert output == ['Insuficiente\nInsuficiente\nInsuficiente\nMeta atingida\n',
    'Insuficiente\nInsuficiente\nInsuficiente\nMeta atingida\n', 'Meta atingida\n',
    'Insuficiente\nInsuficiente\nInsuficiente\nInsuficiente\nInsuficiente\n']
