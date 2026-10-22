# 🎬 KEYFRAME MAP — Google Flow (Veo 3.1)
### الحلقة 01 · «فخ الجزرة العملاقة» · نظام الصورتين لكل لقطة

---

## ⭐ ١. الجواب المختصر

**صورتين في اللقطة الواحدة = هذا هو المعيار الاحترافي، وعادي جداً.**

**ثلاث صور في لقطة واحدة = مستحيل تقنياً في Flow.** خانة الإطارات تقبل **إطار أول + إطار آخر** فقط.

> «Provide a starting and ending image with **Frames to Video**, and Flow will generate a seamless video that bridges the two.» — Google Blog

لكن الثلاث صور موجودة في **مكان آخر تماماً**، وهذا هو الالتباس اللي لازم يتوضّح:

| | **Frames to Video** | **Ingredients to Video** |
|---|---|---|
| **عدد الصور** | **٢** (أول + آخر) | **٣** (حد أقصى) |
| **دورها** | تحكم في **الحركة** — من وين لوين | تحكم في **الهوية** — شكل الشخصية والمكان |
| **المكان** | خانة `+ Add start frame` / `+ Add end frame` | خانة `Ingredients` |
| **المدى** | ٤ / ٦ / ٨ ثوان (١٠ في Omni Flash) | نفس الشي |

👉 **الاثنين لازم تستعملهم مع بعض.** الـ3 Ingredients يخلّي الأرنب يبقى نفس الأرنب. الـ2 Frames يخلّيو الحركة مرسومة، ما يخلّيهاش الـAI يخترعها.

---

## 🔗 ٢. فكرتك عن السلسلة — صحيحة ١٠٠٪

قلت: «اللقطة الأولى مع الثانية، والثانية مع الثالثة».

هذا اسمه **Chaining**، وهو الطريقة اللي يستعملها المحترفين فعلاً. الصورة اللي هي **إطار آخر** للقطة رقم N تولّي هي نفسها **إطار أول** للقطة رقم N+1. يعني صورة وحدة تخدم مرتين، والخياطة بين اللقطتين تكون مثالية بالبكسل.

**لكن فيه تحذير مهم:**
- **لا تسلسل كلشي.** إذا كل اللقطات مربوطة، تخرج **لقطة واحدة طويلة**، والكوميديا تموت — لأن الضحك يجي من **القطع** (cut).
- **سلسل الحركة الجسدية، اقطع في اللحظات الكوميدية.**

**عندنا:**
- ✅ **مربوط:** SC01A → SC01B → SC02 → SC03 → SC04A → SC04B → SC05 (حركة متصلة، نفس الكاميرا)
- ✂️ **مقطوع:** SC05 → SC06 (قطع إلى close-up — هذا هو البانش لاين)

---

## 📏 ٣. القاعدة: لقطة تحتاج صورة ولا صورتين؟

| نوع اللقطة | صور | مثال من الحلقة |
|---|---|---|
| **حركة جسدية بنهاية محددة** | **٢** | الثعلب يشدّ → الأرنب يفلت. لازم تعرف وين توصل بالضبط |
| **أداء / انفعال (performance)** | **١** | الأرنب يضحك ويكمز. الوجه يخدم وحده |
| **نتيجة لازم تكون مضبوطة** | **٢** | الكيس لازم يطيح على الثعلب، ماشي جانبو |

**الاختبار:** «واش نعرف نرسم بالكلمة وين بالضبط لازم توقف الصورة؟» إذا لا → صورتين.

---

## 🎞️ ٤. الجدول النهائي — ٨ مقاطع · ١٠ إطارات

| # | المقطع | المدة | الإطار A (البداية) | الإطار B (النهاية) | صور |
|---|---|---|---|---|---|
| 1 | **SC01A — TIE THE ROPE** | 4s | `KF01_TIE_THE_ROPE` 🆕 | `KF02_LIFT_THE_SACK` 🆕 | 2 |
| 2 | **SC01B — SET THE NET** | 4s | `KF02_LIFT_THE_SACK` | `SC01_THE_SETUP` ✅ | 2 |
| 3 | **SC02 — THE BAIT** | 6s | `KF04_EARS_PEEK_OUT` 🆕 | `SC02_THE_BAIT` ✅ | 2 |
| 4 | **SC03 — THE HAUL** | 6s | `SC02_THE_BAIT` | `SC03_THE_HAUL` ✅ | 2 |
| 5 | **SC04A — THE SLIP** ★ | 4s | `SC03_THE_HAUL` | `KF07_THE_SLIP` 🆕 | 2 |
| 6 | **SC04B — THE IMPACT** ★ | 4s | `KF07_THE_SLIP` | `SC04_THE_REVERSAL` ✅ | 2 |
| 7 | **SC05 — THE PAYOFF** | 6s | `SC04_THE_REVERSAL` | `SC05_THE_PAYOFF` ✅ | 2 |
| 8 | **SC06 — THE END** ✂️ | 6s | `SC06_THE_END` ✅ | — (الأداء حر) | **1** |

