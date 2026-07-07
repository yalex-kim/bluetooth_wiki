import importlib


def test_get_client_uses_configured_base_url(monkeypatch):
    monkeypatch.setenv("OPENAI_BASE_URL", "http://gpt-oss.internal/v1")
    monkeypatch.setenv("OPENAI_API_KEY", "dummy-key")
    # Re-import config + llm so they pick up the patched env.
    import agent.config as cfg
    importlib.reload(cfg)
    import agent.llm as llm
    importlib.reload(llm)

    c1 = llm.get_client()
    c2 = llm.get_client()
    assert c1 is c2  # process-cached
    assert str(c1.base_url).rstrip("/") == "http://gpt-oss.internal/v1"


def test_config_model_defaults_are_gpt_oss(monkeypatch):
    for var in ("BT_AGENT_MODEL", "BT_AGENT_JUDGE_MODEL", "BT_AGENT_SUFFICIENCY_MODEL"):
        monkeypatch.delenv(var, raising=False)
    import agent.config as cfg
    importlib.reload(cfg)
    assert cfg.MODEL == "gpt-oss-120b"
    assert cfg.JUDGE_MODEL == "gpt-oss-120b"
    assert cfg.SUFFICIENCY_MODEL == "gpt-oss-120b"
