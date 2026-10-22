# 🥕 فخ الجزرة العملاقة — الخطوة الأولى
## بناء المراجع الأساسية (Reference Generation)

**السلسلة:** حلقة تجريبية · 3D Animation · صامتة · Slapstick (Tom & Jerry)
**التاريخ:** 22/10/2026

---

## 🧭 المبدأ اللي كنخدمو بيه

الاستمرارية 100% **ما تجيش من البرومبت وحدو** — تجي من **المراجع**.

كل لقطة في الحلقة غادي تتولّد وهي **كتاخد المراجع كصور إدخال** (Image 1 / Image 2 / Image 3).
ماشي غير وصف بالكلام. هذا هو الفرق بين «قريب» و«نفس الشي بالضبط».

| المرجع | الدور |
|---|---|
| **REF_RABBIT** | وجه/جسم/لباس الأرنب — ما يتبدّلش أبداً |
| **REF_FOX** | وجه/جسم/قبعة الثعلب — ما يتبدّلش أبداً |
| **REF_LOCATION** | الجغرافيا: الشجرة · الجحر · الصخرة — الكاميرا تدور وهي ثابتة |

---

## 🗺️ الخريطة الجغرافية الثابتة (Spatial Map)

قبل أي لقطة، نتفقو على المحاور. **كل وصف لاحق كيتبع هذا الجدول:**

```
                    ▲ NORTH (العمق — ورا الشجرة)
                    │
        [ غابة ]    │
                    │
    WEST ─────── (0,0) ─────── EAST
   (يسار الكادر)   الشجرة        (يمين الكادر)
                 │      \
                 │       \
            الجحر (Burrow)   الصخرة (Rock)
                 │           (+4m شرق, +1m قدام)
                    ▼ SOUTH (نحو الكاميرا)
```

> 🔒 **مثبّتة من `REF_LOCATION.png` — الصورة هي الحقيقة، ماشي البرومبت.**

| الجسم | البلاصة الدقيقة (من الصورة) | ملاحظة |
|---|---|---|
| **الشجرة (Pine)** | **مركز الكادر بالضبط** — (0,0) | جذع عمودي، الجذور مفرودة على الأرض |
| **الجحر (Burrow)** | **أسفل الجذع مباشرة، على محور الجذع** | الفتحة دائرية سوداء · كومة تراب داكن حواليها · قطرها ~كرة قدم |
| **الصخرة (Rock)** | **يمين الكادر** · ~2.5 مرة عرض الجذع من المركز · **أقرب للكاميرا** | كبيرة مستديرة، وجهها الأعلى مفلطح، عليها ليكين |
| **الأشجار الخلفية** | خلفية ضبابية فقط — **ما تدخلش أبداً** في الـ midground | treeline بعيد |
| **الأرنب** | بيته = الجحر | يخرج/يدخل من **نفس الفتحة** دائماً |
| **الثعلب** | يدخل من **الغابة الشمالية** (ورا الشجرة) | ماشي من اليمين ولا اليسار |

**المسافات المرجعية (بالنسبة لقطر جذع الشجرة = 1 وحدة):**

```
الشجرة ─── 3 وحدات ─── الصخرة        (أفقياً، شرق)
الجحر  ← 0.5 وحدة قدام قاعدة الجذع    (جنوباً، نحو الكاميرا)
الصخرة ← 2 وحدة قدام الشجرة           (أقرب للكاميرا)
```

### 🎥 قاعدة الزوايا
| الزاوية | الشجرة | الجحر | الصخرة |
|---|---|---|---|
| **Wide (الكاميرا جنوب)** | وسط | قدام-يسار | يمين |
| **Reverse (الكاميرا شمال)** | وسط | ورا-يمين (معكوس) | يسار |
| **Close-up** | خارج الكادر أو blurred | — | — |

> ⚠️ في الزاوية المعكوسة، **المواقع تنقلب بصرياً** — لكنها **نفس الجغرافيا**. هذا ماشي خطأ.

---

# 📝 البرومبتات (English — جاهزة للنسخ)

## 1️⃣ REF_RABBIT — Character Turnaround

