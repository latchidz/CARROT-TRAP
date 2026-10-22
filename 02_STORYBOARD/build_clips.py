import os, shutil, zipfile

SRC = "/home/user/CARROT_TRAP"
S   = SRC + "/03_SCENES"
K   = S + "/KEYFRAMES"
REF = SRC + "/01_REFERENCES"
OUT = "/tmp/clips/CARROT_TRAP_EP01_CLIPS"

NEG = """no text, no subtitles, no watermark, no logo,
no dialogue, no speaking, no lip-sync to speech, no music,
no extra characters, no second sack, no new props appearing,
no changed fur colors, no missing denim vest, no missing straw hat,
no camera movement, no zoom, no pan, no handheld shake,
no 16:9, no letterbox, no black bars,
no warping limbs, no morphing faces, no flickering,
no realistic photo, no injuries, no blood"""

CLIPS = [
 dict(n="01", code="SC01A", title="TIE THE ROPE", dur="4s",
   a=(K+"/KF01_TIE_THE_ROPE.png", "KF01_TIE_THE_ROPE"),
   b=(K+"/KF02_LIFT_THE_SACK.png", "KF02_LIFT_THE_SACK"),
   ar="الثعلب يربط الحبل في وسط الجزرة العملاقة ويشدّه للتجربة.",
   en="Same fox, same world, locked-off camera. The fox finishes the knot around the giant carrot, pulls the rope tight once to test it, and nods to himself. The empty burlap sack sits folded on the ground beside him. No rabbit.\n\nCartoon SFX: rope creak, a satisfied little \"hmph\" breath. No dialogue, no music."),

 dict(n="02", code="SC01B", title="SET THE NET", dur="4s",
   a=(K+"/KF02_LIFT_THE_SACK.png", "KF02_LIFT_THE_SACK"),
   b=(S+"/SC01_THE_SETUP.png", "SC01_THE_SETUP"),
   ar="الثعلب يعلّق كيس الخيش فوق الصخرة، ويختبئ وراها ماسك الحبل.",
   en="Locked camera. The fox lifts the open burlap sack in both arms, swings it up, and drapes it over the flat top of the grey boulder so it hangs ready. He then ducks down behind the rock, out of sight, still holding the rope.\n\nCartoon SFX: fabric whoosh, light thump on stone, scurry of paws. No dialogue."),

 dict(n="03", code="SC02", title="THE BAIT", dur="6s",
   a=(K+"/KF04_EARS_PEEK_OUT.png", "KF04_EARS_PEEK_OUT"),
   b=(S+"/SC02_THE_BAIT.png", "SC02_THE_BAIT"),
   ar="الأرنب يطلع من الجحر — ودان أولاً — يشوف الطُعم ويطيح لعابو.",
   en="Locked camera. The rabbit pushes up out of the burrow — ears first, then his whole head, then his shoulders in the blue denim vest. He stops. He sees the giant carrot. His eyes go wide, ears snap forward, nose twitches fast, and a thread of drool drops from his mouth. He leans toward the carrot.\n\nCartoon SFX: dirt crumble, sniffing, a tiny drip. No dialogue, no music."),

 dict(n="04", code="SC03", title="THE HAUL", dur="6s",
   a=(S+"/SC02_THE_BAIT.png", "SC02_THE_BAIT"),
   b=(S+"/SC03_THE_HAUL.png", "SC03_THE_HAUL"),
   ar="الثعلب يشدّ الحبل بقوة، والأرنب يتجرّ وهو ماسك الجزرة. الحبل مربوط في الجزرة.",
   en="Locked camera. Sudden: the rope snaps taut. The fox yanks from behind the rock with everything he has — legs braced, leaning back, black paws clenched. The rabbit is ripped off his feet and dragged across the grass, still hugging the giant carrot with both arms. Grass and dust kick up. Rabbit's ears fly backward.\n\nCartoon SFX: rope twang, yelp, grass swish, comedic scramble. No dialogue."),

 dict(n="05", code="SC04A", title="THE SLIP  (HINGE)", dur="4s",
   a=(S+"/SC03_THE_HAUL.png", "SC03_THE_HAUL"),
   b=(K+"/KF07_THE_SLIP.png", "KF07_THE_SLIP"),
   ar="★ نقطة الانقلاب — الأرنب يفلت، الحبل يرتخي، الثعلب يفقد التوازن.",
   en="Locked camera. THE HINGE. The rabbit's paws slip off the carrot one by one — first left, then right — and the carrot rolls away from him. The rope goes SLACK and drops in a loose curve. The weight disappears.\n\nCartoon SFX: two soft pops as the paws release, then the rope's tension dying away. No dialogue."),

 dict(n="06", code="SC04B", title="THE IMPACT  (HINGE)", dur="4s",
   a=(K+"/KF07_THE_SLIP.png", "KF07_THE_SLIP"),
   b=(S+"/SC04_THE_REVERSAL.png", "SC04_THE_REVERSAL"),
   ar="★ ظهر الثعلب يضرب الصخرة، والكيس يطيح من فوقها عليه.",
   en="Locked camera. Physics takes over. The fox, still pulling with no resistance, stumbles BACKWARD, both arms windmilling. His back SLAMS into the grey boulder. The impact shakes the stone and knocks the burlap sack off the top — it drops straight down over him. His straw hat spins off his head.\n\nCartoon SFX: whoosh, hollow THUD on stone, fabric flump, hat twirl. No dialogue, no music."),

 dict(n="07", code="SC05", title="THE PAYOFF", dur="6s",
   a=(S+"/SC04_THE_REVERSAL.png", "SC04_THE_REVERSAL"),
   b=(S+"/SC05_THE_PAYOFF.png", "SC05_THE_PAYOFF"),
   ar="الثعلب في الكيس على الأرض، والأرنب يطلع فوق الصخرة ويبدا ياكل.",
   en="Locked camera. The sack settles around the fox — he is now a lump on his back on the ground, only his snout and one black paw out, hat lying flat beside him. He blinks, dazed, one eye twitching. The rabbit scrambles up onto the boulder, sits, and calmly eats a carrot, eyes closed, feet swinging.\n\nCartoon SFX: burlap rustle, a dizzy squeak, satisfied munching. No dialogue."),

 dict(n="08", code="SC06", title="THE END  (CUT - close-up)", dur="6s",
   a=(S+"/SC06_THE_END.png", "SC06_THE_END"),
   b=None,
   ar="✂️ قطع إلى close-up — الأرنب يضحك ويغمز للكاميرا، وقشّرة تطيح على راس الثعلب.",
   en="CUT to close-up. The rabbit bursts out laughing — mouth wide, eyes shut, ears flopping — then points straight at the sacked fox. He aims a slow, cheeky wink at the CAMERA. Above him the fox strains inside the sack, one black paw waving. A strip of carrot peel drops onto the fox's hat brim.\n\nCartoon SFX: belly laugh, munch, a comedically defeated groan. No dialogue, no music."),
]

