#!/usr/bin/env python3
"""Unit tests for CLI -- doesn't work"""

from typer.testing import CliRunner

import cli


def run_cards(*params):
    runner = CliRunner()
    result = runner.invoke(cli.app, params)
    output = result.output.rstrip()
    return output


def test_version():
    assert run_cards("version") == "0.1"


def test_patch_get_path(monkeypatch, tmp_path):
    def fake_get_path():
        return tmp_path

    monkeypatch.setattr(cli, "get_path", fake_get_path)
    assert run_cards("config") == str(tmp_path)


def test_patch_env_var(monkeypatch, tmp_path):
    monkeypatch.setenv("CARDS_DB_DIR", str(tmp_path))
    assert run_cards("config") == str(tmp_path)