```
Professional 3D animated character turnaround sheet for a children's slapstick
comedy, Pixar-quality feature animation rendering, soft global illumination,
subsurface scattering on fur.

CHARACTER — THE RABBIT:
A small chubby white rabbit with a round pear-shaped body that is slightly
chunky. Very long upright ears with soft pink inner ears. Big expressive dark
eyes with round white highlights. Small pink triangular nose. Two prominent
white buck teeth. Fluffy round white cotton tail. Short chubby legs, oversized
fluffy feet. His face reads CHEERFUL AND INNOCENT on the surface, with a tiny
mischievous glint in the eyes.

CLOTHING — EXACTLY THIS AND NOTHING ELSE:
One light-wash blue denim vest, sleeveless, frayed raw armholes, open at the
front, worn over bare white fur. No shirt underneath. No trousers. No shoes.
No hat. No accessories.

LAYOUT:
Four full-body views of THE SAME character arranged in a single row on a plain
light grey (#d8d8d8) seamless studio background:
(1) front view, (2) three-quarter view, (3) full side profile facing right,
(4) back view.
IDENTICAL body proportions, identical fur colour and markings, identical vest
colour and stitching in ALL FOUR views. All four standing on the same invisible
ground line, feet aligned at the same height.

LIGHTING: soft even studio lighting, no harsh shadows, no floor plane, no gradient.

NO TEXT, NO LETTERS, NO NUMBERS, NO LABELS, NO WATERMARK, NO LOGO, NO BORDER.
```

---

## 2️⃣ REF_FOX — Character Turnaround

```
Professional 3D animated character turnaround sheet for a children's slapstick
comedy, Pixar-quality feature animation rendering, soft global illumination,
subsurface scattering on fur.

CHARACTER — THE FOX:
A tall, thin, lanky orange fox. Narrow elongated body, long slim legs, slim
waist. Long bushy fox tail with a bright WHITE tip. Pointed muzzle, small black
nose. Narrow sly amber-yellow eyes with heavy half-closed eyelids. Black paws
and black ear tips. Cream-white chest and belly, burnt-orange back and tail.
His face reads CUNNING, but the wide vacant pupils make him look clearly
CLUMSY AND DIM-WITTED.

CLOTHING — EXACTLY THIS AND NOTHING ELSE:
One old rural straw hat. Wide flat circular brim, woven yellow-tan straw, worn
and slightly frayed at the edge with one small tear in the brim and one small
dark brown patch on the left side. The hat sits tilted slightly on his head.
No other clothing. No shirt. No trousers. No shoes.

LAYOUT:
Four full-body views of THE SAME character arranged in a single row on a plain
light grey (#d8d8d8) seamless studio background:
(1) front view, (2) three-quarter view, (3) full side profile facing right,
(4) back view.
IDENTICAL body proportions, identical fur colour and markings, identical hat
shape, colour and tilt in ALL FOUR views. All four standing on the same
invisible ground line, feet aligned at the same height.

LIGHTING: soft even studio lighting, no harsh shadows, no floor plane, no gradient.

NO TEXT, NO LETTERS, NO NUMBERS, NO LABELS, NO WATERMARK, NO LOGO, NO BORDER.
```

---

## 3️⃣ REF_LOCATION — Master Wide Establishing Shot

```
Cinematic master wide establishing shot of an EMPTY forest clearing for a 3D
animated children's film. Pixar-quality lighting, warm golden late-afternoon
sunlight, soft volumetric sun rays, lush saturated colours, gentle depth of
field. NO characters, NO animals, NO people — the scene is completely empty.

GEOGRAPHY — EXACTLY THIS AND NOTHING ELSE:

1. ONE massive pine tree standing in the EXACT CENTRE of the frame. Tall,
   vertical, thick brown trunk with deeply textured bark, dense dark-green
   needles, roots spreading visibly into the grass at ground level.

2. Directly at the BASE of that trunk, positioned slightly LEFT of the trunk's
   centre line, a dark rounded RABBIT BURROW hole, roughly the size of a
   football, with a small mound of loose dark earth around its rim.

3. On the RIGHT side of the frame, roughly one third of the way in from the
   right edge and noticeably CLOSER to the camera than the tree, ONE large
   smooth rounded GREY BOULDER, about the size of a kitchen chair, with a flat
   top and a few lichen patches.

4. Flat open soft green grass clearing filling the foreground and middle
   ground. Scattered small wildflowers and a few fallen pine cones at the edges.
   Other pine trees ONLY in the far background, forming a soft blurred treeline.

CAMERA: wide 16:9 cinematic frame, low eye-level camera at roughly one metre
height, completely static, deep focus so tree, burrow and boulder are all sharp.

CONSTRAINTS: no other rocks, no other burrows, no other large trees in the
foreground or middle ground, no paths, no fences, no buildings, no props, no
carrots, no signs.

NO TEXT, NO SUBTITLES, NO WATERMARK, NO LOGO.
```

