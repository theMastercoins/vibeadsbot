from adsutils import *
from textutils import *

# === Watch Ad Process ===
def watch_ad(user_id, username="LatifaNew0", first_name="Lati2000🐾"):
    type_writer(f"{Fore.CYAN}Launching ad-watching sequence...")

    rtb = get_adextra_rtb(user_id)
    if not rtb:
        glitch_effect("❌ Failed to reach AdExtra")
        return

    script_id, impurl = extract_ad_info(rtb)
    if script_id:
        type_writer(f"🎯 Ad Script ID: {script_id}")

    # Parallel ad requests
    g_response = fetch_gigapub_ad(user_id, username, first_name)
    tgads_data = tgads_bid_request(user_id, username, first_name)

    if impurl and track_impression(impurl):
        type_writer(f"{Fore.GREEN}✅ Ad watched successfully")
    else:
        type_writer(f"{Fore.YELLOW}⚠️ Could not confirm ad watch")
        report_ad_error(user_id, username, first_name)

    if g_response.get("ads") or tgads_data:
        type_writer(f"{Fore.GREEN}✨ Additional ads available")

    print()