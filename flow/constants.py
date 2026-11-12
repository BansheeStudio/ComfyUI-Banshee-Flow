import logging
import mimetypes
from pathlib import Path
import re
APP_NAME = "Flow"
APP_VERSION = "0.5.2" 
FLOWMSG = f"\033[38;5;129mFlow - {APP_VERSION}\033[0m"
APP_CONFIGS = []

CURRENT_DIR = Path(__file__).parent
ROOT_DIR = CURRENT_DIR.parent
WEBROOT = ROOT_DIR / "web"
CORE_PATH = WEBROOT / "core"
FLOW_PATH = WEBROOT / "flow"
FLOWS_PATH = WEBROOT / "flows"
LINKER_PATH = WEBROOT / "linker"
CUSTOM_THEMES_DIR = WEBROOT / 'custom-themes'
WEB_DIRECTORY = "web/core/js/common/scripts"

CUSTOM_NODES_DIR = ROOT_DIR.parent
EXTENSION_NODE_MAP_PATH = ROOT_DIR.parent / "ComfyUI-Manager" / "extension-node-map.json"

FLOWS_DOWNLOAD_PATH = 'https://github.com/diStyApps/flows_lib'

SAFE_FOLDER_NAME_REGEX = re.compile(r'^[\w\-]+$')
ALLOWED_EXTENSIONS = {'css'}
mimetypes.add_type('application/javascript', '.js')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
FLOWS_CONFIG_FILE = 'flowConfig.json'
FLOWS_TO_REMOVE = [
    "afl_CogVideoX-Fun-i2v-es",
    "afl_CogVideoX-Fun-i2v",
    "afl_MimicMotioni2v",
    "afl_abase",
    "afl_abasei2i",
    "afl_abasesd35t3v",
    "afl_abasevea",
    "afl_abaseveai2i",
    "afl_base-fluxd_at2i",
    "afl_base-fluxdggufi2i",
    "afl_base-fluxdgguft2i",
    "afl_base-fluxdi2i",
    "afl_base-fluxs_ai2t",
    "afl_base-fluxsi2i",
    "afl_baseAD",
    "afl_baseAdLcm",
    "afl_cogvidx_at2v",
    "afl_cogvidxi2v",
    "afl_cogvidxinteri2v",
    "afl_flowup",
    "afl_flux_dev",
    "afl_flux_dev_lora",
    "afl_genfill",
    "afl_ipivsMorph",
    "afl_mochi2v",
    "afl_pulid_flux",
    "afl_pulid_flux_GGUF",
    "afl_reactor",
    "5otvy-cogvideox-orbit-left-lora",
    "umbi9-hunyuan-text-to-video",
    # Removed per user request (2026-11-11): all Flux flows except Base - Flux Schnell,
    # plus AnimateDiff, CogVideoX, Hunyuan, Mochi, ipiv's Morph, OmniGen, ReActor
    "04ibz-cogvideox-text-to-video",
    "1harq-cogvideox-fun-i2v-start-end",
    "1ieqw-cogvideox-image-to-video",
    "2vkrp-cogvideox-fun-i2v",
    "k4ryr-cogvideox-interpolation",
    "7lm54-basic-animatediff",
    "b82lw-basic-animatediff-lcm",
    "85up7-hunyuan-gguf-text-to-video",
    "pla14-hunyuan-text-to-video",
    "40uu9-mochi-text-to-video",
    "bq6f1-mochi-comfyui-native",
    "rbacj-mochi-comfyui-native-webp",
    "96nfo-ipiv-s-morph-img2vid-lcm",
    "xo5fx-omnigen",
    "cxkqe-reactor",
    "28s1h-flux-detailer",
    "30kk2-base-flux-dev",
    "3pw8q-flux-dev-fill-detailed-inpainting",
    "5qjq4-flux-redux-3-images",
    "6xjt5-base-flux-dev-background-removal",
    "7bxez-flux-redux",
    "8e3m5-flux-dev",
    "94lhm-flux-redux-2-images",
    "9w957-base-flux-dev-image-to-image-gguf",
    "b5v17-flux-gguf-detailer",
    "bf3ea-flux-dev-fill-gguf-inpainting",
    "by7uq-flux-dev-gguf-basic-inpainting",
    "f9k2j-flux-dev-basic-inpainting",
    "j4wox-base-flux-dev-paint-image-to-image",
    "ju12s-base-flux-dev-gguf",
    "n0y8e-base-flux-dev-image-to-image",
    "p44se-pulid-flux",
    "pexbu-flux-dev-lora",
    "ppfxh-flux-depth",
    "qtg57-base-flux-schnell-image-to-image",
    "roup2-flux-dev-fill-gguf-detailed-inpainting",
    "vw44x-pulid-flux-gguf",
    "ws4bx-base-flux-dev-image-to-image-background-removal",
    "y2gic-flux-dev-fill-inpainting",
    # Removed per user request (2026-11-11, 2nd round)
    "6l639-basic-mimicmotion",
    "afl_genfill",
    "67e3l-basic-paint-stable-diffusion-image-to-image",
    "12slf-stable-diffusion-3-5-text-to-image",
]

NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
