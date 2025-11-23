from examples.integrated_scenario import main  # type: ignore


def test_integrated_scenario_runs(monkeypatch, capsys):
    # Run with small steps to keep fast
    monkeypatch.setattr(
        "sys.argv",
        ["integrated", "--frequency", "30", "--phase", "0.1", "--steps", "5"],
    )
    main()
    captured = capsys.readouterr()
    assert "[Cymatics]" in captured.out
    assert "[Result]" in captured.out
