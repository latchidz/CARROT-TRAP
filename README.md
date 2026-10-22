# 🥕 CARROT TRAP — Episode 01

**«فخ الجزرة العملاقة» · The Giant Carrot Trap**

سلسلة رسوم متحركة 3D صامتة للأطفال · Slapstick (Tom & Jerry) · 9:16 عمودي

| | |
|---|---|
| **المدة** | 40 ثانية (8 مقاطع) |
| **الإطارات** | 10 keyframes |
| **الصيغة** | 9:16 عمودي · PNG · 768×1376 |
| **الحوار** | لا شيء — صامت |
| **الصوت** | SFX كرتونية فقط · بلا موسيقى |
| **أداة التحريك** | Google Flow · Veo 3.1 · Frames to Video |

---

## ⭐ السلسلة السببية — قلب الحلقة

الحلقة كلها مبنية على فكرة واحدة: **الثعلب ينحبس في فخّه هو.** كل حدث مسبَّب بما قبله ومرئي في الكادر.

```
① SC01  الثعلب يربط الحبل في الجزرة
② SC01  الثعلب يعلّق كيس الخيش فوق الصخرة        ← الشبكة
③ SC01  الثعلب يختبئ وراء الصخرة ماسك الحبل
④ SC02  الأرنب يطلع من الجحر ويشوف الطُعم
⑤ SC03  الثعلب يشدّ → الأرنب يتجرّ
⑥ SC04  الأرنب يفلت من الجزرة                    ← نقطة الانقلاب
⑦ SC04  الحبل يرتخي
⑧ SC04  الثعلب مايل للور بكل ثقله
⑨ SC04  ظهره يضرب الصخرة
⑩ SC04  الارتطام يطيّح الكيس عليه                ← عدالة شعرية
```

### 🧭 الكيس = البوصلة

| المشاهد | موضع الكيس |
|---|---|
| SC01 → SC03 | فوق الصخرة (الشبكة جاهزة) |
| SC04 | ينزل في الهواء على الثعلب |
| SC05 → SC06 | ملفوف على الثعلب على الأرض |

---

## 📐 القاعدة الذهبية — استمرارية 100%

**كل كادر 9:16 · كاميرا مقفولة · لا حركة كاميرا · لا 16:9**

### الأرنب
```
أبيض ممتلئ الجسم · ودان طويلين واقفين (داخلي وردي) · عيون غامقة كبيرة
أنف وردي · سنّان أماميان · ذيل قطني
سترة جينز زرقاء فاتحة بلا أكمام — وحيدة، بلا قميص أو بنطال أو حذاء
```

### الثعلب
```
برتقالي نحيف طويل · ذيل كثّ مع طرف أبيض · صدر كريمي · كفوف سوداء · أطراف ودان سوداء
قبعة قش صفراء قديمة مستهلكة، حافة عريضة، رقعة بنية على اليسار، مائلة — وحيدة
```

### المكان
```
جذع صنوبر ضخم على المحور العمودي المركزي · الجحر عند قاعدته على خط الوسط
صخرة رمادية كبيرة على اليمين، أقرب للكاميرا · إضاءة ذهبية
```

### 📏 قانون الحجم
- الثعلب = **2.3×** الأرنب
- قمة ودن الأرنب = **وسط صدر** الثعلب
- راس الثعلب = **أكبر من جسم الأرنب كامل**

---

## 🎬 الجدول النهائي — 8 مقاطع

| # | المقطع | المدة | الإطار A | الإطار B |
|---|---|---|---|---|
| 1 | SC01A — TIE THE ROPE | 4s | `KF01` | `KF02` |
| 2 | SC01B — SET THE NET | 4s | `KF02` | `SC01` |
| 3 | SC02 — THE BAIT | 6s | `KF04` | `SC02` |
| 4 | SC03 — THE HAUL | 6s | `SC02` | `SC03` |
| 5 | **SC04A — THE SLIP** ★ | 4s | `SC03` | `KF07` |
| 6 | **SC04B — THE IMPACT** ★ | 4s | `KF07` | `SC04` |
| 7 | SC05 — THE PAYOFF | 6s | `SC04` | `SC05` |
| 8 | SC06 — THE END ✂️ | 6s | `SC06` | — (أداء حر) |

★ = نقطة الانقلاب · ✂️ = قطع إلى close-up

> **10 إطارات فقط لـ8 مقاطع** — لأن كل إطار وسطاني يخدم مرتين: نهاية مقطع وبداية اللي بعده.

---

## ⚙️ كيفاش تحرّك في Google Flow

```
Model ....... Veo 3.1 Fast     (Quality لا يدعم Ingredients)
Mode ........ Frames → First and last
Ratio ....... 9:16
Duration .... 4s / 6s
Outputs ..... 2
Audio ....... OFF
```

**صورتين لكل لقطة = المعيار.** Flow يقبل إطار أول + إطار آخر فقط.
**٣ صور = خانة Ingredients** (شخصية + جسم + مكان) — للهوية ماشي للحركة.

