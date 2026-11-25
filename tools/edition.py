"""The stories on the front page for Tuesday 24 November 2026.

Every story here happened, or was first reported, on 24 November 2026
(in some time zone), and each carries the outlets that reported it.
Claims that rest on one side's word are attributed, and each drawn story
carries how sure the reporting is (SURE below).
"""

DAY = "Tuesday 24 November 2026"
DAY_TAG = "TUESDAY 24 NOVEMBER"
DAY_TAG_SHORT = "24 NOVEMBER"
SUBLINE = ["Huawei convicted in Brooklyn", "Houthi drone hits Riyadh's tallest tower",
           "Asia's chip stocks soar"]

REGIONS = {
    "asia": ("Asia", "#c0392b"),
    "mideast": ("Middle East", "#d4881c"),
    "europe": ("Europe", "#1f5f8b"),
    "americas": ("Americas", "#2e7d4f"),
    "africa": ("Africa", "#7b4a9e"),
    "oceania": ("Oceania", "#138a8a"),
    "global": ("Global", "#5b5b5b"),
}

SURE = {
    "OFFICIAL": ("#1f5f8b", "government, agency, court or company statement"),
    "CONFIRMED": ("#2e7d4f", "two or more major outlets"),
    "REPORTED": ("#a07a18", "one outlet's reporting"),
    "CLAIM": ("#b3261e", "one side's word, unverified"),
}

# The day in UTC: only times the reports give.
TIMELINE = [
    ("05:30", "Taiex closes up about 9%"),
    ("06:30", "Kospi closes above 5,000"),
    ("19:48", "Trump pardons two turkeys"),
    ("20:00", "Champions League kick-offs"),
]

KPIS = [
    ("10 of 12", "counts Huawei is convicted on by a Brooklyn jury"),
    ("11", "hurt as a Houthi drone hits Riyadh's PIF tower"),
    ("+9%", "Taiex, as Huang's return to Nvidia lifts Asia"),
    ("47,000", "women killed by partner or kin in 2025, UN says"),
    ("4th", "Politburo member probed: Shanghai's Chen Jining"),
    ("$41bn", "Sanofi agrees to buy Insmed, $175 a share"),
]

LEADS = [
    dict(
        art="court_lead", tag="VERDICT", region="americas", place="NEW YORK, US",
        beat="COURTS", sure="CONFIRMED", chip="GUILTY \u00b7 10 OF 12",
        head="Huawei found guilty on 10 of 12 US counts",
        dek="Bank fraud, Iran sanctions breaches and trade-secret theft; "
            "acquitted of racketeering. Sentencing set for 2027.",
        src="CNN · CNBC · US DOJ",
    ),
    dict(
        art="pif_tower", tag="STRIKE", region="mideast", place="RIYADH, SAUDI ARABIA",
        beat="YEMEN WAR", sure="OFFICIAL", chip="11 INJURED",
        head="Houthi drone hits Riyadh's tallest tower",
        dek="Saudi Civil Defence says 11 hurt at the wealth fund's HQ; "
            "the coalition strikes back at Hodeidah.",
        src="CNBC · NBC · AL JAZEERA",
    ),
    dict(
        art="markets_up", tag="REBOUND", region="asia", place="TAIPEI · SEOUL · TOKYO",
        beat="MARKETS", sure="CONFIRMED", chip="TAIEX +9%",
        head="Asia's chip stocks soar as Huang returns",
        dek="Taiex about +9%, Kospi about +7% above 5,000, Nikkei about +4% "
            "after Nvidia reinstates its CEO.",
        src="CNA · AP · GULF NEWS",
    ),
]

