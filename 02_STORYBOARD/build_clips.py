import os, shutil, zipfile

SRC = "/home/user/CARROT_TRAP"
S   = SRC + "/03_SCENES"
K   = S + "/KEYFRAMES"
REF = SRC + "/01_REFERENCES"
OUT = "/tmp/v41/CARROT_TRAP_EP01"

NEG = """no text, no subtitles, no watermark, no logo,
no dialogue, no speaking, no lip-sync to speech, no music,
no extra characters, no second sack, no new props appearing,
no changed fur colors, no missing denim vest, no missing straw hat,
no camera movement, no zoom, no pan, no handheld shake,
no 16:9, no letterbox, no black bars,
no warping limbs, no morphing faces, no flickering,
no realistic photo, no injuries, no blood"""

CLIPS = [
 dict(n=1, code="SC01A", title="TIE THE ROPE", dur="4s",
   a=(K+"/KF01_TIE_THE_ROPE.png", "KF01_TIE_THE_ROPE"),
   b=(K+"/KF02_LIFT_THE_SACK.png", "KF02_LIFT_THE_SACK"),
   ar="الثعلب يربط الحبل في وسط الجزرة العملاقة ويشدّه للتجربة.",
   en='Same fox, same world, locked-off camera. The fox finishes the knot around the giant carrot, pulls the rope tight once to test it, and nods to himself. The empty burlap sack sits folded on the ground beside him. No rabbit.\n\nCartoon SFX: rope creak, a satisfied little "hmph" breath. No dialogue, no music.'),

 dict(n=2, code="SC01B", title="SET THE NET", dur="4s",
   a=(K+"/KF02_LIFT_THE_SACK.png", "KF02_LIFT_THE_SACK"),
   b=(S+"/SC01_THE_SETUP.png", "SC01_THE_SETUP"),
   ar="الثعلب يعلّق كيس الخيش فوق الصخرة، ويختبئ وراها ماسك الحبل.",
   en="Locked camera. The fox lifts the open burlap sack in both arms, swings it up, and drapes it over the flat top of the grey boulder so it hangs ready. He then ducks down behind the rock, out of sight, still holding the rope.\n\nCartoon SFX: fabric whoosh, light thump on stone, scurry of paws. No dialogue."),

 dict(n=3, code="SC02", title="THE BAIT", dur="6s",
   a=(K+"/KF04_EARS_PEEK_OUT.png", "KF04_EARS_PEEK_OUT"),
   b=(S+"/SC02_THE_BAIT.png", "SC02_THE_BAIT"),
   ar="الأرنب يطلع من الجحر — ودان أولاً — يشوف الطُعم ويطيح لعابو.",
   en="Locked camera. The rabbit pushes up out of the burrow — ears first, then his whole head, then his shoulders in the blue denim vest. He stops. He sees the giant carrot. His eyes go wide, ears snap forward, nose twitches fast, and a thread of drool drops from his mouth. He leans toward the carrot.\n\nCartoon SFX: dirt crumble, sniffing, a tiny drip. No dialogue, no music."),

 dict(n=4, code="SC03", title="THE HAUL", dur="6s",
   a=(S+"/SC02_THE_BAIT.png", "SC02_THE_BAIT"),
   b=(S+"/SC03_THE_HAUL.png", "SC03_THE_HAUL"),
   ar="الثعلب يشدّ الحبل بقوة، والأرنب يتجرّ وهو ماسك الجزرة. الحبل مربوط في الجزرة.",
   en="Locked camera. Sudden: the rope snaps taut. The fox yanks from behind the rock with everything he has — legs braced, leaning back, black paws clenched. The rabbit is ripped off his feet and dragged across the grass, still hugging the giant carrot with both arms. Grass and dust kick up. Rabbit's ears fly backward.\n\nCartoon SFX: rope twang, yelp, grass swish, comedic scramble. No dialogue."),

 dict(n=5, code="SC04A", title="THE SLIP  (HINGE)", dur="4s",
   a=(S+"/SC03_THE_HAUL.png", "SC03_THE_HAUL"),
   b=(K+"/KF07_THE_SLIP.png", "KF07_THE_SLIP"),
   ar="★ نقطة الانقلاب — الأرنب يفلت، الحبل يرتخي، الثعلب يفقد التوازن.",
   en="Locked camera. THE HINGE. The rabbit's paws slip off the carrot one by one — first left, then right — and the carrot rolls away from him. The rope goes SLACK and drops in a loose curve. The weight disappears.\n\nCartoon SFX: two soft pops as the paws release, then the rope's tension dying away. No dialogue."),

 dict(n=6, code="SC04B", title="THE IMPACT  (HINGE)", dur="4s",
   a=(K+"/KF07_THE_SLIP.png", "KF07_THE_SLIP"),
   b=(S+"/SC04_THE_REVERSAL.png", "SC04_THE_REVERSAL"),
   ar="★ ظهر الثعلب يضرب الصخرة، والكيس يطيح من فوقها عليه.",
   en="Locked camera. Physics takes over. The fox, still pulling with no resistance, stumbles BACKWARD, both arms windmilling. His back SLAMS into the grey boulder. The impact shakes the stone and knocks the burlap sack off the top — it drops straight down over him. His straw hat spins off his head.\n\nCartoon SFX: whoosh, hollow THUD on stone, fabric flump, hat twirl. No dialogue, no music."),

 dict(n=7, code="SC05", title="THE PAYOFF", dur="6s",
   a=(S+"/SC04_THE_REVERSAL.png", "SC04_THE_REVERSAL"),
   b=(S+"/SC05_THE_PAYOFF.png", "SC05_THE_PAYOFF"),
   ar="الثعلب في الكيس على الأرض، والأرنب يطلع فوق الصخرة ويبدا ياكل.",
   en="Locked camera. The sack settles around the fox — he is now a lump on his back on the ground, only his snout and one black paw out, hat lying flat beside him. He blinks, dazed, one eye twitching. The rabbit scrambles up onto the boulder, sits, and calmly eats a carrot, eyes closed, feet swinging.\n\nCartoon SFX: burlap rustle, a dizzy squeak, satisfied munching. No dialogue."),

 dict(n=8, code="SC06", title="THE END  (CUT - close-up)", dur="6s",
   a=(S+"/SC06_THE_END.png", "SC06_THE_END"),
   b=None,
   ar="✂️ قطع إلى close-up — الأرنب يضحك ويغمز للكاميرا، وقشّرة تطيح على راس الثعلب.",
   en="CUT to close-up. The rabbit bursts out laughing — mouth wide, eyes shut, ears flopping — then points straight at the sacked fox. He aims a slow, cheeky wink at the CAMERA. Above him the fox strains inside the sack, one black paw waving. A strip of carrot peel drops onto the fox's hat brim.\n\nCartoon SFX: belly laugh, munch, a comedically defeated groan. No dialogue, no music."),
]