if os.path.exists("/tmp/clips"): shutil.rmtree("/tmp/clips")
os.makedirs(OUT)

for c in CLIPS:
    d = f"{OUT}/CLIP_{c['n']}_{c['code']}_{c['title'].split('  ')[0].replace(' ','_')}"
    os.makedirs(d)

    # frame A
    src, name = c["a"]
    shutil.copy(src, f"{d}/FRAME_A__{name}.png")
    # frame B
    if c["b"]:
        src, name = c["b"]
        shutil.copy(src, f"{d}/FRAME_B__{name}.png")

    # prompt file
    frames = "A = First frame  ->  B = Last frame" if c["b"] else "A = First frame ONLY  (leave Last frame empty)"
    txt = f"""=====================================================
  CLIP {c['n']}  ·  {c['code']} — {c['title']}
  {c['dur']}   ·   9:16   ·   silent
=====================================================

{c['ar']}

-----------------------------------------------------
  FLOW SETTINGS
-----------------------------------------------------
Model ......... Veo 3.1 Fast   (Quality does NOT support Ingredients)
Mode .......... Video > Frames > First and last
Aspect ratio .. 9:16
Duration ...... {c['dur']}
Outputs ....... 2
Audio ......... OFF

{frames}

-----------------------------------------------------
  BRIDGE PROMPT  (copy everything below)
-----------------------------------------------------

{c['en']}

-----------------------------------------------------
  NEGATIVE PROMPT
-----------------------------------------------------

{NEG}
"""
    open(f"{d}/PROMPT.txt", "w", encoding="utf-8").write(txt)