---

## 📁 الملفات المتوقعة

| الملف | واش فيه |
|---|---|
| `REF_RABBIT.png` | ورقة تصميم الأرنب — 4 زوايا |
| `REF_FOX.png` | ورقة تصميم الثعلب — 4 زوايا |
| `REF_LOCATION.png` | اللقطة التأسيسية الفارغة |

---

## ✅ بوابة الموافقة

**الخطوة 2 (القصة واللقطات) ما كتبداش** حتى توافق على هاذ الثلاثة.
إذا حاجة ما عجباتكش (لون السترة · شكل القبعة · بلاصة الصخرة) — نصححو دروك،
قبل ما نبنيو 6 لقطات فوقهم.

---

# 🔄 تحديث 22/10 — الشكل النهائي **9:16 عمودي**

**قرار العميل:** كل المشاهد عمودية 9:16 · **مشاهد** ماشي أوراق تصميم.

## الملفات المعتمدة (9:16 · 768×1376)

| # | الملف | الدور |
|---|---|---|
| 1 | `REF_RABBIT_SCENE_9x16.png` | هوية الأرنب + ثبات المكان |
| 2 | `REF_FOX_SCENE_9x16.png` | هوية الثعلب + ثبات المكان |
| 3 | `REF_LOCATION_9x16.png` | **الجغرافيا القانونية** — بلا شخصيات |

> ⚠️ أوراق التصميم الأفقية (`REF_RABBIT` · `REF_FOX`) **تبقى مرجع هوية فقط** — ما تدخلش ككادر. المشاهد كلها 9:16.

## 🔒 الجغرافيا المثبّتة (من `REF_LOCATION_9x16.png`)

```
┌─────────────────────┐
│                     │   ← قمة الجذع تخرج من فوق
│         █           │
│         █           │   الجذع = محور عمودي في المركز
│         █           │
│         █           │
│      ( () )   ▓▓▓   │   الجحر في قاعدة الجذع (وسط) · الصخرة يمين
│   ░░░░░░░░░░░░░░░   │
└─────────────────────┘
        ▲ الكاميرا
```

| العنصر | الإحداثي (بالكادر 9:16) |
|---|---|
| **الجذع** | **المحور العمودي المركزي** — من فوق حتى ⅔ الكادر |
| **الجحر** | قاعدة الجذع · **مركز أفقياً** · ~⅛ من أسفل الكادر |
| **الصخرة** | **يمين** · أسفل · **أقرب للكاميرا** من الجذع |
| **الأرنب** | **يسار الجحر** (بين الجذع والحافة اليسرى) |
| **الثعلب** | **يمين** · قريب من الصخرة |

**قوانين ما تتبدّلش:**
1. الجذع دائماً **مركزي** — حتى في الزاوية المعكوسة.
2. الجحر **ملاصق لقاعدة الجذع دائماً** — ما يتنقلش.
3. الصخرة **يمين الكادر** دائماً (تنقلب يسار فقط في Reverse).
4. الأرنب **قصير** (⅓ الكادر) · الثعلب **طويل ونحيف** (⅓.5) — الفرق في الطول جزء من الهوية.
5. الأرضية عشب · الإضاءة ذهبية دافية — **ما تتبدّلش**.

## 🎯 برومبتات 9:16 — النسخة المعتمدة

البرومبتات الكاملة في الملف تحت كل صورة. القاعدة:

```
VERTICAL 9:16 PORTRAIT cinematic scene ... 9:16 portrait frame (1080x1920)
+ "IMAGE 1 = THE ENVIRONMENT · IMAGE 2 = THE CHARACTER IDENTITY CARD"
+ "Reproduce the environment of IMAGE 1 exactly ... Do NOT move, add or remove anything."
+ "Copy the face and the fur and the vest/hat with photographic fidelity."
```

**كل لقطة قادمة في الحلقة = نفس هذه الصيغة الثلاثية.**