CARDS = [
    dict(art="probe", region="asia", place="SHANGHAI, CHINA", sure="OFFICIAL", chip="UNDER INVESTIGATION",
         head="China probes Shanghai party chief",
         dek="Chen Jining is the fourth Politburo member of 2022 to face investigation.",
         src="XINHUA · BLOOMBERG"),
    dict(art="femicide", region="global", place="VIENNA · NEW YORK", sure="OFFICIAL",
         head="UN: five women an hour killed by partner or kin",
         dek="47,000 in 2025; Africa has the highest rate, the femicide brief finds.",
         src="UNODC · UN WOMEN"),
    dict(art="ebola", region="africa", place="ITURI, DR CONGO", sure="OFFICIAL", chip="STAFF RESCUED",
         head="WHO staff rescued from Ebola zone hospital",
         dek="Sheltered three days in Akwe amid army–CRP fighting, Tedros says.",
         src="WHO · ARAB NEWS · ANI"),
    dict(art="trophy", region="africa", place="LAUSANNE · DAKAR", sure="CONFIRMED", chip="TITLE RESTORED",
         head="Senegal restored as Africa Cup champions",
         dek="Sport's top court overturns CAF's award of the 2025 title to Morocco.",
         src="AA · CAS"),
    dict(art="refinery", region="europe", place="MOSCOW, RUSSIA", sure="OFFICIAL", chip="REFINING \u221245%",
         head="Putin calls retaliation for refinery hits “inevitable”",
         dek="Drone strikes have cut Russian refining by 45% since late October, sources say.",
         src="REUTERS · AL JAZEERA"),
    dict(art="hormuz", region="mideast", place="STRAIT OF HORMUZ", sure="CLAIM", chip="IRGC CLAIM",
         head="Iran says mines stop ships in Hormuz",
         dek="IRGC says tankers and a container ship struck mines on an “unauthorised route”.",
         src="IRIB · JPOST · ANI"),
    dict(art="debt", region="americas", place="CARACAS, VENEZUELA", sure="OFFICIAL", chip="242% OF GDP",
         head="Venezuela puts its debt at $237.5bn",
         dek="242% of GDP, disclosed ahead of a restructuring of defaulted bonds.",
         src="10 THINGS · REUTERS"),
    dict(art="scoreline", region="europe", place="MADRID, SPAIN", sure="CONFIRMED", chip="5-1",
         head="Real Madrid come back to rout PSV 5-1",
         dek="Arsenal draw 1-1 with Dortmund; Galatasaray edge Aston Villa 1-0.",
         src="AA · UEFA"),
    dict(art="pharma", region="europe", place="PARIS, FRANCE", sure="OFFICIAL", chip="$41BN DEAL",
         head="Sanofi agrees to buy Insmed for $41bn",
         dek="$175 a share for the maker of the lung drug Brinsupri, a filing shows.",
         src="SANOFI · SEC FILING"),
    dict(art="ariane", region="americas", place="KOUROU, FRENCH GUIANA", sure="REPORTED", chip="36 SATELLITES",
         head="Ariane 6 lofts 36 Amazon Leo satellites",
         dek="Europe's heavy rocket flies its fourth Amazon Leo mission.",
         src="ARIANESPACE · AIAA"),
]

PINS = [
    (1, -73.99, 40.69, "americas"), (2, 46.64, 24.77, "mideast"), (3, 121.5, 25.03, "asia"),
    (4, 121.47, 31.23, "asia"), (5, 16.37, 48.21, "global"), (6, 30.0, 1.9, "africa"),
    (7, -17.45, 14.69, "africa"), (8, 37.6, 55.75, "europe"), (9, 56.3, 26.6, "mideast"),
    (10, -66.9, 10.5, "americas"), (11, -3.69, 40.45, "europe"), (12, 2.35, 48.86, "europe"),
    (13, -52.77, 5.24, "americas"),
]

BRIEFS = [
    (14, "TAIPEI", "TSMC and MediaTek jump nearly 10%", "asia"),
    (15, "SEOUL", "Samsung +7.5%, SK Hynix +8.6% as Kospi tops 5,000", "asia"),
    (16, "TOKYO", "Nikkei 225 ends about 4% higher", "asia"),
    (17, "KUALA LUMPUR", "Malaysia to send 6,803 Rohingya back to Myanmar", "asia"),
    (18, "HODEIDAH", "Coalition hits Houthi targets in Hodeidah and Saada", "mideast"),
    (19, "DOHA", "Qatar and Pakistan condemn the Riyadh tower attack", "mideast"),
    (20, "LONDON", "UK sanctions the Houthi group and four officials", "europe"),
    (21, "KYIV", "Hungary's PM Magyar on first official visit", "europe"),
    (22, "PARIS", "Sarkozy and Carla Bruni ordered to stand trial", "europe"),
    (23, "BRUSSELS", "EU proposes 22nd Russia sanctions package", "europe"),
    (24, "LONDON", "Arsenal 1-1 Dortmund; Man City 2-2 Napoli", "europe"),
    (25, "SUVA", "Fiji warns drought may last into early 2027", "oceania"),
    (26, "BOGOTÁ", "UN marks 10 years of Colombia's peace accord", "americas"),
    (27, "HAVANA", "WHO chief urges end to US fuel blockade", "americas"),
    (28, "BRASÍLIA", "Chamber passes fiscal bill with 353 votes", "americas"),
    (29, "WASHINGTON", "Hackers breached a CIA–ODNI unclassified system", "americas"),
    (30, "WASHINGTON", "Tariff rise readied for China, EU and 14 others", "americas"),
    (31, "WASHINGTON", "Trump pardons two Thanksgiving turkeys", "americas"),
    (32, "WASHINGTON", "Blanche won't say if Nvidia is under investigation", "americas"),
    (33, "ANCHORAGE", "Sullivan concedes Alaska Senate race to Peltola", "americas"),
]

DATE_CHECK = (
    "Left out as earlier news: Nvidia's 31.5% jump on Huang's return and the leaked count of "
    "Russia's war dead (Mon 23 Nov), COP31's collapse (Sun 22 Nov), the first strike on Riyadh's "
    "PIF tower (Thu 19 Nov). Every story here happened, or was first reported, on Tuesday "
    "24 November 2026 in some time zone."
)

SOURCES = (
    "Sources: CNN · CNBC · US DOJ · NBC · Al Jazeera · Anadolu · AP · Reuters · "
    "Xinhua · Bloomberg · UNODC · WHO · CAS · IRIB · Politico · Rio Times · Fiji Sun · UEFA"
)
