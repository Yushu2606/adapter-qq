from nonebot.compat import type_validate_python

from nonebot.adapters.qq.models import (
    GetMenuReturn,
    GetPanelReturn,
    GetPanelsReturn,
    PostPanelReturn,
    PutMenuReturn,
    PutPanelReturn,
)


def test_get_menu_return_parses_official_example():
    payload = {
        "menu": {
            "items": [{"type": "send_message", "name": "帮助", "send_message": "/help"}]
        },
        "version": 1,
    }

    result = type_validate_python(GetMenuReturn, payload)

    assert result.version == 1
    assert result.menu is not None
    assert result.menu.items is not None
    assert result.menu.items[0].name == "帮助"
    assert result.menu.items[0].type == "send_message"


def test_get_menu_return_allows_unset_menu():
    result = type_validate_python(GetMenuReturn, {"version": 0})

    assert result.menu is None


def test_put_menu_return_parses_version():
    assert type_validate_python(PutMenuReturn, {"version": 1}).version == 1


def test_get_panels_return_parses_official_example():
    payload = {
        "records": [
            {
                "panel_id": "p_x8k2x8k2x8k2",
                "scope": "c2c",
                "target_type": "all",
                "panel": {
                    "items": [
                        {"type": "command", "name": "查询天气", "desc": "查询当前天气"}
                    ],
                    "remark": "C2C面板",
                },
                "created_at": "2024-01-01T00:00:00+00:00",
                "updated_at": "2024-01-01T00:00:00+00:00",
                "version": 1,
            }
        ],
        "next_cursor": "",
        "is_end": True,
    }

    result = type_validate_python(GetPanelsReturn, payload)

    assert result.is_end is True
    assert result.records[0].panel_id == "p_x8k2x8k2x8k2"
    assert result.records[0].scope == "c2c"
    assert result.records[0].panel.items[0].name == "查询天气"


def test_post_panel_return_parses_panel_id():
    result = type_validate_python(PostPanelReturn, {"panel_id": "p_x8k2x8k2x8k2"})

    assert result.panel_id == "p_x8k2x8k2x8k2"


def test_get_panel_return_parses_official_example():
    payload = {
        "panel_id": "p_x8k2x8k2x8k2",
        "scope": "group",
        "target_type": "specific",
        "panel": {"items": [{"type": "command", "name": "群签到", "desc": "每日签到"}]},
        "created_at": "2024-01-01T00:00:00+00:00",
        "updated_at": "2024-01-01T00:00:00+00:00",
        "version": 1,
        "user_openids": [],
        "group_openids": ["openid_group_001"],
    }

    result = type_validate_python(GetPanelReturn, payload)

    assert result.target_type == "specific"
    assert result.group_openids == ["openid_group_001"]


def test_put_panel_return_parses_version():
    assert type_validate_python(PutPanelReturn, {"version": 1}).version == 1