AR_NUM = {1:"الأول",2:"الثاني",3:"الثالث",4:"الرابع",5:"الخامس",6:"السادس",7:"السابع",8:"الثامن"}

if os.path.exists("/tmp/v41"): shutil.rmtree("/tmp/v41")
os.makedirs(OUT + "/PROMPTS")

combined = ["="*62,
            "  CARROT TRAP · EPISODE 01",
            "  كل البرومبتات في ملف واحد — 8 مقاطع",
            "="*62, ""]

for c in CLIPS:
    nn = f"{c['n']:02d}"
    slug = c['title'].split('  ')[0].replace(' ','_')
    # ---- clip folder: IMAGES ONLY ----
    d = f"{OUT}/{nn}_CLIP_{c['code']}_{slug}"
    os.makedirs(d)
    shutil.copy(c["a"][0], f"{d}/FRAME_A__{c['a'][1]}.png")
    if c["b"]:
        shutil.copy(c["b"][0], f"{d}/FRAME_B__{c['b'][1]}.png")

    # ---- prompt file in PROMPTS/ ----
    frames = ("A = First frame   ->   B = Last frame" if c["b"]
              else "A = First frame ONLY  (Last frame = empty)")
    body = f"""================================================================
  المشهد {AR_NUM[c['n']]}   ·   CLIP {nn}   ·   {c['code']} — {c['title']}
  {c['dur']}   ·   9:16   ·   صامت
================================================================

{c['ar']}

----------------------------------------------------------------
  إعدادات Flow
----------------------------------------------------------------
Model ......... Veo 3.1 Fast   (Quality لا يدعم Ingredients)
Mode .......... Video > Frames > First and last
Aspect ratio .. 9:16
Duration ...... {c['dur']}
Outputs ....... 2
Audio ......... OFF

{frames}

  الصور: {nn}_CLIP_{c['code']}_{slug}/FRAME_A … /FRAME_B …

----------------------------------------------------------------
  BRIDGE PROMPT  —  انسخ من هنا
----------------------------------------------------------------

{c['en']}

----------------------------------------------------------------
  NEGATIVE PROMPT
----------------------------------------------------------------

{NEG}
"""
    fname = f"{nn}_PROMPT_SCENE_{nn}__{c['code']}_{slug}.txt"
    open(f"{OUT}/PROMPTS/{fname}", "w", encoding="utf-8").write(body)

    combined.append("="*62)
    combined.append(f"  المشهد {AR_NUM[c['n']]}  ·  CLIP {nn}  ·  {c['code']} — {c['title']}  ·  {c['dur']}")
    combined.append("="*62)
    combined.append("")
    combined.append(c['en'])
    combined.append("")