برومبتات الجسر الكاملة (Word-for-word) في [`02_STORYBOARD/KEYFRAME_MAP_FLOW.md`](02_STORYBOARD/KEYFRAME_MAP_FLOW.md).

---

## 📁 هيكل المشروع

```
CARROT_TRAP/
├── 01_REFERENCES/          مراجع الشخصيات والمكان وقانون الحجم
│   ├── REF_SCALE_9x16.png          ⭐ قانون الحجم الإلزامي
│   ├── REF_RABBIT_SCENE_9x16.png
│   ├── REF_FOX_SCENE_9x16.png
│   ├── REF_BURROW_RABBIT_9x16.png · REF_FOX_DEN_9x16.png
│   ├── REF_LOCATION_9x16.png · REF_RABBIT.png · REF_FOX.png · REF_LOCATION.png
│   └── STEP1_PROMPTS.md
├── 02_STORYBOARD/
│   ├── MASTER_PRODUCTION_MEMO_V2.md     ← السلسلة السببية + خطة اللقطات
│   ├── KEYFRAME_MAP_FLOW.md             ← ⭐ 8 مقاطع + برومبتات الجسر
│   └── STORYBOARD.md
├── 03_SCENES/              الإطارات العشرة
│   ├── SC01_THE_SETUP.png … SC06_THE_END.png
│   └── KEYFRAMES/
│       ├── KF01_TIE_THE_ROPE.png
│       ├── KF02_LIFT_THE_SACK.png
│       ├── KF04_EARS_PEEK_OUT.png
│       └── KF07_THE_SLIP.png            ★ إطار الانقلاب
├── 04_ANIMATION/           برومبتات التحريك (توقيت بالثواني + SFX + Negative)
│   └── ANIM_SC01.txt … ANIM_SC06.txt
├── CARROT_TRAP_CONTACT_SHEET.png        ورقة الاتصال — 6 لوحات
└── KEYFRAME_CHAIN_SHEET.png             ⭐ خريطة السلسلة — A → B
```

---

## 🚫 Negative Prompt الثابت

```
no text, no subtitles, no watermark, no logo,
no dialogue, no speaking, no music,
no extra characters, no second sack, no new props,
no changed fur colors, no missing denim vest, no missing straw hat,
no camera movement, no zoom, no pan,
no 16:9, no letterbox, no warping limbs, no morphing faces,
no realistic photo, no injuries, no blood
```

---

## 🥕 قانون الجزرة (FROZEN)

المرجع البصري: [`01_REFERENCES/REF_CARROT_9x16.png`](01_REFERENCES/REF_CARROT_9x16.png) · التفاصيل: [`CARROT_SPEC.md`](01_REFERENCES/CARROT_SPEC.md)

| البند | القانون |
|---|---|
| **الحجم** | طولها = **طول الثعلب واقف** (~2× الأرنب) |
| **الشكل** | مخروط واحد · قمة مدوّرة · طرف واحد حاد · **5** سيقان خضراء |
| **الحبل** | عقدة في **وسطها** — أبداً في الأرنب |
| **الوضع** | راقدة أفقياً دائماً · ⛔ واقفة · ⛔ طايرة · ⛔ متكية |
| **المكان** | على العشب **يسار** فم الجحر |

### ✅ تصحيحات V3

| كان | ولّى |
|---|---|
| الجزرة يمين الجحر في SC01/KF01/KF02 | **يسار** |
| الجزرة صغيرة في SC03/SC04 | بطول الثعلب |
| الحبل مربوط في **الأرنب** في SC03 | **في وسط الجزرة** |
| الحبل طايح في الهواء | مربوط، والارتخاء ظاهر |
| SC05/SC06 بلا الجزرة العملاقة | الجزرة راقدة في الكادر |

---

## 📥 التحميل — V3.2

### ⭐ زيب واحد: برومبتات + مشاهد + مراجع

**https://github.com/latchidz/CARROT-TRAP/releases/download/v3.2/CARROT_TRAP_EP01_V32_PROMPTS_AND_SCENES.zip**

`35 ملف · 46.4 MB`

```
CARROT_TRAP_EP01/
├── 00_READ_FIRST_AR.md      ← دليل البدء
├── PROMPTS/                 9 ملفات (خريطة الإطارات · برومبتات الجسر · التحريك)
├── SCENES/                  6 مشاهد + KEYFRAMES/ 4 إطارات
├── REFERENCES/              11 ملف (منهم REF_CARROT ⭐ + CARROT_SPEC)
└── SHEETS/                  ورقة الاتصال + خريطة السلسلة
```

| | الرابط |
|---|---|
| **المستودع** | https://github.com/latchidz/CARROT-TRAP |
| **كل الإصدارات** | https://github.com/latchidz/CARROT-TRAP/releases |
| **صورة فرادى (raw)** | `https://raw.githubusercontent.com/latchidz/CARROT-TRAP/main/03_SCENES/KEYFRAMES/KF07_THE_SLIP.png` |

---

*Built with Arena.ai · 2026-10-22*