# ---------- reference folder ----------
R = OUT + "/_REFERENCE"
os.makedirs(R)
for f in ["REF_CARROT_9x16.png","CARROT_SPEC.md","REF_RABBIT_SCENE_9x16.png",
          "REF_FOX_SCENE_9x16.png","REF_SCALE_9x16.png","REF_LOCATION_9x16.png",
          "REF_BURROW_RABBIT_9x16.png"]:
    p = f"{REF}/{f}"
    if os.path.exists(p): shutil.copy(p, f"{R}/{f}")

# ---------- sheets ----------
SH = OUT + "/_SHEETS"
os.makedirs(SH)
for f in ["CARROT_TRAP_CONTACT_SHEET.png","KEYFRAME_CHAIN_SHEET.png"]:
    shutil.copy(f"{SRC}/{f}", f"{SH}/{f}")

# ---------- top level readme ----------
open(OUT + "/00_START_HERE.txt","w",encoding="utf-8").write("""=====================================================
   CARROT TRAP · EPISODE 01  ·  READY TO ANIMATE
   8 clips · 40 seconds · 9:16 · silent
=====================================================

كل مقطع عندو مجلد خاص فيه:
   FRAME_A__....png   ← حطّو في خانة  First frame
   FRAME_B__....png   ← حطّو في خانة  Last frame
   PROMPT.txt         ← فيه البرومبت الإنجليزي + الإعدادات + النيغاتيف

الترتيب في Flow:
   Video > Frames > First and last   ·   9:16   ·   Audio OFF

-----------------------------------------------------
  الـ8 مقاطع
-----------------------------------------------------
 1  SC01A  TIE THE ROPE      4s   الثعلب يربط الحبل
 2  SC01B  SET THE NET       4s   يعلّق الكيس فوق الصخرة ويختبئ
 3  SC02   THE BAIT          6s   الأرنب يطلع من الجحر
 4  SC03   THE HAUL          6s   الثعلب يشدّ والأرنب يتجرّ
 5  SC04A  THE SLIP          4s   ★ الأرنب يفلت
 6  SC04B  THE IMPACT        4s   ★ ظهره يضرب الصخرة والكيس يطيح
 7  SC05   THE PAYOFF        6s   الثعلب في الكيس
 8  SC06   THE END           6s   ✂️ close-up · غمزة للكاميرا

-----------------------------------------------------
  ملاحظات
-----------------------------------------------------
· الإطار اللي يخدم مرتين مكرّر في المجلدين — هذا مقصود،
  باش كل مجلد يخدم وحدو بلا ما تخلط.

· مقطع 8 (SC06): حطّ غير First frame، وخلّي Last frame فارغ.

· _REFERENCE/ : مرجع الجزرة + الأرنب + الثعلب + قانون الحجم.
  ⛔ ما تولّدش كادر جديد بلا REF_CARROT_9x16.

· _SHEETS/ : ورقة الاتصال + خريطة السلسلة للمراجعة.

· كاميرا مقفولة · لا 16:9 · كيس خيش واحد فقط · الثعلب 2.3× الأرنب

=====================================================
  https://github.com/latchidz/CARROT-TRAP
=====================================================
""")

# ---------- zip ----------
z = "/tmp/CARROT_TRAP_EP01_CLIPS.zip"
if os.path.exists(z): os.remove(z)
with zipfile.ZipFile(z,"w",zipfile.ZIP_DEFLATED,compresslevel=9) as zf:
    for root,dirs,files in os.walk(OUT):
        for f in sorted(files):
            full=os.path.join(root,f)
            zf.write(full, os.path.relpath(full, os.path.dirname(OUT)))

print("folders:", len([d for d in os.listdir(OUT) if os.path.isdir(OUT+'/'+d)]))
print("files  :", sum(len(f) for _,_,f in os.walk(OUT)))
print("zip    :", os.path.getsize(z), "bytes")