combined.append("="*62)
combined.append("  NEGATIVE PROMPT (ينطبق على الـ8 كلهم)")
combined.append("="*62)
combined.append("")
combined.append(NEG)
open(f"{OUT}/PROMPTS/00_ALL_PROMPTS_ONE_FILE.txt","w",encoding="utf-8").write("\n".join(combined))

# ---- reference + sheets ----
R = OUT + "/_REFERENCE"; os.makedirs(R)
for f in ["REF_CARROT_9x16.png","CARROT_SPEC.md","REF_RABBIT_SCENE_9x16.png",
          "REF_FOX_SCENE_9x16.png","REF_SCALE_9x16.png","REF_LOCATION_9x16.png",
          "REF_BURROW_RABBIT_9x16.png"]:
    p=f"{REF}/{f}"
    if os.path.exists(p): shutil.copy(p, f"{R}/{f}")
SH = OUT + "/_SHEETS"; os.makedirs(SH)
for f in ["CARROT_TRAP_CONTACT_SHEET.png","KEYFRAME_CHAIN_SHEET.png"]:
    shutil.copy(f"{SRC}/{f}", f"{SH}/{f}")

open(OUT + "/00_START_HERE.txt","w",encoding="utf-8").write("""================================================================
   CARROT TRAP · الحلقة 01  ·  جاهز للتحريك
   8 مقاطع · 40 ثانية · 9:16 · صامت
================================================================

الهيكل:
   PROMPTS/     ← 8 برومبتات، كل واحد في ملف + ملف جامع
   NN_CLIP_…/   ← الصور فقط (FRAME_A + FRAME_B)

----------------------------------------------------------------
  البرومبتات — PROMPTS/
----------------------------------------------------------------
  00_ALL_PROMPTS_ONE_FILE.txt          كل الـ8 في ملف واحد
  01_PROMPT_SCENE_01__SC01A_TIE_THE_ROPE.txt
  02_PROMPT_SCENE_02__SC01B_SET_THE_NET.txt
  03_PROMPT_SCENE_03__SC02_THE_BAIT.txt
  04_PROMPT_SCENE_04__SC03_THE_HAUL.txt
  05_PROMPT_SCENE_05__SC04A_THE_SLIP.txt
  06_PROMPT_SCENE_06__SC04B_THE_IMPACT.txt
  07_PROMPT_SCENE_07__SC05_THE_PAYOFF.txt
  08_PROMPT_SCENE_08__SC06_THE_END.txt

  كل ملف فيه:  وصف عربي · إعدادات Flow · البرومبت الإنجليزي · النيغاتيف

----------------------------------------------------------------
  الصور — 8 مجلدات
----------------------------------------------------------------
  01_CLIP_SC01A_TIE_THE_ROPE/
      FRAME_A__KF01_TIE_THE_ROPE.png     ← First frame
      FRAME_B__KF02_LIFT_THE_SACK.png    ← Last frame
  02_CLIP_SC01B_SET_THE_NET/   … وهكذا لين 08

  الإطار الوسطاني مكرّر في المجلدين — هذا مقصود،
  باش كل مجلد يخدم وحدو.

  مقطع 08 (SC06): فيه FRAME_A فقط — خلّي Last frame فارغ.

----------------------------------------------------------------
  إعدادات Flow
----------------------------------------------------------------
  Video > Frames > First and last  ·  9:16  ·  Audio OFF
  Model: Veo 3.1 Fast   ·   المدة كيما في ملف البرومبت

----------------------------------------------------------------
  _REFERENCE/   مرجع الجزرة ⭐ + الأرنب + الثعلب + قانون الحجم
  _SHEETS/      ورقة الاتصال + خريطة السلسلة
----------------------------------------------------------------
  كاميرا مقفولة · لا 16:9 · كيس خيش واحد فقط · الثعلب 2.3× الأرنب
================================================================
  https://github.com/latchidz/CARROT-TRAP
================================================================
""")

z="/tmp/CARROT_TRAP_EP01_V41.zip"
if os.path.exists(z): os.remove(z)
with zipfile.ZipFile(z,"w",zipfile.ZIP_DEFLATED,compresslevel=9) as zf:
    for root,dirs,files in os.walk(OUT):
        for f in sorted(files):
            full=os.path.join(root,f)
            zf.write(full, os.path.relpath(full, os.path.dirname(OUT)))
print("zip:", os.path.getsize(z), "bytes")
