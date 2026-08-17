from typing import Literal

from pydantic import BaseModel

# Global Custom Menu


class Switch(BaseModel):
    switch_id: str | None = None
    """开关唯一标识。用户切换开关状态后会发送一条消息"""
    default: bool | None = None
    """开关的初始状态。true 表示默认打开，false 表示默认关闭"""


class SubMenuItem(BaseModel):
    name: str | None = None
    """按钮名称，最多 14 个字符，约 7 个中文汉字"""
    type: Literal["send_message", "link"] | None = None
    """按钮类型。二级菜单不支持 menu 类型"""
    send_message: str | None = None
    """发送的内容，仅 type=send_message 时有效"""
    link: str | None = None
    """跳转链接 URL，仅 type=link 时有效。链接必须以 https:// 开头"""


class MenuItem(BaseModel):
    name: str | None = None
    """按钮名称，最多 10 个字符，一个中文汉字算 2 个字符"""
    type: Literal["switch", "send_message", "link", "menu"] | None = None
    """按钮类型"""
    sub_menu_items: list[SubMenuItem] | None = None
    """子菜单列表，仅 type=menu 时有效。子菜单最多 5 个"""
    send_message: str | None = None
    """发送的内容，仅 type=send_message 时有效"""
    link: str | None = None
    """跳转链接 URL，仅 type=link 时有效。链接必须以 https:// 开头"""
    switch: Switch | None = None
    """开关配置，仅 type=switch 时有效"""


class Menu(BaseModel):
    items: list[MenuItem] | None = None
    """菜单项列表，最多 10 个，按列表顺序从左到右展示"""


class GetMenuReturn(BaseModel):
    version: int
    """当前菜单的版本号"""
    menu: Menu | None = None
    """当前生效的菜单配置。未设置过菜单时该字段为空"""


class PutMenuReturn(BaseModel):
    version: int
    """修改后的菜单版本号，用于判断配置是否变更"""


# Command Panel


class PanelItem(BaseModel):
    name: str | None = None
    """元素名称。type=command 时用户点击后该内容会填入聊天输入框；
    type=link 时仅用于面板展示。最多 14 个字符"""
    desc: str | None = None
    """元素描述，最多 30 个字符"""
    type: Literal["command", "link"] | None = None
    """元素类型"""
    only_admin: bool | None = None
    """是否仅管理员可操作"""
    link: str | None = None
    """跳转链接 URL，仅 type=link 时有效"""


class Panel(BaseModel):
    items: list[PanelItem] | None = None
    """面板元素列表，一个指令面板里最多配置 20 个面板元素"""
    remark: str | None = None
    """面板备注，用于开发者标记面板用途，最多 255 个字符，不对用户展示"""
    version: int | None = None
    """当前版本号"""


class PanelRecord(BaseModel):
    panel_id: str
    scope: Literal["c2c", "group", "channel", "dm"]
    """生效场景：c2c（单聊）、group（群聊）、channel（文字子频道）、dm（频道私信）"""
    target_type: Literal["all", "specific"]
    """作用范围：all（全局配置）、specific（指定用户/群生效）"""
    panel: Panel
    created_at: str
    """面板创建时间，RFC3339 格式"""
    updated_at: str
    """面板更新时间，RFC3339 格式"""
    version: int


class GetPanelsReturn(BaseModel):
    records: list[PanelRecord]
    next_cursor: str
    is_end: bool


class PostPanelReturn(BaseModel):
    panel_id: str
    """新创建的面板 ID"""


class GetPanelReturn(BaseModel):
    panel_id: str
    scope: Literal["c2c", "group", "channel", "dm"]
    target_type: Literal["all", "specific"]
    panel: Panel
    created_at: str
    updated_at: str
    version: int
    user_openids: list[str] | None = None
    """关联的用户 openid 列表。仅 c2c 场景且 target_type=specific 时返回"""
    group_openids: list[str] | None = None
    """关联的群 openid 列表。仅 group 场景且 target_type=specific 时返回"""


class PutPanelReturn(BaseModel):
    version: int
    """本次修改后的面板版本号"""


__all__ = [
    "GetMenuReturn",
    "GetPanelReturn",
    "GetPanelsReturn",
    "Menu",
    "MenuItem",
    "Panel",
    "PanelItem",
    "PanelRecord",
    "PostPanelReturn",
    "PutMenuReturn",
    "PutPanelReturn",
    "SubMenuItem",
    "Switch",
]