**المجموع: ٤٠ ثانية · ٨ مقاطع · ١٠ إطارات (٦ موجودة + ٤ جديدة)**

> 🆕 = وُلّدت في جولة الكيفريمات · ✅ = موجودة من V2
>
> **الإطارات المشتركة:** `KF02` يخدم مرتين (نهاية ١ / بداية ٢) · `SC02` مرتين (٣ / ٤) · `SC03` مرتين (٤ / ٥) · `SC04` مرتين (٦ / ٧) · `SC05` مرتين (٧ / ٨)
> → لهذا ٨ مقاطع ما تحتاجش ١٦ صورة، غير **١٠**.

---

## ⚙️ ٥. إعدادات Flow (نسخ حرفي)

```
Model .............. Veo 3.1 Fast   (يدعم Ingredients + 9:16)
Mode ............... Frames → First and last
Aspect ratio ....... 9:16  ← إلزامي
Duration ........... 4s أو 6s حسب الجدول
Outputs ............ 2 (باش تختار الأحسن)
Audio .............. OFF (نركّبو SFX في المونتاج)
```

> ⚠️ **Veo 3.1 Quality لا يدعم Ingredients.** إذا حبيت الجودة العالية، استعمل Fast للـIngredients ثم رقّي في المونتاج — ولا اشتغل بـQuality مع Frames فقط.

---

## 🎯 ٦. برومبتات الجسر (Bridge Prompts)

اكتبهم في خانة البرومبت مع الإطارين. **الإطارين = التركيب. البرومبت = الرحلة بينهم.**

### 1️⃣ SC01A — TIE THE ROPE · 4s
```
Same fox, same world, locked-off camera. The fox finishes the knot around the
giant carrot, pulls the rope tight once to test it, and nods to himself.
The empty burlap sack sits folded on the ground beside him. No rabbit.
Cartoon SFX: rope creak, a satisfied little "hmph" breath. No dialogue, no music.
```

### 2️⃣ SC01B — SET THE NET · 4s
```
Locked camera. The fox lifts the open burlap sack in both arms, swings it up,
and drapes it over the flat top of the grey boulder so it hangs ready. He then
ducks down behind the rock, out of sight, still holding the rope.
Cartoon SFX: fabric whoosh, light thump on stone, scurry of paws. No dialogue.
```

### 3️⃣ SC02 — THE BAIT · 6s
```
Locked camera. The rabbit pushes up out of the burrow — ears first, then his
whole head, then his shoulders in the blue denim vest. He stops. He sees the
giant carrot. His eyes go wide, ears snap forward, nose twitches fast, and a
thread of drool drops from his mouth. He leans toward the carrot.
Cartoon SFX: dirt crumble, sniffing, a tiny drip. No dialogue, no music.
```

### 4️⃣ SC03 — THE HAUL · 6s
```
Locked camera. Sudden: the rope snaps taut. The fox yanks from behind the rock
with everything he has — legs braced, leaning back, black paws clenched. The
rabbit is ripped off his feet and dragged across the grass, still hugging the
giant carrot with both arms. Grass and dust kick up. Rabbit's ears fly backward.
Cartoon SFX: rope twang, yelp, grass swish, comedic scramble. No dialogue.
```

### 5️⃣ SC04A — THE SLIP ★ · 4s
```
Locked camera. THE HINGE. The rabbit's paws slip off the carrot one by one —
first left, then right — and the carrot rolls away from him. The rope goes
SLACK and drops in a loose curve. Off-screen weight disappears.
Cartoon SFX: two soft pops as paws release, then the rope's tension dying.
No dialogue.
```

### 6️⃣ SC04B — THE IMPACT ★ · 4s
```
Locked camera. Physics takes over. The fox, still pulling with no resistance,
stumbles BACKWARD, both arms windmilling. His back SLAMS into the grey boulder.
The impact shakes the stone and knocks the burlap sack off the top — it drops
straight down over him. His straw hat spins off his head.
Cartoon SFX: whoosh, hollow THUD on stone, fabric flump, hat twirl.
No dialogue, no music.
```

### 7️⃣ SC05 — THE PAYOFF · 6s
```
Locked camera. The sack settles around the fox — he is now a lump on his back on
the ground, only his snout and one black paw out, hat lying flat beside him. He
blinks, dazed, one eye twitching. The rabbit scrambles up onto the boulder, sits,
and calmly eats a carrot, eyes closed, feet swinging.
Cartoon SFX: burlap rustle, a dizzy squeak, satisfied munching. No dialogue.
```

### 8️⃣ SC06 — THE END ✂️ · 6s (Frames → **First only**)
```
CUT to close-up. The rabbit bursts out laughing — mouth wide, eyes shut, ears
flopping — then points straight at the sacked fox. He aims a slow, cheeky wink
at the CAMERA. Above him the fox strains inside the sack, one black paw waving.
A strip of carrot peel drops onto the fox's hat brim.
Cartoon SFX: belly laugh, munch, a comedic defeated groan. No dialogue, no music.
```

