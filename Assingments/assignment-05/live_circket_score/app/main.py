import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from typing import List, Optional

import requests
from flask import Blueprint, render_template

bp = Blueprint("main", __name__)

FEED_URL = "https://static.cricinfo.com/rss/livescores.xml"
CACHE_TTL = 60  # seconds


@dataclass
class ScoreItem:
    title: str
    link: str
    pub_date: Optional[str]


def fetch_feed() -> List[ScoreItem]:
    resp = requests.get(FEED_URL, timeout=10)
    resp.raise_for_status()
    root = ET.fromstring(resp.content)

    items: List[ScoreItem] = []
    for item in root.iterfind("channel/item"):
        title_el = item.find("title")
        link_el = item.find("link")
        pub_el = item.find("pubDate")
        title = title_el.text.strip() if title_el is not None and title_el.text else "(no title)"
        link = link_el.text.strip() if link_el is not None and link_el.text else "#"
        pub_date = pub_el.text.strip() if pub_el is not None and pub_el.text else None
        items.append(ScoreItem(title=title, link=link, pub_date=pub_date))
    return items


_cache = {"ts": 0.0, "data": []}


def get_scores_cached() -> List[ScoreItem]:
    now = time.time()
    if now - _cache["ts"] < CACHE_TTL and _cache["data"]:
        return _cache["data"]
    data = fetch_feed()
    _cache["ts"] = now
    _cache["data"] = data
    return data


@bp.route("/")
def index():
    try:
        scores = get_scores_cached()
        error = None
    except Exception as exc:
        scores = []
        error = str(exc)
    return render_template("index.html", scores=scores, error=error)
