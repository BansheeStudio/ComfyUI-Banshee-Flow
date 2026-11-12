from aiohttp import web
import server
from .flow_manager import FlowManager
from .downloader import download_update_flows
from .constants import FLOWMSG, logger

def setup_server() -> None:
    try:
        server_instance = server.PromptServer.instance
    except Exception as e:
        logger.error(f"{FLOWMSG}: Failed to get server instance: {e}")
        return

    # Auto-download/update of flows disabled (2026-11-11): this re-cloned the full
    # upstream flows_lib repo on every startup and re-added flows the user had
    # removed. Flow set is now managed manually. To re-enable, restore this line:
    # download_update_flows()

    try:
        FlowManager.setup_app_routes(server_instance.app)
    except Exception as e:
        logger.error(f"{FLOWMSG}: Failed to set up app routes: {e}")