---

## 🚫 ٧. Negative Prompt (نفسه في كل مقطع)

```
no text, no subtitles, no watermark, no logo,
no dialogue, no speaking, no lip-sync to speech, no music,
no extra characters, no second sack, no new props appearing,
no changed fur colors, no missing denim vest, no missing straw hat,
no camera movement, no zoom, no pan, no handheld shake,
no 16:9, no letterbox, no black bars,
no warping limbs, no morphing faces, no flickering,
no realistic photo, no injuries, no blood
```

---

## ✅ ٨. تصحيح الجزرة — تم

المشاكل اللي كانت في V2 وتصلّحت كلها:

| المشكلة | التصحيح |
|---|---|
| الجزرة **يمين** الجحر في SC01 · KF01 · KF02 | أُعيد توليدهم — الجزرة ولّات **يسار** |
| الجزرة **صغيرة** في SC03 · SC04 | أُعيد توليدهم — ولّات بطول الثعلب |
| **الحبل مربوط في الأرنب** في SC03 | أُعيد — العقدة ولّات في **وسط الجزرة** وظاهرة |
| الحبل **طايح في الهواء** في SC04 · KF07 | أُعيد — الحبل مربوط، والارتخاء ولّى ظاهر |
| KF07 بلا جزرة مربوطة | أُعيد |
| SC05 · SC06 بلا الجزرة العملاقة | أُعيدوا — الجزرة راقدة في الكادر |

**⛔ بلا `REF_CARROT_9x16` في المراجع → لا تولّد أي كادر فيها الجزرة.**

### ⚠️ ملاحظتين صغار مازالو
1. **SC03** — الكيس ماشي باين فوق الصخرة. القصة ما تنهارش (الكيس باين في SC02 وقبل ما يطيح في SC04)، لكن الأفضل نعاودو.
2. **SC06** — الجزرة راقدة لكن الاتجاه معكوس (الطرف يسار). مقبول في close-up.

---

## 🥕 ٧. قانون الجزرة (FROZEN)

> المرجع البصري: `01_REFERENCES/REF_CARROT_9x16.png` · التفاصيل في `01_REFERENCES/CARROT_SPEC.md`

```
ONE GIANT CARROT lying FLAT on the grass — thick rounded crown, tapering to ONE
single sharp point, warm orange body with darker orange ridges near the crown,
5 short bright-green leaf stalks, ONE thick brown twisted rope tied in a SIMPLE
KNOT around its exact MIDDLE. GREEN LEAVES point LEFT, SHARP TIP points RIGHT.
It is GIANT: its length equals the fox's standing height. Never upright, never
floating, never leaning.
```

| البند | القانون |
|---|---|
| **الحجم** | طولها = **طول الثعلب واقف** (~2× الأرنب) |
| **الشكل** | مخروط واحد · قمة مدوّرة · **طرف واحد حاد** |
| **الأوراق** | **5** سيقان خضراء قصيرة |
| **الحبل** | مربوط في **وسطها** بعقدة ظاهرة — **أبداً في الأرنب** |
| **الوضع** | راقدة **أفقياً** دائماً · ⛔ واقفة · ⛔ طايرة · ⛔ متكية |
| **المكان** | على العشب **يسار** فم الجحر |

---

## 📁 ٩. الملفات

```
03_SCENES/
├── SC01_THE_SETUP.png … SC06_THE_END.png      (6 · V2)
└── KEYFRAMES/
    ├── KF01_TIE_THE_ROPE.png        🆕 إطار أول SC01A
    ├── KF02_LIFT_THE_SACK.png       🆕 نهاية SC01A / بداية SC01B
    ├── KF04_EARS_PEEK_OUT.png       🆕 إطار أول SC02
    └── KF07_THE_SLIP.png            🆕 ★ إطار الانقلاب — الأهم في الحلقة
```

---

## 🧠 ١٠. خلاصة الجواب

1. **صورتين = عادي وهو الصح.** ثلاث صور في لقطة واحدة = **مستحيل** في Flow.
2. **٣ صور = Ingredients**، ووظيفتهم يثبّتو الهوية، ماشي الحركة.
3. **السلسلة اللي وصفتها صحيحة** — الإطار المشترك يخدم مرتين. لكن **اخلط**: سلسل الحركة، اقطع على الكوميديا.
4. **ماشي كل لقطة تحتاج صورتين.** لقطات الأداء (SC06) صورة وحدة تكفيها — والـAI يكمّل الوجه.
5. **الأهم:** الإطارات يحلّو مشكلة «الـAI يخترع الحركة». من ٨ مقاطع، ٧ ولّاو مرسومين بالبكسل من البداية للنهاية.
