"""
ComfyUI Compare custom node package
"""

from .py.compare import Compare

NODE_CLASS_MAPPINGS = {
    Compare.NAME: Compare,
}

# Tell ComfyUI where to find frontend files relative to this package
WEB_DIRECTORY = "./web/comfyui"

__all__ = ["NODE_CLASS_MAPPINGS", "WEB_DIRECTORY"]
