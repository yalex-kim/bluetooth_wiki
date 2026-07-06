"""Bluetooth wiki agent package.

``BluetoothWikiAgent`` is imported lazily so that SDK-free consumers (the
``search`` package, index build scripts, unit tests of pure logic) can import
``agent.config``/``agent.citations`` without requiring ``claude_agent_sdk``.
"""

from .citations import citation_to_url, file_path_to_url, parse_citation

__all__ = ["BluetoothWikiAgent", "file_path_to_url", "parse_citation", "citation_to_url"]


def __getattr__(name: str):
    if name == "BluetoothWikiAgent":
        from .agent import BluetoothWikiAgent

        return BluetoothWikiAgent
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
